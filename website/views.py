from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
	profile = Profile.objects.all()
	achievements = Achievements.objects.all()
	context = {'profile':profile,'achievements':achievements}
	return render(request, 'website/index.html', context)



