from django.contrib import admin
from .models import EventItem 
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['Name','Duration','Genre','hostName','Language','Venue']

admin.site.register(EventItem,EventAdmin)