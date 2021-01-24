from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGAUGE_ELGLISH = "en"
    LANGAUGE_KOREAN = "kr"

    LANGAUGE_CHOICES = (
        (LANGAUGE_ELGLISH, "English"),
        (LANGAUGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw"),
    )

    avatar = models.ImageField("프로필사진", null=True, blank=True)
    gender = models.CharField(
        "성별", choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField("사용자정보", default="", blank=True)
    birthdate = models.DateField("생년월일", null=True)
    langauge = models.CharField(
        "언어유형", choices=LANGAUGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        "화폐유형", choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField("호스트권한", default=False)
