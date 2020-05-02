
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from students import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html')),
    re_path(r'^api/students/$', views.students_list),
    re_path(r'^api/students/(?P<pk>[0-9]+)$', views.students_detail),
]
