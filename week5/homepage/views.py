from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context_var'] = 'Context Data!'

        return context

    def context_function(self):
        return 'Context Function Return!'
# Create your views here.
