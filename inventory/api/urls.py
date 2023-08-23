from rest_framework import routers

from .views import PlaceViewSet

router = routers.SimpleRouter()
router.register(r"places", PlaceViewSet)

urlpatterns = router.urls
