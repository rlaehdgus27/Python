from django.db import models
from core import models as core_models
from users import models as users_models
from rooms import models as rooms_models


class Review (core_models.TimeStampedModel):

    """ Review Modle Definition """

    content = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(rooms_models.Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} - {self.room}'
