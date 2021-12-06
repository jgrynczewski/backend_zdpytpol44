from django.contrib import admin

from relations.models import Country
from relations.models import Capital

# Register your models here.
admin.site.register(Country)
admin.site.register(Capital)