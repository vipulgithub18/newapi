from django.shortcuts import render
from django.http import HttpResponse
from .models import jon
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def home(request):
    return HttpResponse("<h2>This is my First aapp <h2>")

@csrf_exempt
def job(request):

    # Using GET methods Retrive (Show data Web page) with api platform
    # if request.method == "GET":
    #     result = []
    #     jobs=jon.objects.all()
    #     for job in jobs:
    #         data={
    #             "company":job.company,
    #             "descriptions":job.descriptions
    #         }
    #         result.append(data)
    #     return HttpResponse(json.dumps(result))

    #  Render template retrive data 

    if request.method == "GET":
        jobs=jon.objects.all()
        return render(request,'myapp/home.html',{"job":jobs})
    


    # Using post methods isert data added data with api platform

    if request.method == 'POST':
        decod_data = request.body.decode("utf-8")
        python_data = json.loads(decod_data)
        for data in python_data:
            data_comp = data["company"]
            data_disc = data["descriptions"]
            job=jon(company=data_comp, descriptions=data_disc)
            job.save()
        return HttpResponse({"data insert succefully "})
    

    # Using post methods delete data from database  with api platform

    if request.method=="DELETE":
        decod_data = request.body.decode("utf-8")
        python_data = json.loads(decod_data)
        com=python_data["descriptions"]
        job = jon.objects.filter(descriptions=com).delete()
        return HttpResponse({"one again delted succefully : "})



