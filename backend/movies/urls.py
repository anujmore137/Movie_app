from django.urls import path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register('movies', MoviesViewSet)
urlpatterns = router.urls


# urlpatterns = [
#     path('movies/', index)
# ]
