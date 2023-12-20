from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('job/<int:id>',views.jobDetails,name='jobDetail')
]
