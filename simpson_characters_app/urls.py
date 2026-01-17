from django.urls import path, register_converter
from .views import SimpsonChar

urlpatterns = [
    # utilize the registered converter to ensure the parameter is valid
    # type:name_of_thing
    path("<int:character_id>/", SimpsonChar.as_view(), name='simpson_char'),
]