from celery import task
from celery import registry
from celery.task.control import inspect
from celery.execute import send_task
from celery.result import AsyncResult

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext

from frontend.ping.models import PingJob, PingJobForm

def index(request):
    if request.method == "POST":
        form = PingJobForm(request.POST)
        job = form.save(commit=False)

        # send task
        task = send_task('ping.ping', [job.host])

        job.task_id = task.task_id
        job.save()

        return redirect(job)
    else:
        print registry.tasks
        form = PingJobForm()
        return render_to_response("index.html",
                    RequestContext(request, {"form": form})
                )

def workers(request):
    stats = inspect().stats()

    return render_to_response("workers.html",
                RequestContext(request, {"stats": stats})
            )

def job(request, job_id):
    task = PingJob.objects.get(id=job_id)

    if 'NEW' == task.status:
        result = AsyncResult(task.task_id)
        if result.ready():
            task.status = 'Completed'
            task.result = '%s is %s' % (task.host,
                    {True: "up", False: "down"}[result.result])
            task.save()

    return render_to_response("job.html",
                RequestContext(request, {"job": task})
           )
