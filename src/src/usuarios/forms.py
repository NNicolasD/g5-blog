# from .models import Usuario
# from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()
# class RegistroUsuarioForm(UserCreationForm):

#     class Meta:
#         model  = Usuario
#         fields = ['username','password1','password2']
#         help_text = {k:"" for k in fields}

#     @transaction.atomic
#     def save(self):
#         user              = super().save(commit=False)
#         user.is_superuser = False
#         user.is_staff     = False
#         user.save()
#         return user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
