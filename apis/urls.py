from django.urls import path
from .views import *

urlpatterns = [

    # landing page
    path('', landing_page, name="landing"),

    # list all providers
    path('provider/list/', ProviderListCreate.as_view(), name="list_providers"),

    # create provider
    path('provider/create/', create_provider, name="create_provider"),

    # get provider
    path('provider/get/', get_provider, name="edit_provider"),

    # edit provider
    path('provider/edit/', update_provider, name="update_provider"),

    # delete provider
    path('provider/delete/', delete_provider, name="delete_provider"),

    # List / create provider - API
    path('providers/', ProviderListCreate.as_view()),

    # Read / Update / Delete provider by phone_number - API
    path('provider/<phone_number>/', RUDProvider.as_view()),

    # list all service areas
    path('service_area/list/', ServiceAreaListCreate.as_view(), name="list_service_areas"),

    # create service area
    path('service_area/create/', create_area, name="create_area"),

    # update service area
    path('service_area/edit/', update_area, name="update_area"),

    # get area
    path('service_area/get/', get_area, name="get_area"),

    # delete area
    path('service_area/delete/', delete_area, name="delete_area"),

    # list all polygons with lat-lon as same as entered lat-lon
    path('service_area/get/all/', get_all_polygons, name="get_all_polygons"),

    # List / create service area - API
    path('service_areas/', ServiceAreaListCreate.as_view()),

    # Read / Update / Delete provider by phone_number - API 
    path('service_area/<polygon_name>/', RUDServiceArea.as_view()),
]