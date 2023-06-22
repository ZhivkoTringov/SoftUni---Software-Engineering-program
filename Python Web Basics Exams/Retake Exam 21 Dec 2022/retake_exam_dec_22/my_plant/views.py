from django.shortcuts import render, redirect

from retake_exam_dec_22.my_plant.forms import CreateProfileForm, CreatePlantForm, EditPlantForm, DeletePlantForm, \
    EditProfileForm, DeleteProfileForm
from retake_exam_dec_22.my_plant.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    if get_profile() is not None:
        return redirect('index')
    context = {
        'hide_nav': True
    }
    return render(request, 'core/home-page.html', context,)


def catalogue(request):
    context = {
        'plants': Plant.objects.all(),
    }

    return render(request, 'core/catalogue.html', context, )


def create_plant(request):
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'plant/create-plant.html', context, )


def details_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant,

    }
    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'plant/delete-plant.html', context)


def create_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'hide_nav': True,

    }
    return render(request, 'profile/create-profile.html', context, )


def details_profile(request):
    profile = Profile.objects.get()
    plant_count = Plant.objects.count()

    context = {
        'profile': profile,
        'plant_count': plant_count,
    }
    return render(request, 'profile/profile-details.html', context, )


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')


    context = {
        'form': form,
        'profile': profile,

    }
    return render(request, 'profile/edit-profile.html', context,)


def delete_profile(request):

    profile = Profile.objects.get()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)
