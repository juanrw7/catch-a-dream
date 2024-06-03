from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


TYPES = (
  ('J', 'Just a Dream'),
  ('N', 'Nightmare'),
  ('R', 'Recurring'),
  ('C', 'Comforting'),
  ('W', 'Weird'),
)

# Create your models here.
class Dream(models.Model):
  title = models.CharField(max_length=75)
  description = models.TextField(max_length=4000)
  date = models.DateField('Dream date')
  type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  def str_type(self):
    return self.get_type_display()
  
  def get_absolute_url(self):
      return reverse("dream-detail", kwargs={"dream_id": self.id})
  