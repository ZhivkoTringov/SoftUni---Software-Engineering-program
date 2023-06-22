
from django.urls import path, include

from retake_exam_dec_22.my_plant.views import index, catalogue, details_profile, create_profile, edit_profile, \
    delete_profile, create_plant, details_plant, edit_plant, delete_plant

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('details/', details_profile, name='details profile'),
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>', details_plant, name='details plant'),
    path('edit/<int:pk>', edit_plant, name='edit plant'),
    path('delete/<int:pk>', delete_plant, name='delete plant'),
)
