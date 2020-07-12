from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')

def reverse(request):
	get_text = request.GET['usertext']
	number_of_words = len(get_text.split())
	return render(request, 'reverse.html', {'usertext':get_text,'number_of_words':number_of_words})