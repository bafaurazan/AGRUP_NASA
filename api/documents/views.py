"""Defining views for documents"""

from http import HTTPStatus
from django.http import HttpRequest

from ninja import Router
from ninja.pagination import LimitOffsetPagination, paginate


from documents.schemas import SensorIn
from documents.controllers import (
    dane_gleb,
    dane_gleb_wykres,
    dane_gleb_json,
    sensor_json_R,
)


router = Router(tags=["Documents"])

@router.get("/sensor_R2/")
def sensor_R_view(request):
    return sensor_json_R(request)

@router.get("/sendjson2/{id}")
def json_view(request,id: int):
    return dane_gleb_json(request,id)

# Echo message from R
@router.get("/document/tak/")
def echo_view(request):
    return dane_gleb(request)

# Plot histogram from R
@router.get("/document/tak2/")
def plot_view(request):
    return dane_gleb_wykres(request)



