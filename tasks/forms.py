from django import forms

class RawTaskForm(forms.Form):
    title = forms.CharField(required=True, widget=forms. TextInput({ "placeholder": "Title"}))
    desc = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "rows" : 10,
            "cols" : 40,
            "placeholder" : "Description"
        }
    ))
    file = forms.FileField(required=False)