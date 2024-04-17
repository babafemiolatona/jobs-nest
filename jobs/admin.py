from django.contrib import admin
from .models import (Job, Category, Company,
                     Application, UserProfile)

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Application)
admin.site.register(UserProfile)
