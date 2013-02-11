from django.contrib import admin

from flashcards.models import Card, Set
from flashcards.forms import CardForm, SetForm


class SetAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'creator']
    list_filter = ['level']
    search_fields = ['title', 'level', 'creator']
    fieldsets = (
        ('Set Information', {
            'fields': ('title',
                'level',
                )
            }),
    )
    form = SetForm
    ordering = ['-create_dt']
    
class CardAdmin(admin.ModelAdmin):
    list_display = ['question', 'known', 'set', 'creator']
    list_filter = ['known', 'set', 'creator']
    search_fields = ['question', 'known', 'set', 'creator']
    fieldsets = (
        ('Card Information', {
            'fields': ('question',
                'answer',
                'known'
                'set',
                )
            }),
    )
    form = CardForm
    ordering = ['-create_dt']

admin.site.register(Set, SetAdmin)
admin.site.register(Card, CardAdmin)