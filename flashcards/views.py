from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

from flashcards.models import Set, Card
from flashcards.forms import SetForm, CardForm

def home(request, template_name="index.html"):
    return render_to_response(template_name, context_instance=RequestContext(request))

def set_list(request, template_name="set_list.html"):
    sets = Set.objects.all()
    
    return render_to_response(template_name, {'sets': sets}, context_instance=RequestContext(request))

def set_detail(request, set_id, template_name="set_detail.html"):
    set = get_object_or_404
    cards = Card.objects.filter(set=set)
    
    return render_to_response(template_name, {'set': set, 'cards': cards}, context_instance=RequestContext(request))

def set_add(request, set_id, template_name="set_detail.html", form=SetForm):
    
    return render_to_response(template_name, context_instance=RequestContext(request))

def set_edit(request, set_id, template_name="set_edit.html", form=SetForm):
    set = get_object_or_404
    
    return render_to_response(template_name, {'set': set}, context_instance=RequestContext(request))

def set_delete(request, set_id, template_name="set_delete.html"):
    set = get_object_or_404
    
    return render_to_response(template_name, {'set': set}, context_instance=RequestContext(request))

def set_progress(request, set_id, template_name="set_progress.html"):
    set = get_object_or_404
    
    return render_to_response(template_name, {'set': set}, context_instance=RequestContext(request))

def card_detail(request, set_id, card_id, template_name="card_detail.html"):
    card = get_object_or_404
    
    return render_to_response(template_name, {'card': card}, context_instance=RequestContext(request))

def card_add(request, set_id, template_name="card_add.html", form=CardForm):

    return render_to_response(template_name, context_instance=RequestContext(request))

def card_edit(request, card_id, template_name="card_edit.html", form=CardForm):
    card = get_object_or_404
    
    return render_to_response(template_name, {'card': card}, context_instance=RequestContext(request))

def card_delete(request, card_id, template_name="card_delete.html"):
    card = get_object_or_404
    
    return render_to_response(template_name, {'card': card}, context_instance=RequestContext(request))