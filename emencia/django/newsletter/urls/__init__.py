"""Default urls for the emencia.django.newsletter"""
from django.conf.urls.defaults import *

urlpatterns = patterns('',                       
                       url(r'^mailing/', include('emencia.django.newsletter.urls.mailing_list')),
                       url(r'^tracking/', include('emencia.django.newsletter.urls.tracking')),
                       url(r'^statistics/', include('emencia.django.newsletter.urls.statistics')),
                       url(r'^', include('emencia.django.newsletter.urls.newsletter')),
                       )
