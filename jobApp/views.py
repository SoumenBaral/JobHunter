from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from . import models 
def home (request):
    temp = tempClass
    is_authentication = False
    # context = {'data':jobTitle,'temp': temp,'is_authentication': is_authentication}
    context = models.jobPost.objects.all()
    return  render(request,'hello.html',{'context':context})


class tempClass :
    x = 6

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
        job = models.jobPost.objects.get(id=id)
        
        return render(request,'jobdetails.html',{'job':job})
    except:
        return HttpResponseNotFound('Page Not Found')