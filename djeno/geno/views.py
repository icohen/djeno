from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from . import models

class ProtectedView(TemplateView):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


class HomeView(ProtectedView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['people'] = models.Person.objects.order_by('birth__date')
        return context
