import os

from xml_converter.exceptions import FileExtensionValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".xml"]
    
    if not ext.lower() in valid_extensions:
        raise FileExtensionValidationError("Unsupported file extension.")
