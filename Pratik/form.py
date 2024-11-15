from django import forms
from .models import EventItem

class MainForm(forms.ModelForm):
    class Meta:
        model = EventItem
        fields = ['Name','Duration','Genre','hostName','Language','imageURL','Venue']