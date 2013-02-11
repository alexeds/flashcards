from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

from flashcards.models import Set, Card

def home(request):

def set_list(request):

def set_detail(request, set_id):
    set = get_object_or_404

def set_add(request, set_id):
    set = get_object_or_404

def set_edit(request, set_id):
    set = get_object_or_404

def set_delete(request, set_id):
    set = get_object_or_404

def set_progress(request, set_id):
    set = get_object_or_404

def card_detail(request, set_id, card_id):
    card = get_object_or_404

def card_add(request, set_id):
    card = get_object_or_404

def card_edit(request, card_id):
    card = get_object_or_404

def card_delete(request, card_id):
    card = get_object_or_404