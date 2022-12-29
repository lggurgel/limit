from typing import Dict

from rest_framework import serializers

from xml_converter.exceptions import BadFormatFileException
from xml_converter.services import convert_to_dict
from xml_converter.validators import validate_file_extension


class CreateXmlToJsonConversionSerializer(serializers.Serializer):

    class Meta:
        fields = ["file"]

    file = serializers.FileField(validators=[validate_file_extension])
    converted_data = serializers.JSONField(required=False)

    def create(self, validated_data) -> Dict:

        try:
            validated_data["converted_data"] = convert_to_dict(validated_data["file"])
        except BadFormatFileException as err:
            raise serializers.ValidationError(str(err))

        return validated_data
