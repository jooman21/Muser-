
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def crossdock_file_extension(value):
    allowed_extensions = ['xlsx', 'xls', 'pdf']
    extension_validator = FileExtensionValidator(allowed_extensions)

    try:
        extension_validator(value)
    except ValidationError as e:
        raise ValidationError('Only Excel (xlsx, xls), and PDF files are allowed.')


def file_size_1_10(value):
    filesize = value.size
   #  print(filesize)
   #  print(value.name)

    if filesize > 10000000:
        raise ValidationError('Maximum file size is 10Mb.')
    elif filesize < 1000000:
     raise ValidationError('Minimum file size is 1Mb.')