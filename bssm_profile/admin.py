from django.contrib import admin
from .models import Category
from .models import Project
from .models import Skill
from .models import Tool


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tool)
