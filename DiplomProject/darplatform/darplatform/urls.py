from django.contrib import admin
from django.urls import path, include
from dar import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('main/', views.load_main, name='main'),
    path('registration/', views.registration, name='registration'),
    path('student/', include('student.urls'), name='student'),
    path('subject/', include('subject.urls'), name='subject'),
    path('teacher/', include('teacher.urls'), name='teacher'),
    path('dar/', include('dar.urls'), name='dar'),
]
