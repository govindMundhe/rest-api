from django.contrib import admin
from .views import OrderViewSet , ItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'item', ItemViewSet)

urlpatterns = router.urls