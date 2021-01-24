from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as users_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Abject Definition """

    class Meta:
        verbose_name_plural = "객실유형"


class Amenity(AbstractItem):

    """ Amenity Abject Definition """

    class Meta:
        verbose_name_plural = "편의시설"


class Facility(AbstractItem):

    """ Facility Abject Definition """

    class Meta:
        verbose_name_plural = "일반시설"


class HouseRules(AbstractItem):

    """ HouseRules Abject Definition """

    class Meta:
        verbose_name_plural = "규칙"


# #################### Main Class ####################


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    class Meta:
        verbose_name_plural = "객실"

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)

    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()

    check_in = models.TimeField()
    check_out = models.TimeField()

    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(users_models.User, on_delete=models.CASCADE)

    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRules, blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    class Meta:
        verbose_name_plural = "사진"

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
