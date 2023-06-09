from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    # path('list/', views.movie_list, name = 'movie-list'),
    # path('<int:pk>/', views.movie_details, name = 'movie-details'),
    path('list/', views.MovieListAV.as_view(), name = 'movie-list'),
    path('<int:pk>/', views.MovieDetailAV.as_view(), name = 'movie-details'),
]
