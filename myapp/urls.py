# from django.urls import path
# from .import views
# from django.urls import path
# from .import views
# urlpatterns = [
#     # path('movie/', views.moviesInfo, name='movie_page'),
#     # path('sports/', views.sportsInfo, name='sports_page'),
#     # path('politics/', views.politicsInfo,name='politics_page'),
#     path('', views.index),
       
# ]

from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('product',views.product, name='product'),
]