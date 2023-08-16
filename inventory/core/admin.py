from django.contrib import admin
from .models import (
    Place,
    Group,
    Nomenclature,
    NomenclatureInstance,
    NomenclatureType,
    Characteristic,
    CharacteristicValue,
)

# Register your models here.
admin.site.register(
    [
        Place,
        Group,
        Nomenclature,
        NomenclatureInstance,
        NomenclatureType,
        Characteristic,
        CharacteristicValue,
    ]
)
