from django.shortcuts import render

from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from datetime import datetime
from .models import Link
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from interface import urls
from django.contrib import messages
from .forms import NewMeetingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.
"""
def newMeeting(request):
    user = request.user
    form = NewMeetingForm()

    if request.method =='POST':
        
        form = NewMeetingForm(request.POST)
        form['user']=User.objects.get(pk=user.id)
        if form.is_valid():
            
            form.save()
            return redirect('home')
        else:
            return redirect('newmeeting')
    context = {'form': form}
    return render(request,'newmeeting.html',context)

"""

@login_required(login_url='login')
def newmeetinglink(request):
    return render(request,'newmeeting.html',{})


@login_required(login_url='login')
def deleteMeet(request,id):

    Link.objects.filter(id =id).delete()
    return redirect('home')







@login_required(login_url='login')
def newMeeting(request):
    if request.method=='POST':
        user_obj = User.objects.get(id = request.user.id)
        meeting_name = request.POST.get('meeting_name')
        meeting_link = request.POST.get('meeting_link')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        monday = False
        tuesday = False
        wednesday = False
        thursday= False
        friday= False
        saturday= False
        sunday= False
        if request.POST.get('monday')=='on':
            monday = True
        if request.POST.get('tuesday')=='on':
            tuesday = True
        if request.POST.get('wednesday')=='on':
            wednesday = True
        if request.POST.get('thursday')=='on':
            thursday = True
        if request.POST.get('friday')=='on':
            friday = True
        if request.POST.get('saturday')=='on':
            saturday = True
        if request.POST.get('sunday')=='on':
            sunday = True        

        Link.objects.create(
            user = user_obj,
            meeting_name = meeting_name,
            meeting_link = meeting_link,
            start_time =start_time,
            end_time = end_time,
            monday =monday,
            tuesday = tuesday,
            wednesday = wednesday,
            thursday =thursday,
            friday =friday,
            saturday =saturday,
            sunday =sunday
        )

        return redirect('home')


  


@login_required(login_url='login')
def current_meeting(request):
    current_time = datetime.now()

    current_hour = current_time.hour #3:00 pm -> 15
    current_min = current_time.minute #3:00 pm -> 0

    meeting_list = list(Link.objects.filter(user=request.user))

    current_meeting = None

    def time_in_mins(hr, min):
        return hr * 60 + min

    for meeting in meeting_list:
        start_time_hour = meeting.start_time.hour
        start_time_min = meeting.start_time.minute

        end_time_hour = meeting.end_time.hour
        end_time_min = meeting.end_time.minute

        day_list = []

        if meeting.monday == True:
            day_list.append('Monday')
        if meeting.tuesday == True:
            day_list.append('Tuesday')
        if meeting.wednesday == True:
            day_list.append('Wednesday')
        if meeting.thursday == True:
            day_list.append('Thursday')
        if meeting.friday == True:
            day_list.append('Friday')
        if meeting.saturday == True:
            day_list.append('Saturday')
        if meeting.sunday == True:
            day_list.append('Sunday')
        

        if ((day_list.count(current_time.strftime('%A')) == 0)
            or (time_in_mins(start_time_hour, start_time_min) - 6) > time_in_mins(current_hour, current_min)
                or (time_in_mins(end_time_hour, end_time_min)) < time_in_mins(current_hour, current_min)):

            continue

        current_meeting = meeting

    if current_meeting == None:
        return render(request, 'nomeetings.html', {'alls':meeting_list})
    else:

        send_mail(
        "MyMeetWebapp",
        str(User.username)+str(current_meeting)+"       Username:"+str(request.user)+"      Meeting List is Here:"+str(meeting_list),
        'mymeetwebapp.com',
        ['ravibhai7812@gmail.com'],
        fail_silently=False,
        )


        return render(request, 'linktoclick.html', { 'obj': current_meeting,'alls':meeting_list})


def registerPage(request):
    if request.user.is_authenticated:
	    return redirect('home')
    else:
        form = UserCreationForm()

        if request.method=='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request,'register.html',context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
