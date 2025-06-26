# imports

from __future__ import absolute_import , unicode_literals
from celery import Celery
import os
#--------------------------------------------------------------
#default setings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','body.settings')
app = Celery('body')
#--------------------------------------------------------------
#here we load task for all registered django app configs

app.config_from_object('django.conf:settings', namespace='CELERY')
#--------------------------------------------------------------
#discovers task automatically

app.autodiscover_tasks()
#--------------------------------------------------------------
#task

@app.task(bind=True)
def debug_tasks(self):
    print(f'request:{self.request!r}')