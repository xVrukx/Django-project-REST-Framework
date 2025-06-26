#imports
from __future__ import unicode_literals,absolute_import
'''makes sure that app is imported so that whenever djanjo starts in shared task app is used'''
from .celery import app as celery_app

#-------------------------------------------
__all__ = ['celery_app']