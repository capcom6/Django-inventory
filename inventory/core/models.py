from django.db import models


# Create your models here.
class Status(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"


StatusField = models.CharField(
    max_length=16, choices=Status.choices, default=Status.ACTIVE
)


class TimestampedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimestampedModel):
    status = StatusField
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Place(BaseModel):
    address = models.CharField(max_length=128)


class Group(BaseModel):
    place = models.ForeignKey(Place, related_name="groups", on_delete=models.RESTRICT)
    comment = models.TextField(blank=True, null=True)


class NomenclatureType(BaseModel):
    pass


class Nomenclature(BaseModel):
    type = models.ForeignKey(
        NomenclatureType, related_name="nomenclatures", on_delete=models.RESTRICT
    )
    characteristics = models.ManyToManyField(
        "Characteristic", related_name="nomenclatures", through="CharacteristicValue"
    )


class NomenclatureInstance(TimestampedModel):
    status = StatusField
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.RESTRICT)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    comment = models.TextField(blank=True, null=True)


class Characteristic(BaseModel):
    type = models.ForeignKey(
        NomenclatureType, related_name="characteristics", on_delete=models.RESTRICT
    )


class CharacteristicValue(models.Model):
    value = models.CharField(max_length=128)
    characteristic = models.ForeignKey(
        Characteristic, related_name="characteristic_values", on_delete=models.RESTRICT
    )
    nomeclature = models.ForeignKey(
        Nomenclature, related_name="characteristic_values", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.characteristic}: {self.value}"

    class Meta:
        unique_together = ("characteristic", "nomeclature")
