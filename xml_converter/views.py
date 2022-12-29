from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from xml_converter.serializers import CreateXmlToJsonConversionSerializer
from xml_converter.services import convert_to_dict


def upload_page(request):
    if request.method == 'POST':
        # TODO: Convert the submitted XML file into a JSON object and return to the user.
        return JsonResponse({})

    return render(request, "upload_page.html")


class CreateXmlToJsonConversionAPI(CreateAPIView):

    serializer_class = CreateXmlToJsonConversionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        xml_data = convert_to_dict(serializer.validated_data["file"])
        
        return Response(xml_data, status=HTTP_200_OK)
