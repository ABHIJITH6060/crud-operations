from django import forms

from new_app.models import furniture


class FurnitureForms(forms.ModelForm):
    class Meta:
        model=furniture
        fields= "__all__"



