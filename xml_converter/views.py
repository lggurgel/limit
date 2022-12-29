from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from xml_converter.exceptions import BadFormatFileException
from xml_converter.serializers import CreateXmlToJsonConversionSerializer
from xml_converter.services import convert_to_dict
from xml_converter.validators import validate_file_extension


def upload_page(request):
    if request.method == 'POST':
        # TODO: Convert the submitted XML file into a JSON object and return to the user.
        
        file = request.FILES.get('file')
        
        if not file:
            return JsonResponse({"file": "No file was submitted."}, status=HTTP_400_BAD_REQUEST)
        
        try:
            validate_file_extension(file)
        except ValidationError as err:
            return JsonResponse({"file": str(err)}, status=HTTP_400_BAD_REQUEST)

        try:
            xml_data = convert_to_dict(file)
        except BadFormatFileException as err:
            return JsonResponse({"file": str(err)}, status=HTTP_400_BAD_REQUEST)
        
        return JsonResponse(xml_data, status=HTTP_200_OK)

    return render(request, "upload_page.html")


class CreateXmlToJsonConversionAPI(CreateAPIView):

    serializer_class = CreateXmlToJsonConversionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        try:
            xml_data = convert_to_dict(serializer.validated_data["file"])
        except BadFormatFileException as err:
            return Response({"file": str(err)}, status=HTTP_400_BAD_REQUEST)
        
        return Response(xml_data, status=HTTP_200_OK)
