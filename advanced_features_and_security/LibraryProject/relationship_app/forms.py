from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """Registration form for the project's custom user model (signs in with email)."""

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'username')
