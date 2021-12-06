from django.contrib import admin

from relations.models import Country
from relations.models import Capital
from relations.models import Language
from relations.models import Framework

# Register your models here.
admin.site.register(Country)
admin.site.register(Capital)
admin.site.register(Language)
admin.site.register(Framework)