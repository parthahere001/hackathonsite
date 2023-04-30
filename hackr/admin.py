from django.contrib import admin
from .models import hackathonsModel, hackersModel

admin.site.register(hackathonsModel)
admin.site.register(hackersModel)
