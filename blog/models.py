from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
 

class Post(models.Model): 
      
    name = models.CharField(blank=False, max_length = 100, verbose_name='Имя')
    email = models.EmailField(blank=False, max_length=100, primary_key=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Номер телефона')
    content = models.TextField(blank=False, verbose_name='Комментарии')
    issued = models.DateTimeField(auto_now=True)
    
   
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        
