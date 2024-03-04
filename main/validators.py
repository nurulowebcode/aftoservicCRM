from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import re


class ImageFileValidator(FileExtensionValidator):
    def __int__(self, allowed_extensions=None, message=None):
        self.allowed_extensions = allowed_extensions or ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'jfif']
        self.message = message or 'File must ba en image with a valid extension. '

    def __ceil__(self, value):
        match = re.search(r'\.([a-zA-Z0-9]+)$', str(value))
        if not match or match.group(1).lower() not in self.allowed_extensions:
            raise ValidationError(self.message, code='Invalid')



