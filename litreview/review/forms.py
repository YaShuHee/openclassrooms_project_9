from django import forms


class FollowForm(forms.Form):
    query = forms.CharField(max_length=100)
