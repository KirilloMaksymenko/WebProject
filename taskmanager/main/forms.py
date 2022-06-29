from .models import Task, Server_Board, UserProfile
from django.forms import  ModelForm, TextInput, Textarea,EmailInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

###___Local___###
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task","crossed_out","color"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'input-title',
                'placeholder': ' Enter name',
            }),
            "task": Textarea(attrs={
                'class': 'input-notes',
                'placeholder': ' Enter text',
                'col': "8",
                'rows': "8",
            }),
        }

###___Server___###
class ServerForm(ModelForm):
    class Meta:
        model = Server_Board
        fields = ["title", "task","crossed_out","color"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'input-title',
                'placeholder': ' Enter name',
            }),
            "task": Textarea(attrs={
                'class': 'input-notes',
                'placeholder': ' Enter text',
                'col': "8",
                'rows': "8",
            }),
        }

###___Account___###
class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta():
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields["password"].widget.attrs['placeholder'] = "Password"
            self.fields["username"].widget.attrs['placeholder'] = "User name"

class RegisterUserForm(ModelForm):
    class Meta():
        model = User
        fields = ("username", "password","email")
        widgets = {
            "username": TextInput(attrs={

                'class': "form-control",
                'placeholder': "User name"
            }),
            "password": PasswordInput(attrs={

                'class': "form-control",
                'placeholder': "Password"
            }),
            "email": EmailInput(attrs={

                'class': "form-control",
                'placeholder': "Email"
            }),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class EditProfileForm(ModelForm):
    class Meta():
        model = UserProfile
        fields = ("bio",)
        widgets = {
            "bio": Textarea(attrs={
                'class': 'me-3 py-2 text-dark text-decoration-none bio-area',
                'placeholder': ' Enter text',

            }),
        }


