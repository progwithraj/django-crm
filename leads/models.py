from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# to create user
# User = get_user_model()

class User(AbstractUser):
    pass


class Leads(models.Model):

    SOURCE = [
        ('YouTube','YouTube'),
        ('LinkedIN','LinkedIN'),
        ('Instagram','Instagram'),
        ('Blog','Blog'),
        ('NewsLetter','NewsLetter'),
        ('Search','Search')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    phone = models.IntegerField()
    called = models.BooleanField(default=False)
    source = models.CharField(max_length=100,choices = SOURCE)
    profile_pic = models.ImageField(blank=True,null=True)
    other_docs = models.FileField(blank=True,null=True)
    agent = models.ForeignKey("Agent",on_delete=models.SET_DEFAULT , default = 'ADMIN')


    class Meta:
        db_table = 'Leads'
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self):
        return self.first_name+" "+self.last_name


class Agent(models.Model):
    """Model definition for Agent."""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    phone = models.IntegerField()
    

    class Meta:
        """Meta definition for Agent."""
        db_table= 'Agents'
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    def __str__(self):
        """Unicode representation of Agent."""
        return self.first_name+" "+self.last_name


