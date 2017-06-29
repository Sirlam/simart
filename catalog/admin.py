from django.contrib import admin

# Register your models here.
from .models import BankAccount, CrudeType, OnAccount, Station

admin.site.register(BankAccount)
admin.site.register(CrudeType)
admin.site.register(OnAccount)
admin.site.register(Station)

