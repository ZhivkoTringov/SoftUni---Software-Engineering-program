from django.core import validators, exceptions
from django.db import models


def validate_isalnum(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15


    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(validators.MinLengthValidator(2),
                    validate_isalnum),
        null=False,
        blank=False,

    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_ALBUM_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other'

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),

    )

    ambum_name = models.CharField(
        max_length=MAX_ALBUM_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name",
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=MUSICS,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',

    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(0.0),
        ),
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)