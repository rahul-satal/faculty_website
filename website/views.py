from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
	profile = Profile.objects.all()
	context = {'profile':profile}
	return render(request, 'website/index.html', context)
