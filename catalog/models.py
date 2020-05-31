from django.db import models

class User(models.Model):
    user_login = models.CharField(max_length=20, help_text='Введите логин')
    user_name = models.CharField(max_length=20, help_text='Введите имя')
    gender = models.CharField(max_length=10, help_text='Введите пол')
    date_of_birth = models.DateField(null=True, blank=True)
    
class Meta:
    ordering = ['user_login', 'user_name']

def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

def __str__(self):
        return f'{self.user_name}, {self.user_login}'

class Measurement(models.Model):
    systolic=models.IntegerField(null=False, blank=False)
    dyastolic=models.IntegerField(null=False, blank=False)
    pulse=models.IntegerField(null=False, blank=False)

user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

def __str__(self):
        return self.title
    
def get_absolute_url(self):
        return reverse('measurement-detail', args=[str(self.id)])



 
