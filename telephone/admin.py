from django.contrib import admin
from . import models

admin.site.register(models.Phone)
admin.site.register(models.Review)
admin.site.register(models.Comment)