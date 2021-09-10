from .forms import *
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def landing_page(request):

    """Landing page."""

    return render(request, 'apis/landing.html')

def create_provider(request):

    """Create a provider."""

    if request.method == "POST":
        form = CreateProviderForm(request.POST)
        if form.is_valid():
            saved = form.save()
            return redirect('landing')
    else:
        form = CreateProviderForm()
    return render(request, 'apis/create_provider.html', {'form' : form})

def get_provider(request):

    """Retrieve provider by phone."""

    provider = None
    if request.GET.get('number'):
        number = request.GET.get('number')
        provider = Provider.objects.filter(phone_number=number).values()
        if not provider:
            raise Http404("No matching provider")
    return render(request,'apis/get_provider.html', {'provider': provider})

def update_provider(request):

    """Update provider by phone."""

    provider = None
    flag = False
    if request.GET.get('number'):
        number = request.GET.get('number')
        try:
            provider = Provider.objects.get(phone_number=number)
        except Provider.DoesNotExist:
            raise Http404("No matching provider")
        flag = True
    if provider and request.method == "POST":
        form = CreateProviderForm(request.POST, instance=provider)
        if form.is_valid():
            saved = form.save()
            return redirect('/api/provider/list/')
    else:
        form = CreateProviderForm(instance=provider)
    return render(request, 'apis/update_provider.html', {'form': form, 'flag' : flag})

def delete_provider(request):

    """Delete provider by phone."""

    provider = None
    if request.GET.get('number'):
        number = request.GET.get('number')
        provider = Provider.objects.filter(phone_number=number)
        if not provider:
            raise Http404("No matching provider")
        provider.delete()
        return redirect('/api/provider/list/')
    return render(request,'apis/delete_provider.html')

class ProviderListCreate(generics.ListCreateAPIView):
    
    """List all providers and Create a provider."""
    
    def get(self, request):
        providers = Provider.objects.values()
        serializer_class = ProviderSerializer(providers, many=True).data   
        return render(request, 'apis/list_providers.html', {'providers' : list(providers)})
    
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class RUDProvider(generics.RetrieveUpdateDestroyAPIView):

    """Retrieve a provider/ Update a provider/ Delete a provider - by phone_numebr (unique)."""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    lookup_field = 'phone_number'

# -----------------------Service Area--------------------------#

def create_area(request):

    """Create a service area."""

    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            provider = request.POST.get('provider')
            provider_object = Provider.objects.filter(name=provider).first()
            form.provider = Service_area.objects.filter(provider = provider_object).first()
            saved = form.save()
            return redirect('landing')
    else:
        form = AreaForm()
    return render(request, 'apis/create_area.html', {'form' : form})

def update_area(request):

    """Update service area by name."""

    area = None
    flag = False
    if request.GET.get('name'):
        poly_name = request.GET.get('name')
        try:
            area = Service_area.objects.get(polygon_name=poly_name)
        except Service_area.DoesNotExist:
            raise Http404("No matching provider")
        flag = True
    if area and request.method == "POST":
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            saved = form.save()
            return redirect('/api/service_area/list/')
    else:
        form = AreaForm(instance=area)
    return render(request, 'apis/update_area.html', {'form': form, 'flag' : flag})

def get_area(request):
    
    """Retrieve area by name."""

    area = None
    provider = None
    if request.GET.get('name'):
        name = request.GET.get('name')
        area = Service_area.objects.filter(polygon_name=name).values()
        provider = Provider.objects.filter(id=area[0]['provider_id']).first()
        if not area:
            raise Http404("No matching service area")
    return render(request,'apis/get_area.html', {'area': area, 'provider' : provider})

def delete_area(request):
    
    """Delete area by name."""

    area = None
    if request.GET.get('name'):
        name = request.GET.get('name')
        area = Service_area.objects.filter(polygon_name=name)
        if not area:
            raise Http404("No matching service area")
        area.delete()
        return redirect('/api/service_area/list/')
    return render(request,'apis/delete_area.html')

def get_all_polygons(request):
    
    """Get all polygons by latitude and longitude"""

    latitude = longitude = poly_list = None
    flag = False
    if request.GET.get('latitude') and request.GET.get('longitude'):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        poly_list = Service_area.objects.filter(latitude=latitude, longitude=longitude)
        flag = True
        if not poly_list:
            flag = True
    return render(request,'apis/get_all_polygons.html', {'list': poly_list, 'flag': flag})

class ServiceAreaListCreate(generics.ListCreateAPIView):
    
    """List all Service Areas and Create a Service Area."""

    def get(self, request):
        service_areas = Service_area.objects.values()  
        return render(request, 'apis/list_areas.html', {'areas' : list(service_areas)})

    queryset = Service_area.objects.all()
    serializer_class = ServiceAreaSerializer

class RUDServiceArea(generics.RetrieveUpdateDestroyAPIView):

    """Retrieve a service area/ Update a service area/ Delete a service area - by polygon_name (unique)."""

    queryset = Service_area.objects.all()
    serializer_class = ServiceAreaSerializer
    lookup_field = 'polygon_name'


'''
    queryset = Service_area.objects.filter(latitude = request.POST.get('latitude'), longitude = request.POST.get('longitude')).all()
'''