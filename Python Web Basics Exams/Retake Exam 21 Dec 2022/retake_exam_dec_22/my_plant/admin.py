from django.contrib import admin

from retake_exam_dec_22.my_plant.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
