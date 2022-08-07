from dataclasses import field
from django import forms
#from models import Post  
from phonenumber_field.formfields import PhoneNumberField


# class ContactForm(forms.ModelForm):
   
#     class Meta:    
#         model = Post
#         fields = ('name','email','content')
#         widgets = {
#             'content': forms.Textarea(attrs={'cols': 40, 'rows': 9}),}
    
#     def clean_name(self):
#         data = self.cleaned_data['name']
#         if 'спасибо' not in data.lower():
#             raise forms.ValidationError('Вы обязательно должны нас поблагодарить!')
#         return data 

class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=50, label = 'введите имя')
    email = forms.EmailField(max_length=150, label = 'введите email')
    #phone_number = PhoneNumberField(max_length=150)
    content= forms.CharField(widget=forms.Textarea,max_length=2000, label = 'введите сообщение')
    
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        content = cleaned_data.get('content')
        if not name and not email and not content:
            raise forms.ValidationError('А заполнять кто будет, Си Дзинь Пинь?')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   