from django.contrib import admin

# Register your models here.
from .models import Station, CrudeType, Tank, Pump, OnAccount, OnAccountSale, PumpSale, StationPump, Voucher, TankQuantity, BankAccount, DepositAmount

admin.site.register(Station)
admin.site.register(CrudeType)
admin.site.register(Tank)
admin.site.register(Pump)
admin.site.register(OnAccount)
admin.site.register(OnAccountSale)
admin.site.register(PumpSale)
admin.site.register(StationPump)
admin.site.register(Voucher)
admin.site.register(TankQuantity)
admin.site.register(BankAccount)
admin.site.register(DepositAmount)
