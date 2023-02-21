from django.contrib import admin
from .models import User,Experience,Education,Skill,Award

admin.site.register(User)
admin.site.register(Experience)
admin.site.register(Education) 
admin.site.register(Skill)
admin.site.register(Award)