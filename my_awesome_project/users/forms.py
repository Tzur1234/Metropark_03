from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from my_awesome_project.fines.models import CardIDField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

User = get_user_model()

# admim
#------------------------------------------------------------------------------------------------------------
class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


# class UserAdminChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email')




# class UserAdminCreationForm(UserCreationForm):
#     """
#     Form for User Creation in the Admin Area.
#     To change user signup, see UserSignupForm and UserSocialSignupForm.
#     """

#     class Meta:
#         model = User
#         error_messages = {
#             "username": {"unique": _("This username has already been taken.")},
#         }
#         fields = ('username', 'email', 'israeli_id')




# user-register-form
# ------------------------------------------------------------------------------------------------------------------------
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'israeli_id')


# class UserSignupForm(SignupForm):

#     """
#     Form that will be rendered on a user sign up section/screen.
#     Default fields will be added automatically.
#     Check UserSocialSignupForm for accounts created from social.
#     """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
