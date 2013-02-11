from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

from flashcards.models import Set, Card
from flashcards.forms import SetForm, CardForm

def home(request, template_name="index.html"):

def set_list(request, template_name="set_list.html"):

def set_detail(request, set_id, template_name="set_detail.html"):
    set = get_object_or_404

def set_add(request, set_id, template_name="set_detail.html", form=SetForm):
    set = get_object_or_404

def set_edit(request, set_id, template_name="set_edit.html", form=SetForm):
    set = get_object_or_404

def set_delete(request, set_id, template_name="set_delete.html"):
    set = get_object_or_404

def set_progress(request, set_id, template_name="set_progress.html"):
    set = get_object_or_404

def card_detail(request, set_id, card_id, template_name="card_detail.html"):
    card = get_object_or_404

def card_add(request, set_id, template_name="card_add.html", form=CardForm):
    card = get_object_or_404

def card_edit(request, card_id, template_name="card_edit.html", form=CardForm):
    card = get_object_or_404

def card_delete(request, card_id, template_name="card_delete.html"):
    card = get_object_or_404