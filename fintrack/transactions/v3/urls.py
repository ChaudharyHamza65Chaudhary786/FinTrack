from rest_framework.routers import DefaultRouter

from .views import TransactionViewset

router = DefaultRouter()
router.register('', TransactionViewset, basename='transaction')

urlpatterns = router.urls
