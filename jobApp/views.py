from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
def home (request):
    return  HttpResponse('I am from HttpResponse and This is home ')

jobTitle = [
    'Frontend Developer',
    'Backend Developer',
    'Fullstack Developer'
]
jobDescription = [
    'It a very god job for Bigener ',
    'It a very god job for Bigener ',
    'It a very god job for Bigener '

]

def jobDetails(request,id):
    try:
        return_html = f"<h3>{jobTitle[id]}</h3> <p>{jobDescription[id]}</p>"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound('Page Not Found')