from django.contrib import admin

from Auth import models

# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.ConfirmCode)