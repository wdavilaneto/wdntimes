from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Orgao)
admin.site.register(Time)
admin.site.register(Projeto)
admin.site.register(Pessoa)
