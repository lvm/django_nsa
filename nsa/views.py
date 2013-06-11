from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from forms import NSAForm


def nsa_member_only(function):
    def wrapper(request, *args, **kw):
        if not request.session.get('nsa_member', False):
            return render(request, "nsa/logon.html", {'form': NSAForm})
        return function(request, *args, **kw)
    return wrapper


def logon(request):
    f = NSAForm(request.POST)
    if f.is_valid():
        request.session['nsa_member'] = True
    else:
        return render(request, "nsa/logon.html", {'form': f})
    return HttpResponseRedirect(reverse('nsa_index'))


def logoff(request):
    request.session['nsa_member'] = False
    request.session['accordance'] = False
    return HttpResponseRedirect(reverse('nsa_index'))


@nsa_member_only
def index(request):
    if not request.session.get('accordance', False):
        return HttpResponseRedirect(reverse('nsa_warrant'))
    data = {'nsa_member': request.session.get('nsa_member')}
    data['users'] = User.objects.all()
    return render(request, "nsa/index.html", data)


@nsa_member_only
def warrant(request):
    data = {'nsa_member': request.session.get('nsa_member')}
    if 'yes' in request.GET.keys():
        request.session['accordance'] = True
        return HttpResponseRedirect(reverse('nsa_index'))
    return render(request, "nsa/warrant.html", data)


@nsa_member_only
def users(request, user_id=None):
    data = {'nsa_member': request.session.get('nsa_member')}
    if not user_id:
        return HttpResponseRedirect(reverse('nsa_index'))
    data['user'] = User.objects.get(id=user_id)
    data['user_fields'] = [(f, f.value_from_object(data['user']))
                           for f in data['user']._meta.fields
                               if f.name not in ['id', 'password']]
    return render(request, "nsa/users.html", data)


@nsa_member_only
def users_data(request, user_id=None, data_id=None):
    if not user_id:
        return HttpResponseRedirect(reverse('nsa_index'))
    data = {'nsa_member': request.session.get('nsa_member')}
    data['user'] = User.objects.get(id=user_id)
    if data_id:
        data['secret'] = data['user'].logentry_set.get(id=data_id)
    data['secrets'] = data['user'].logentry_set.all()
    return render(request, "nsa/users_data.html", data)
