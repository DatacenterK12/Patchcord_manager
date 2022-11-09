from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Cross(models.Model):
    name = models.CharField(max_length=5)
    ten = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )
    fifteen = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )
    twenty = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )
    twentyfive = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )
    thirty = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )
    thirtyfive = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )

    def __str__(self):
        return self.name
