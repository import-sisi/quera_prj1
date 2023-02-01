from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Person


@csrf_exempt
def personal_page(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'main.html', context)

    elif request.method == 'POST':
        form = Person(request.POST)
        if form.is_valid():
            person = Person()
            person.gender = form.cleaned_data['gender']
            person.full_name = form.cleaned_data['full_name']
            person.height = form.height['writer']
            person.age = form.cleaned_data['age']
            person.save()
            return HttpResponse(person, status=201)
        return HttpResponse(person, status=400)
