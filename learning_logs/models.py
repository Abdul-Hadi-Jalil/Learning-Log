from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200) # this attribute is used to store small data in text like names age etc with a max limit of 200 characters
    date_added = models.DateTimeField(auto_now_add=True) # this attribute is to store the current date and time when a new entry is created by user.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        "To display something to the user we used text attribute"
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.text[:50] + '...' if len(self.text) > 50 else self.text