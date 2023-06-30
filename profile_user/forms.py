#django
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import User, ProfileUser


class CustomPhoneNumberPrefixWidget(PhoneNumberPrefixWidget):
   
    def subwidgets(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        return context['widget']['subwidgets']
    

class CreateSigupForm(forms.ModelForm):
    """ form model update profile. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
    
    class Meta:

        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {            
            'password' : forms.PasswordInput(),
        }

    def clean(self):
        """Verify password confirmation match."""

        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError({'password': forms.ValidationError('Passwords do not match.')})
        return data
    
    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email is already in use.')
        return email     

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        
        username = data['username'] 
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        user = User.objects.create_user(
            username=username, 
            password=password, 
            first_name=first_name, 
            last_name=last_name, 
            email=email
            )
        profile = ProfileUser(user=user)
        profile.save()    


class UpdateFormProfileUser(forms.ModelForm):
    """ form model update profile. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        self.fields['picture'].widget.attrs['class'] = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
        self.fields['biography'].widget.attrs['placeholder'] = 'Escribe una descripción aquí....'

    class Meta:

        model = ProfileUser
        fields = ('picture', 'phone_number', 'address', 'website', 'biography', 'document_type', 'document_number')
        widgets = {            
            'picture' : forms.FileInput(),
            'document_type' : forms.Select(),
            'document_number' : forms.NumberInput(),
            'phone_number' : CustomPhoneNumberPrefixWidget(initial='CO'),
            'address' : forms.TextInput(),
            'website' : forms.TextInput(),
            'biography' : forms.Textarea(),
        }

    def clean_document_number(self):
        """Document_number must be unique."""
        
        id_profile = self.data['id_profile']
        document_number = self.cleaned_data['document_number']
        document_number_taken = ProfileUser.objects.filter(document_number=document_number).exclude(id=id_profile).exists()
        if document_number_taken:
            raise forms.ValidationError('Document number is already in use.')
        return document_number    

    def clean_phone_number(self):
        """phone_number must be unique."""
        
        id_profile = self.data['id_profile']
        phone_number = self.cleaned_data['phone_number']
        phone_number_taken = ProfileUser.objects.filter(phone_number=phone_number).exclude(id=id_profile).exists()
        if phone_number_taken:
            raise forms.ValidationError('Phone number is already in use.')
        return phone_number 


