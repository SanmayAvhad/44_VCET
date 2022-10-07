from django.contrib import admin
from django.urls import path, include
from In_the_loop import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index')
   path('', views.index, name='index'),


   path('form.html', views.form),
   path('button.html', views.button),
   path('chart.html', views.chart),
   path('element.html', views.element),
   path('signin.html', views.signin),
   path('signup.html', views.signup),
   path('table.html', views.table),
   path('blank.html', views.blank), 
   path('typography.html', views.typography),
   path('widget.html', views.widget),
]
