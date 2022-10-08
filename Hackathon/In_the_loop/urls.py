from django.contrib import admin
from django.urls import path, include
from In_the_loop import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index')
   path('', views.index, name='index'),
   
   path('index.html', views.index),
   path('Schedule.html', views.Schedule),
   path('OpenAi.html', views.OpenAi),
   path('chart.html', views.chart),

]
