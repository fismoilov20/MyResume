from django import forms
from .models import ContactProfile



class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={                  # sets HTML attributes
            'placeholder': 'Your name..',
            'class': 'form-control',
        })
    )
    email = forms.EmailField(max_length=200, required=True,
        widget=forms.EmailInput(attrs={                 # sets HTML attributes
            'placeholder': 'Your email..',
            'class': 'form-control',
        })
    )
    message = forms.CharField(max_length=1000, required=True,
        widget=forms.Textarea(attrs={                   # sets HTML attributes
            'placeholder': 'Write something..',
            'rows': 6,
            'class': 'form-control',
        })
    )

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message')