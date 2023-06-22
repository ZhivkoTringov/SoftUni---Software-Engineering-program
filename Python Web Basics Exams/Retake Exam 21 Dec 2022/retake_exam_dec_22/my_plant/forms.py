from django import forms

from retake_exam_dec_22.my_plant.models import Profile, Plant

class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name',)

class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
        def __init__(self, *args, **kwargs):
            super(EditProfileForm, self).__init__(*args, **kwargs)

        class Meta(BaseProfileForm.Meta):
            fields = BaseProfileForm.Meta.fields + ('profile_picture',)


class DeleteProfileForm(EditProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True
