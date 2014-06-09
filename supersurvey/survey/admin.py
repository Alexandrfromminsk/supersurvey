from django.contrib import admin
from survey.models import *

admin.site.register(Respondent)
admin.site.register(Survey)
admin.site.register(Variant)
admin.site.register(Question)