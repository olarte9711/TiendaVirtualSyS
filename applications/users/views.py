from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http  import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView,
    ListView
)
from django.views.generic.edit import (
    FormView
)

from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm

from .models import User

from .functions import code_generator
# Create your views here.

class UserRegisterView(FormView):

    
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        #generamos el codigo
        codigo = code_generator()

        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            full_name= str(nombres)+' '+str(apellidos),
            genero=form.cleaned_data['genero'],
            codregistro= codigo
        )
        #enviar el codigo al email del user

        asunto = 'Confirmacion de email'
        mensaje = 'codigo de verificación: '+ codigo
        email_remitente = 'olarte9711@gmail.com'

        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        #redirigir
        return HttpResponseRedirect(
            reverse(
                'users_app:user-verification',
                kwargs={'pk':usuario.id}
            )
        )        

        return super(UserRegisterView,self).form_valid(form)

class LoginUser(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('estampa_app:index')


    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form) 

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )

class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = "users/update.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1'],
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
       
        return super(UpdatePasswordView, self).form_valid(form)

class CodeVerificationView(FormView):
    template_name = "users/verification.html"
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update(
            {
                'pk': self.kwargs['pk']
            }
        )
        return kwargs

    def form_valid(self, form):

        User.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_active=True
        )
        return super(CodeVerificationView, self).form_valid(form)

class UserListView(ListView):
    template_name = "users/lista.html"
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()

    
