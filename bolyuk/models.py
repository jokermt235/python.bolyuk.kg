from django.db import models
#from django.contrib.auth import get_user_model
#User = get_user_model()
# Create your models here.

class Category(models.Model):
    name     = models.CharField(max_length=255)
    position = models.IntegerField()
    creaeted = models.DateField()
    modified = models.DateField()
    #TYPES = ((1 , 'Ходовка'),(2,'Мотор'))
    #types  = models.IntegerField('verbose_name'='Types',choises=TYPES)
    #user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
