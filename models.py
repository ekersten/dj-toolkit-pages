from django.db import models
from model_utils.models import TimeStampedModel
from tags.models import Taggable
from core.models import Shareable
from core.models import Publishable
from core.models import Approveable

# Create your models here.

class Page(TimeStampedModel, Taggable, Shareable, Approveable, Publishable):
    title = models.CharField(max_length=200)
    body = models.TextField()
