from django.urls import path 
from sita_app.views import *
from . import views
urlpatterns = [
    path('',home,name="home"),
    path('register', register,name='register'),
    path('administrateur',administrateur,name='administrateur'),
    path('help_desk',help_desk,name='help_desk'),
    path('consulteur',consulteur,name='consulteur'),
    path('creationticket',creationticket,name='creationticket'),
    path('gestioncomposants',gestioncomposants,name='gestioncomposants'),
    path('acceuil',acceuil,name='acceuil'),
    path('gererticket',gererticket,name='gererticket'),
    path('add_site',add_site,name="add_site"),
    path('add_ticket', creationticket, name='add_ticket'),
    path('tickets/update-short', updateShort, name='update_short'),
    path('updateTicket/<str:pk>/',updateTicket,name="updateTicket"),
]
