from django.urls import path
from . import views

app_name = 'movieapp'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Movielist.as_view(), name='home'),
    path('movie/<int:pk>/', views.MovieDetail.as_view(), name='details'),
    # path('movie/<int:movie_id>/', views.detail, name='details'),
    # path('add/', views.add, name='add'),
    path('add/', views.Addview.as_view(), name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
