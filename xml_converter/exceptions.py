from django.core.exceptions import ValidationError


class BadFormatFileException(Exception):
    pass


class FileExtensionValidationError(ValidationError):
    pass