from django.urls import path

from . import views

app_name='registration'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:course_id>/like/', views.like, name='like'),
    path('<int:course_id>/', views.add_name, name='add_name'),
]
