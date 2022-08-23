
from django.core.validators import BaseValidator, ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class MinLengValidator(BaseValidator):
    message = 'Zagolovok is too short, please enter some more words, Thanks!'
    code = 'to easy'
    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)

@deconstructible
class MaxLengValidator(BaseValidator):
    message = 'Description is too long, could you please do not do it again!'
    code = 'too long'

    def compare(self, a, b):
        return a < b


    def clean(self, x):
        return len(x)

# class CheckForInt(BaseValidator):
#     message = "You have entered integers, please, don't do it again!"
#     code = 'Errrorrr'
#     def compare(self, a, b):
#

#
# def check_for_int(value):
#     if any(i.isdigit() for i in value):
#         raise ValidationError('Errrorrr')

