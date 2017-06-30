from django.contrib import admin

# Register your models here.
from .models import BankAccount, CrudeType, OnAccount, Pump, Station, StationPump, StationTank, Tank, TankQuantity, DepositAmount, OnAccountSale, PumpSale, Voucher

admin.site.register(BankAccount)
admin.site.register(CrudeType)
admin.site.register(OnAccount)
admin.site.register(Station)
admin.site.register(Pump)
admin.site.register(StationTank)
admin.site.register(StationPump)
admin.site.register(Tank)
admin.site.register(TankQuantity)
admin.site.register(DepositAmount)
admin.site.register(OnAccountSale)
#  admin.site.register(PumpSale)
admin.site.register(Voucher)

@admin.register(PumpSale)
class PumpSaleAdmin(admin.ModelAdmin):
    list_display = ('station', 'pump', 'opening', 'closing', 'rate', 'sale_add_date')




