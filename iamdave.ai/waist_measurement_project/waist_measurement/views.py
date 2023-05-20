from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Measurement

def waist_size_Filter(request):
    show_waist_menu = False
    
    if request.method == 'POST':
        height1 = request.POST['height']
        weight1 = request.POST['weight']
        age1 = request.POST['age']
                
        measurements = Measurement.objects.filter(height=height1, weight=weight1, age=age1)
                
        if measurements.exists():
            show_waist_menu = True
            return render(request, 'waist_measurement/index.html', {
                    'measurements': measurements,
                    'show_waist_menu': show_waist_menu,
                    'height': height1,
                    'weight': weight1,
                    'age': age1
                })
        else:
            return redirect('add_details/')
    else:
        if request.method == 'GET':
            height1 = request.GET.get('height')
            weight1 = request.GET.get('weight')
            age1 = request.GET.get('age')
            waist1 = request.GET.get('waist_Select')
            
            if waist1 == "null":
                return redirect('add_details/')
            else:
                measurement = Measurement.objects.create(
                    height=height1 or 1,
                    weight=weight1 or 1,
                    age=age1 or 1,
                    waist=waist1 or 1,
                )
                measurement.save()
        
    return render(request, 'waist_measurement/index.html')


def uplodeData(request):
    if request.method == 'POST':
        height1 = request.POST['height']
        weight1 = request.POST['weight']
        age1 = request.POST['age']
        waist1 = request.POST['waist']        
        
        measurement = Measurement.objects.create(
            height=height1,
            weight=weight1,
            age=age1,
            waist=waist1,
        )
        measurement.save()
        messages.success(request, 'Thank you!')
        return redirect(request.META.get('HTTP_REFERER', '/'))
            
    return render(request, 'waist_measurement/add_details.html')
