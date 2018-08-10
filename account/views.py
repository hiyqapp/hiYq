from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('account/')

def login(request):
	return HttpResponse('account/login')

def logout(request):
	return HttpResponse('account/logout')

def new(request):
	return HttpResponse('account/new')

def delete(request):
	return HttpResponse('account/delete')

