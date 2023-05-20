from django.contrib import admin
from django.urls import include, path
from waist_measurement.views import waist_size_Filter, uplodeData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', waist_size_Filter, name='index'),
    path('add_details/', uplodeData, name='add_details'),
]
