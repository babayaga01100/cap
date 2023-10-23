from django.urls import path

from server.api import RegistrationSF
from .views import DoorView, FanView, InfoView, LedView, RaspberryView, WarningView, WaterView

app_name = 'server'

urlpatterns = [
    # path('', PatentAttorneyListView.as_view(), name='patent-attorney-list'),
    # path('<int:pk>/', PatentAttorneyRetrieveView.as_view(), name='patent-attorney-retrieve')
    path('raspberry', RaspberryView.as_view()),
    path('info', InfoView.as_view()),
    path('led', LedView.as_view()),
    path('water', WaterView.as_view()),
    path('fan', FanView.as_view()),
    path('door', DoorView.as_view()),
    path('warning', WarningView.as_view()),

    path("registration_sf", RegistrationSF.as_view(), name="Registration_SF")

]

