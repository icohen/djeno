from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from . import models

def home(request):
    people = models.Person.objects.order_by('birth__date')
    return render_to_response('geno/home.html', 
                              {'people': people},
                              context_instance=RequestContext(request))