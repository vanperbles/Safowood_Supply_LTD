from django import forms
from .models import Item

class ItemCreateForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ('category','name','slug','cost_price','sealing_price','stock','description','image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'slug': forms.TextInput(attrs={'class': 'textinputclass'}),
            'sealing_price': forms.TextInput(attrs={'class': 'textinputclass'}),
            'stock': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),

        }
