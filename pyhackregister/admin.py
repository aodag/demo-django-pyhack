from django.contrib import admin
from .models import PyhackEvent


# Register your models here.
class PyhackEventAdmin(admin.ModelAdmin):
    pass

admin.site.register(PyhackEvent, PyhackEventAdmin)
