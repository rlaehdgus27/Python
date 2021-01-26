from django.db import models
from core import models as core_models
from users import models as users_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField(users_models.User, blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
