from xml_converter.views import CreateXmlToJsonConversionAPI

from django.urls import path

urlpatterns = [
    path('converter/convert/', CreateXmlToJsonConversionAPI.as_view())
]