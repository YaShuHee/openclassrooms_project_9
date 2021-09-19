from django import forms


class FollowForm(forms.Form):
    query = forms.CharField(max_length=100)


class TicketForm(forms.Form):
    fields = ("title", "description", "image")
