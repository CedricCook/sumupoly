from django.conf.urls import url, patterns
from django.conf import settings

from . import views

app_name = 'sumupoly'

CALLBACK_REGEX = '^' + settings.SUMUPOLY_SUMUP_REDIRECT_URI + '$'

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    # url(CALLBACK_REGEX, views.callback, name='oauth_callback'),
    url(r'^authorize$', views.authorize, name='authorize'),
    url(r'^transactions$', views.transactions, name='transactions'),
    url(r'^nothing$', views.nothing, name='nothing'),
)