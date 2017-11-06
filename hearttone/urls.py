"""hearttone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views import static

from records import views
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    # Records urls
    url(r'^$', views.PatientList.as_view(), name='home'),
    # url(r'^patient/add/$', views.PatientRecordCreateView.as_view(), name='patient_add'),
    # url(r'^patient/(?P<pk>\d+)/edit/$', views.PatientRecordUpdateView.as_view(), name='patient_edit'),
    url(r'^patient/add/$', views.edit_patient, name='patient_add'),
    url(r'^patient/(?P<id_patient>\d+)/edit/$', views.edit_patient, name='patient_edit'),
    url(r'^patient/(?P<pk>\d+)/delete/$', views.PatientDeleteView.as_view(), name='patient_delete'),

    url(r'^admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve,
            {'document_root': MEDIA_ROOT}),
    ]