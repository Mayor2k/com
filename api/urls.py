from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'menu-items', views.MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.UserAuth.as_view()),
]