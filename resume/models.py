from django.db import models
from datetime import datetime

class User(models.Model):
    nome_user = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    address = models.TextField()
    phone =  models.CharField(max_length= 100)
    about_description = models.TextField() 
    interest_description = models.TextField()

    #def __str__(self):
     #   return f'{self.nome_user} {self.email}{self.address}{self.phone}{self.about_description}{self.interest_description}'


class Experience(models.Model):
    id_user = models.ForeignKey(User,models.CASCADE,related_name='experiences')
    job_name = models.CharField(max_length=200)
    organization =  models.CharField(max_length=200)
    period = models.CharField(max_length=100) 
    experience_description = models.TextField()
#    date_atu = models.DateTimeField(default=datetime.now(),blank=True)

class Education(models.Model):
    id_user = models.ForeignKey(User,models.CASCADE,related_name='educations')
    education_name = models.CharField(max_length=200)
    institution =  models.CharField(max_length=200)
    period = models.CharField(max_length=100) 
 #   date_atu = models.DateTimeField(default=datetime.now(),blank=True)

class Skill(models.Model):
    id_user = models.ForeignKey(User,models.CASCADE,related_name='skills')
    skill_name = models.CharField(max_length=200)
    skill_description =  models.CharField(max_length=200) 
  #  date_atu = models.DateTimeField(default=datetime.now(),blank=True)

class Award(models.Model):
    id_user = models.ForeignKey(User,models.CASCADE,related_name='awards')
    awards_name = models.CharField(max_length=200)
    awards_description =  models.CharField(max_length=200) 
    #date_atu = models.DateTimeField(default=datetime.now(),blank=True)