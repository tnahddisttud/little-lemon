from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path
from . import views

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
    path('booking/', include(router.urls), name='booking'),
    path('api-token-auth/', obtain_auth_token)
]