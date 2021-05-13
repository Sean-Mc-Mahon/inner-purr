from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        #  special dunder or double underscore string called 'all' includes all the fields.
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        #  list comprehension, a shorthand way of creating a for loop that adds items to a list.
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        #  use friendly names for choices instead of using the id.
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ''

#  code taken from CI module @ https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/ba9321f0f1b610e75bf58aee9b0c938bb558f78e/products/forms.py