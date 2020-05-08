from rest_framework.routers import DefaultRouter

from user.views import UserViewSet, FarmCategoryViewSet, FarmProduceViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'category', FarmCategoryViewSet, basename='category')
router.register(r'produce', FarmProduceViewSet, basename='produce')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = router.urls
