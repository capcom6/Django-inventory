from rest_framework import routers

from .views import (
    PlaceViewSet,
    GroupViewSet,
    NomenclatureTypeViewSet,
    NomenclatureViewSet,
    NomenclatureInstanceViewSet,
    CharacteristicViewSet,
    # CharacteristicValueSerializer,
)

router = routers.SimpleRouter()

router.register(r"places", PlaceViewSet)
router.register(r"group", GroupViewSet)
router.register(r"nomenclature_type", NomenclatureTypeViewSet)
router.register(r"nomenclature", NomenclatureViewSet)
router.register(r"nomenclature_instance", NomenclatureInstanceViewSet)
router.register(r"characteristic", CharacteristicViewSet)
# router.register(r"characteristic_value", CharacteristicValueSerializer)

urlpatterns = router.urls
