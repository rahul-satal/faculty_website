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

                    #Teachings

def lecture(request):
	lecture_list = TeachLstp.objects.filter(user_id = name)
	context = {'lecture_list':lecture_list}
	return render(request, 'website/lecture.html', context)

def additional_teaching(request):
	additional_list = TeachRimc.objects.filter(user_id = name)
	context = {'additional_list':additional_list}
	return render(request, 'website/additional_teaching.html', context)

def innovative_teaching(request):
	innovative_list = TeachTlm.objects.filter(user_id = name)
	context = {'innovative_list':innovative_list}
	return render(request, 'website/innovative_teaching.html', context)		

	             #publications

def published_papers(request):
	published_papers_list = TeachPpij.objects.filter(user_id = name)
	context = {'published_papers_list':published_papers_list}
	return render(request, 'website/published_papers.html', context)

def chapters_published(request):
	chapters_published_list = TeachApb.objects.filter(user_id = name)
	context = {'chapters_published_list':chapters_published_list}
	return render(request, 'website/chapters_published.html', context)

def full_papers(request):
	full_papers_list = TeachFcp.objects.filter(user_id = name)
	context = {'full_papers_list':full_papers_list}
	return render(request, 'website/full_papers.html', context)

def books_published(request):
	books_published_list = TeachBpe.objects.filter(user_id = name)
	context = {'books_published_list':books_published_list}
	return render(request, 'website/books_published.html', context)					




