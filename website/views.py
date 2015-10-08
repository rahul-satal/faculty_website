from django.http import HttpResponse
from django.shortcuts import render
from .models import *

name = "shaligram.prajapat@gmail.com"
def index(request):
	profile = Profile.objects.all()
	achievements = Achievements.objects.all()
	context = {'profile':profile,'achievements':achievements}
	return render(request, 'website/index.html', context)

def ongoing_projects(request):
	ongoing_projects_list = TeachOpc.objects.filter(user_id = name)
	context = {'ongoing_projects_list':ongoing_projects_list}
	return render(request, 'website/ongoing_projects.html', context)

def completed_projects(request):
	completed_projects_list = TeachCpc.objects.filter(user_id = name)
	context = {'completed_projects_list':completed_projects_list}
	return render(request, 'website/completed_projects.html', context)	

def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)	

def lecture(request):
	lecture_list = Myfriend.objects.all()
	context = {'lecture_list':lecture_list}
	return render(request, 'website/lecture.html', context)

def additional_teaching(request):
	additional_list = Myfriend.objects.all()
	context = {'additional_list':additional_list}
	return render(request, 'website/additional_teaching.html', context)

def innovative_teaching(request):
	innovative_list = Myfriend.objects.all()
	context = {'innovative_list':innovative_list}
	return render(request, 'website/innovative_teaching.html', context)			




