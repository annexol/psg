from django.urls import path
from .views import *


urlpatterns = [
    path("", MicrosoftApps.as_view(), name="apps"),
    path("filter_apps/", FilterMicrosoftApps.as_view(), name="filter_apps"),


]

