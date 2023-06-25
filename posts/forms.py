# Django
from django import forms
# model
from .models import Posts
from profile_user.models import ModelDataBeta


class PostsFormCreate(forms.ModelForm):
    """Post model form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        self.fields['media_file'].widget.attrs['class'] = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
        self.fields['media_file'].widget.attrs['accept'] = 'image/png, .jpeg, .jpg, image/gif, .f4v, .MOV,.avi, .mp4, .webm, .mkv, .f4v'
        self.fields['description'].widget.attrs['placeholder'] = 'Escribe una descripción aquí....'

    class Meta:
        """Form settings."""       

        model = Posts
        fields = ('user', 'profile', 'title', 'media_file', 'description')         


class DataBetaForm(forms.ModelForm):
    """Post model Data Beta."""

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for form in self.visible_fields():
                form.field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            self.fields['occupation'].widget.attrs['placeholder'] = 'Comentanos a que te dedicas....'

    class Meta:
        """Form settings."""

        model = ModelDataBeta
        exclude = ['is_valid']
        widgets = {
            'first_name' : forms.TextInput(),
            'last_name' : forms.TextInput(), 
            'document_type' : forms.Select(),
            'document_number' : forms.NumberInput(),
            'email' : forms.EmailInput(),
            'phone_number' : forms.NumberInput(),
            'city' : forms.TextInput(),
            'address' : forms.TextInput(),
            'neighborhood' : forms.TextInput(), 
            'occupation' : forms.Textarea(),
        }


