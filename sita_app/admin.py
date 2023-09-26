from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Site)
admin.site.register(Compagnie)
admin.site.register(Zone)
admin.site.register(Terminal)
admin.site.register(Ticket)
admin.site.register(Equipement)