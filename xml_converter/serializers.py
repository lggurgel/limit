from rest_framework import serializers

from xml_converter.validators import validate_file_extension

class CreateXmlToJsonConversionSerializer(serializers.Serializer):

    class Meta:
        fields = ["file"]

    file = serializers.FileField(required=True, validators=[validate_file_extension])
