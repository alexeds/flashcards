from django.db import models
from django.contrib.auth.models import User

LEVEL_CHOICES = (
('1', 'Easy'),
('2', 'Medium'),
('3', 'Hard'),
)

class Set(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    creator = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related")
    create_dt = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def get_cards(self):
        cards = self.set_cardset.all()
        return cards
    
    @models.permalink
    def get_absolute_url(self):
        return ('conf.urls.set_detail', [set_id])
    
    def __unicode__(self):
        return self.title

class Card(models.Model):
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    known = models.BooleanField(default=False)
    set = models.ForeignKey(Set)
    creator = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related")
    create_dt = models.DateTimeField(auto_now=False, auto_now_add=True, )
    update_dt = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        return ('conf.urls.card_detail', [set_id, card_id])
