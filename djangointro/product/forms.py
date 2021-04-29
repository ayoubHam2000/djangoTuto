from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label = '',
        widget=forms.TextInput(
            attrs = {
                "class" : "",
                "placeholder" : "Your title"
            }
        )
    )

    email = forms.EmailField()

    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class" : "new-class-name two",
                "rows" : 20,
                "placeholder" : "description"
            }
        ),

    )

    price = forms.DecimalField(initial=20.99) 
    
    class Meta:
        model = Product
        fields = [
            'title', 
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valide title")
        else:
            return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valide email")
        else:
            return email


#django fields
class RawProductForm(forms.Form):
    title = forms.CharField(
        label = '',
        widget=forms.TextInput(
            attrs = {
                "class" : "",
                "placeholder" : "Your title"
            }
        )
    )
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class" : "new-class-name two",
                "rows" : 20,
                "placeholder" : "description"
            }
        ),

    )
    price = forms.DecimalField(initial=20.99)