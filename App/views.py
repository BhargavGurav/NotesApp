from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User 
from .models import *
import datetime
# Create your views here.
def home(request):
    return render(request, 'home.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        if username == '':
            messages.error(request, 'Please fill Email field !')
            return HttpResponseRedirect('/')
        if password == '':
            messages.error(request, 'Please fill password field !')
            return HttpResponseRedirect('/')
        user = User.objects.create_user(username=username, email=username, password=password, is_staff=True)
        user.save()
        messages.success(request, 'Registered successfully.')
        return HttpResponseRedirect('/')


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def loginuser(request):
    if request.method == 'POST':
        usermail = request.POST['useremail']
        password = request.POST['password']

        if usermail == '' or password == '':
            messages.error(request, 'Please fill both fields!')
            return HttpResponseRedirect('/loginuser')
        elif User.objects.filter(username=usermail):
            user = authenticate(username=usermail, password=password)

            if user is not None:
                login(request, user)

                messages.success(request, 'Logged In')
                return HttpResponseRedirect('/dashboard')

            else:
                messages.error(request, 'Wrong data')
                return HttpResponseRedirect('/loginuser')


    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='loginuser')
def dashboard(request):
    notes = Created.objects.filter(user=request.user)
    notes2 = Uploaded.objects.filter(user=request.user)

    subject_set = set([i.subject for i in notes])
    subject_set2 = set([i.subject for i in notes2])
    subjects = subject_set.union(subject_set2)

    return render(request, 'dashboard.html', {'notes' : notes, 'subjects' : subjects, 'notes2' : notes2})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def logoutuser(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/')


def collect_note(request):
    if request.method=='POST':
        user = request.user
        subject = request.POST['subject']
        note = request.POST['note']
        created = datetime.datetime.now()

        notes = Created(user=user, subject=subject, note=note, created_on=created)
        notes.save()
        messages.success(request, 'Note Saved !')
        return HttpResponseRedirect('/dashboard')

    notes = Created.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'notes' : notes})
    
def upload_note(request):
    if request.method=='POST' or request.method=='FILES':
        user = request.user
        subject = request.POST['subject']
        note = request.FILES['note']
        created = datetime.datetime.now()

        notes = Uploaded(user=user, subject=subject, note_file=note, created_on=created)
        notes.save()
        messages.success(request, 'Note Saved !')
        return HttpResponseRedirect('/dashboard')

    notes = Uploaded.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'notes' : notes})
