from django.conf.urls import patterns, include, url

 from django.contrib import admin
 admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'flashcards.views.home', name='home'),
     
    #sets
    url(r'^sets/$' 'flashcards.views.sets_list', name="sets_list"),
    url(r'^sets/(?P<set_id>\d+)/$' 'flashcards.views.set_detail', name="set_detail"),
    url(r'^sets/add/$' 'flashcards.views.set_add', name="set_add"),
    url(r'^sets/(?P<set_id>\d+)/edit/$' 'flashcards.views.set_edit', name="set_edit"),
    url(r'^sets/(?P<set_id>\d+)/delete/$' 'flashcards.views.set_delete', name="set_delete"),
    url(r'^sets/(?P<set_id>\d+)/progress/$' 'flashcards.views.set_progress', name="set_progress"),
     
    #cards
    url(r'^sets/(?P<set_id>\d+)/(?P<card_id>\d+)/$' 'flashcards.views.card_detail', name="card_detail"),    
    url(r'^sets/(?P<set_id>\d+)/add/$' 'flashcards.views.card_add', name="card_add"),
    url(r'^cards/(?P<set_id>\d+)/edit/$' 'flashcards.views.card_edit', name="card_edit"),
    url(r'^cards/(?P<set_id>\d+)/delete/$' 'flashcards.views.card_delete', name="card_delete"),

    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
