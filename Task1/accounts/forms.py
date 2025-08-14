# from django import forms
# from django.contrib.auth.models import User
# from .models import Profile

# class SignupForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
#     user_type = forms.ChoiceField(choices=Profile.USER_TYPES)

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']

#     profile_picture = forms.ImageField(required=False)
#     address_line1 = forms.CharField(max_length=255)
#     city = forms.CharField(max_length=50)
#     state = forms.CharField(max_length=50)
#     pincode = forms.CharField(max_length=10)

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")
#         return cleaned_data
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Bootstrap styling
            field.widget.attrs['placeholder'] = field.label  # Optional placeholder

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
