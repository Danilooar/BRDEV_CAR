from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render

# View de Registro
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redireciona para login após cadastro

    def form_valid(self, form):
        """Salva o usuário e redireciona para a página de login."""
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """Retorna o formulário com erros."""
        return self.render_to_response(self.get_context_data(user_form=form))

    def get(self, request, *args, **kwargs):
        """Renderiza o formulário de registro."""
        return self.render_to_response(self.get_context_data(user_form=self.get_form()))


# View de Login
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')  # Redireciona após login
