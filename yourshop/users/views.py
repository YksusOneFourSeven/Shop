from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from .forms import CreationForm
from .models import Account
from .forms import AccountForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import JsonResponse



class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('store:home')
    template_name = 'users/signup.html'

class AccountView(LoginRequiredMixin, FormView):
    template_name = 'users/account.html'
    form_class = AccountForm
    success_url = reverse_lazy('users:account')  # Укажите URL успешного обновления

    def form_valid(self, form):
        account = form.save(commit=False)
        account.user = self.request.user
        account.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Обработка невалидной формы
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['all'] = Account.objects.get(user=self.request.user)
        account = Account.objects.get(user=self.request.user)
        account_data = model_to_dict(account)
        account_data = {key: value for key, value in account_data.items() if key not in ['id', 'user']}
        context['user_account_data'] = account_data
        if self.request.method == 'POST':
            form = self.form_class(self.request.POST, instance=account)
            if form.is_valid():
                form.save()
        else:
            form = self.form_class(instance=account)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        account = Account.objects.get(user=self.request.user)
        form = self.form_class(request.POST, instance=account)
        if form.is_valid():
            form.save()
            response_data = {
                'status': 'success',
                'message': 'Account updated successfully'
            }
        else:
            response_data = {
                'status': 'error',
                'message': 'Error updating account',
                'errors': form.errors
            }
        return JsonResponse(response_data)

