from django.urls import path

from . import views

app_name='registration'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /registration/5/
    path('<int:course_id>/', views.detail, name='detail'),
    # ex: /registration/5/results/
    path('<int:course_id>/results/', views.results, name='results'),
    # ex: /registration/5/vote/
    path('<int:course_id>/register/', views.register, name='register'),
]