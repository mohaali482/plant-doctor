from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import SignupForm

UserModel = get_user_model()

class RegisterView(CreateView):
    model = UserModel
    form_class = SignupForm
    template_name = "authentication/register.html"
    success_url = reverse_lazy('auth:login')
