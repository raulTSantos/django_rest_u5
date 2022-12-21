
from rest_framework import routers
from .api import PaymentSetView

router = routers.DefaultRouter()

router.register(r'pagos', PaymentSetView, 'payments_urls')

urlpatterns = router.urls