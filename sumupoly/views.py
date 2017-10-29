from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib import messages

import pickle
import time
import json
import os

from sumup_oauthsession import OAuth2Session

HOST = settings.SUMUPOLY_SUMUP_API_HOST
CLIENT_ID = settings.SUMUPOLY_SUMUP_CLIENT_ID
CLIENT_SECRET = settings.SUMUPOLY_SUMUP_CLIENT_SECRET
REDIRECT_URI = 'http://localhost:16161/oauth-callback'

sumup = OAuth2Session(HOST, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

def home(request):
    return render(request, 'sumupoly/index.html', {})

def authorize(request):
    return redirect(sumup.authorization_url())

def callback(request):
    try: 
        code = request.GET.get('code', '')
        state = request.GET.get('state', '')
        is_authorized = sumup.authorize(code, state)
    except ValueError as e:
        return HttpResponse(e)

    if is_authorized:
        redirect_to = request.COOKIES['sumup_next']
        return redirect(reverse(redirect_to))
    else:
        return HttpResponse("Error: Unable to obtain SumUp - OAuth authorization")

def nothing(request):
    if not sumup.is_authorized():
        response = redirect(reverse('authorize'))
        response.set_cookie('sumup_next', 'nothing', max_age=1000)
        return response

    r = sumup.get('v0.1/me')
    return HttpResponse(json.dumps(r.json(), indent=4), content_type='application/json')

def transactions(request):
    if not sumup.is_authorized():
        response = redirect(reverse('authorize'))
        response.set_cookie('sumup_next', 'transactions', max_age=1000)
        return response

    params = {
        'limit': 100,
        'order': 'descending',
        'statuses[]': 'SUCCESSFUL',
        'types[]': 'PAYMENT', 
        # 'changes_since': '2017-10-23T08:23:00.000Z'
    }

    r = sumup.get('v0.1/me/transactions/history', params=params)

    return HttpResponse(json.dumps(r.json(), indent=4), content_type='application/json')

