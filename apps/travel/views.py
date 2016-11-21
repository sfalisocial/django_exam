from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Travel, Member
from ..logreg.models import User
from datetime import datetime, date

def loggedin(request):
    if 'logged_user' not in request.session:
        messages.error(request, "You must login to view this page!")
        return redirect('/')


def index(request):
    loggedin(request)
    #queries!
    user = User.objects.get(id=request.session['logged_user'])

    created_trips = Travel.objects.filter(creator_id=user)
    joined_trips = Travel.objects.filter(member__member_id=user)
    travel = created_trips | joined_trips

    other_trips = Travel.objects.exclude(id__in=travel)
    #end
    print travel.query
    context = {
        "user" : user,
        "travel" : travel,
        "other_trips" : other_trips
    }
    return render(request,'travel/index.html', context)

def addtravel(request):
    return render(request,'travel/addplan.html')

def viewtravel(request, id):
    travel = Travel.objects.filter(id=id)
    other_members = Member.objects.filter(travel=travel)
    context = {
        "travel" : travel,
        "members" : other_members,
    }
    return render(request,'travel/travel.html', context)

def join(request, id):
    user = User.objects.get(id=request.session['logged_user'])
    travel = Travel.objects.get(id=id)
    Member.objects.create(member=user, travel=travel)
    print 'we made it!'
    return redirect('homepage')

def submit(request):
    if request.method == "POST":
        form_errors = Travel.objects.validation(request.POST)
        print form_errors
        if form_errors:
            for error in form_errors:
                messages.error(request, error)
            return redirect('addtravel')
        else:
            user = User.objects.get(id=request.session['logged_user'])
            travel = Travel.objects.create(destination=request.POST['destination'],description=request.POST['description'],start_date=request.POST['start_date'],end_date=request.POST['end_date'],creator=user)
            messages.success(request, "Successfully added trip!")
            return redirect('homepage')
