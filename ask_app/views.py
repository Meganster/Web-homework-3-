from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from os.path import join

questions = []

for i in range(1, 21):
        questions.append({
            'id': i,
            'title': 'title ' + str(i),
            'text': 'text ' + str(i),
	    'tagOne': str(i),
	    'tagTwo': str(i+1),
        })

answers = []

for i in range(1, 21):
        answers.append({
            'id': i,
            'title': 'title ' + str(i),
            'text': 'text ' + str(i),
        })



def hello(request):
	request.GET
	return request.GET

def first(request):
	now = "Helloworld"
	html = "<html><body> %s </body></html>" %now
	return HttpResponse(html)


def login(request):
	return render(request, 'login.html')

def signup(request):
	return render(request, 'signup.html')

def index(request):
	return render(request, 'index.html', {
	'objects': questions,
	})
		
def tag(request):
	return render(request, 'tag.html')

def question(request):
	return render(request, 'question.html', {
	'objects': answers,
	})

def ask(request):
	return render(request, 'ask.html')




