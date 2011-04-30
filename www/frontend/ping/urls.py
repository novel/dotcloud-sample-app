from django.conf.urls.defaults import *

from frontend.ping.views import index, workers, job

urlpatterns = patterns('',
        (r'^$', index),
        (r'workers$', workers),
        (r'job/(?P<job_id>\d+)/', job),
)
