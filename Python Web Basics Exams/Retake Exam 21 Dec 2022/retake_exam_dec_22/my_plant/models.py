from django.core import validators, exceptions
from django.db import models


def validate_startswith_capital_letter(value):
    if not value[0].isupper():
        raise exceptions.ValidationError('Your name must start with a capital letter!')


def validate_letters_only(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 10
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_FIRSTNAME = 20

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_USERNAME),),
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRSTNAME,
        validators=(validate_startswith_capital_letter,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_FIRSTNAME,
        validators=(validate_startswith_capital_letter,),
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    MAX_LENGTH_TYPES = 14
    MAX_LENGTH_NAME = 20
    MIN_LENGTH_NAME = 2

    OUT_DOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    TYPES_OF_PLANTS = (
        (OUT_DOOR_PLANTS, OUT_DOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    plant_type = models.CharField(
        max_length=MAX_LENGTH_TYPES,
        choices=TYPES_OF_PLANTS,
        null=False,
        blank=False,
        verbose_name='Type'
    )

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_NAME),
                    validate_letters_only,
                    ),
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    description = models.TextField(

        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)
