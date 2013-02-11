from datetime import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from flashcards.models import Set, Card


class SetForm(TendenciBaseForm):

    class Meta:
        model = Set
        fields = (
            'title',
            'level',
        )

class CardForm(TendenciBaseForm):

    class Meta:
        model = Card
        fields = (
            'question',
            'answer',
            'set',
        )