from django.urls import path
from salem import views
from django.views.generic.base import TemplateView  # import TemplateView

urlpatterns = [
    path('', views.carMeet, name='carMeet'),
    path('setup.html', views.setup, name='setup'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('disclaimer.html', views.disclaimer, name='disclaimer'),
    path('redirect.html', views.dataInput, name='redirect')
    #     path("robots.txt",TemplateView.as_view(template_name="templates/robots.txt", content_type="text/plain")),  #add the robots.txt file
]
