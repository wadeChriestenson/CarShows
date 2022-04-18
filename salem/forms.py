from django import forms
from django.forms import NumberInput

from salem.widget import TimePickerInput

enthusiastChoices = (
    ("JDM", "JDM"),
    ("UDSM", "USDM"),
    ("EDM", "EDM")
)


class setupMeetInfo(forms.Form):
    latitude = forms.FloatField(
        max_value=999.9999,
        widget=forms.HiddenInput(attrs={'id': 'lat'}))
    longitude = forms.FloatField(
        max_value=99.9999,
        widget=forms.HiddenInput(attrs={'id': 'lng'}))
    host_name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name or car club name'}))
    meet_place = forms.CharField(
        label='Location',
        max_length=100,
        widget=forms.HiddenInput(attrs={'id': 'meetPlace'}))
    meet_address = forms.CharField(
        label='Address',
        max_length=100,
        widget=forms.HiddenInput(attrs={'id': 'meetAddress'}))
    meet_description = forms.CharField(
        label='Description',
        # max_length=100,
        widget=forms.Textarea(attrs={'placeholder': 'Examples: Meet at north end of lot, No-Burnouts, Etc..'}))
    meet_date = forms.DateField(
        label='Meet Date',
        widget=NumberInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=TimePickerInput)
    end_time = forms.TimeField(widget=TimePickerInput)
    enthusiast_type = forms.ChoiceField(
        label='Enthusiast Type',
        choices=enthusiastChoices,
        widget=forms.CheckboxSelectMultiple)
