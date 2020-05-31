from django.shortcuts import render

from catalog.models import User, Measurement

def index(request):
   

    # Generate counts of some of the main objects
    num_measurement= Measurement.objects.all().count()
    
    
        
    # The 'all()' is implied by default.    
    num_user = User.objects.count()
    
    context = {
        'num_measurement': num_measurement,
        'num_user': num_user,
    }

   
    return render(request, 'index.html', context=context)
    
    from django.views import generic

class MeasurementListView(generic.ListView):
    model = Measurement


