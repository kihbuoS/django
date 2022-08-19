from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AppoinmentCreationForm
from .models import Consultant, Appointment


def person_create_view(request):
    form = AppoinmentCreationForm()
    if request.method == 'POST':
        form = AppoinmentCreationForm()
        if form.is_valid():
            form.save()
            return HttpResponse('Thank ')
    return render(request, 'persons/home.html', {'form': form})


# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})


# AJAX
def load_consultant(request):
    department_id = request.GET.get('department_id')
    consults = Consultant.objects.filter(department_id=department_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'consults': consults})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

