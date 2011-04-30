import subprocess

from celery.task import task

@task
def ping(host):
    command = ["ping", "-c", "60", "-q", host]

    retcode = subprocess.call(command, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    return 0 == retcode
