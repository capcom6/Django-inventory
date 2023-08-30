from rest_framework import routers

from .views import PlaceViewSet, GroupViewSet

router = routers.SimpleRouter()
router.register(r"places", PlaceViewSet)
router.register(r"places/(?P<place_id>\d+)/groups", GroupViewSet, "group")
# router.register(r"groups", GroupViewSet)

urlpatterns = router.urls
