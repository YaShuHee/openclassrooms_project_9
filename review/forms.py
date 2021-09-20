from django.forms import ModelForm
from django import forms
from .models import Ticket


class FollowForm(forms.Form):
    query = forms.CharField(max_length=100)


class NewTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        widget = {
            "title": forms.TextInput(),
            "description": forms.Textarea(),
            "image": forms.ImageField(),
        }


class NewTicketAndReviewForm(forms.Form):
    title = forms.CharField(max_length=128, widget=forms.TextInput)
    description = forms.CharField(max_length=2048, widget=forms.Textarea)
    image = forms.ImageField()
    headline = forms.CharField(max_length=128, widget=forms.TextInput)
    rating = forms.IntegerField(min_value=0, max_value=5, widget=forms.RadioSelect(choices=(
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )))
    body = forms.CharField(max_length=8192, widget=forms.Textarea)


class NewReviewForm(forms.Form):
    headline = forms.CharField(max_length=128, widget=forms.TextInput)
    rating = forms.IntegerField(min_value=0, max_value=5, widget=forms.RadioSelect(choices=(
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )))
    body = forms.CharField(max_length=8192, widget=forms.Textarea)


class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["description", "image"]
        widget = {
            "description": forms.Textarea(),
            "image": forms.ImageField(),
        }


class UpdateReviewForm(forms.Form):
    headline = forms.CharField(max_length=128, widget=forms.TextInput)
    rating = forms.IntegerField(min_value=0, max_value=5, widget=forms.RadioSelect(choices=(
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )))
    body = forms.CharField(max_length=8192, widget=forms.Textarea)