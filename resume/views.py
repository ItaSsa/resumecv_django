from django.shortcuts import render
from .models import User,Experience,Education,Skill,Award


def index(request):
    users = User.objects.all().values()
    experience = Experience.objects.all()
    education = Education.objects.all()
    skill = Skill.objects.all().values()
    award = Award.objects.all().values()
  


    dados = {
        'users' : users[0],
        'experiences': experience, 
        'educations' : education,
        'skills' : skill,
        'awards' : award
    }


    return render(request, "index.html", dados)
