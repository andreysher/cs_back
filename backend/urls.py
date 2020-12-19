from rest_framework import routers
from django.urls import path
from backend.api import ListViewSet

router = routers.DefaultRouter()
router.register('api/lists', ListViewSet, 'lists')

urlpatterns = router.urls