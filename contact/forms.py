from django import forms

class ContactSubmissionForm(forms.Form):
    full_name = forms.CharField(label="To‘liq ism", widget=forms.TextInput(attrs={
        'class': 'w-full border px-4 py-2 rounded-md',
        'placeholder': 'To‘liq ismingiz'
    }))
    age = forms.IntegerField(label="Yosh", widget=forms.NumberInput(attrs={
        'class': 'w-full border px-4 py-2 rounded-md',
        'placeholder': 'Yoshingiz'
    }))
    region = forms.CharField(label="Hudud", widget=forms.TextInput(attrs={
        'class': 'w-full border px-4 py-2 rounded-md',
        'placeholder': 'Qaysi viloyatdan siz?'
    }))
    phone_number = forms.CharField(label="Telefon raqam", widget=forms.TextInput(attrs={
        'class': 'w-full border px-4 py-2 rounded-md',
        'placeholder': '+998 90 123 45 67'
    }))
