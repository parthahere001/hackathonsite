from django.contrib import admin
from .models import hackathonsModel, hackersModel, submissionModel

admin.site.register(hackathonsModel)
admin.site.register(hackersModel)
admin.site.register(submissionModel)
