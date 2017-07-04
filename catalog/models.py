from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

import uuid


class Station(models.Model):
    """
    Model representing Filling stations
    """
    station_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Stations")
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        String for representing the Model objects.
        """
        return reverse('station-detail', args=[str(self.station_id)])


class CrudeType(models.Model):
    """
    Model representing Tanks belonging to each filling stations
    """
    CRUDE_TYPE = (
        ('PMS', 'Petrol'),
        ('DPK', 'Diesels'),
        ('AGO', 'Kerosene'),
        ('GAS', 'Natural Gas'),
    )
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Products")
    crude_type = models.CharField(max_length=3, unique=True, choices=CRUDE_TYPE, blank=True, default='PMS', help_text="Select the Crude product")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.crude_type


class OnAccount(models.Model):
    """
    Model for on Account Sales
    """
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Pumps")
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        String for representing the Model objects.
        """
        return reverse('account-detail', args=[str(self.account_id)])


class BankAccount(models.Model):
    """
    Model representing Bank Accounts
    """
    name = models.CharField(max_length=200, help_text="What was purchased or deducted from the main account")
    account_number = models.PositiveIntegerField(help_text="Account Number")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.name, self.account_number)


#  Models for tanks and sales


class Tank(models.Model):
    """
    Model representing Tanks belonging to each filling stations
    """

    tank_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Tanks")
    tank = models.CharField(max_length=200)
    crude_type = models.ForeignKey(CrudeType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.tank, self.crude_type)


class StationTank(models.Model):
    """
    Model representing or connecting tanks to a particular station
    """
    tank = models.ForeignKey(Tank, on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ("station", "tank")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.tank, self.station)


class TankQuantity(models.Model):
    """
    Model for Tank Quantity
    """
    tank = models.ForeignKey(StationTank, on_delete=models.SET_NULL, null=True)
    opening = models.PositiveIntegerField()
    closing = models.PositiveIntegerField()
    under = models.PositiveIntegerField()
    pump = models.DecimalField(max_digits=6, decimal_places=2)
    new = models.PositiveIntegerField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.tank


class Pump(models.Model):
    """
    Model representing Fuel Pumps
    """
    pump_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Pumps")
    crude_type = models.ForeignKey(CrudeType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        unique_together = ("crude_type", "name")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.name, self.crude_type)


class StationPump(models.Model):
    """
    Models associating Pump to station and Tanks
    """
    tank = models.ForeignKey(StationTank, on_delete=models.SET_NULL, null=True)
    pump = models.ForeignKey(Pump, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ("tank", "pump")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.pump, self.tank)

#  Models for sales


class PumpSale(models.Model):
    """
    Model representing Sales of pump Products
    """
    sale_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Pumps")
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    pump = models.ForeignKey(StationPump, on_delete=models.SET_NULL, null=True)
    opening = models.DecimalField(max_digits=9, decimal_places=2)
    closing = models.DecimalField(max_digits=9, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    sale_add_date = models.DateField(auto_now=True)
    date_purchased = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.sale_id, self.pump)


class OnAccountSale(models.Model):
    """
    Model for on Account Sales
    """
    account_sale = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Pumps")
    on_account = models.ForeignKey(OnAccount, on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    sale_add_date = models.DateField(auto_now=True)
    date_purchased = models.DateField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.account_sale, self.on_account)


class Voucher(models.Model):
    """
    Model representing expenditure
    """
    info = models.CharField(max_length=200, help_text="What was purchased or deducted from the main account")
    value = models.PositiveIntegerField()
    date_added = models.DateField(auto_now=True)
    date_used = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.id, self.info)


class DepositAmount(models.Model):
    """
    Model representing Bank deposited Amount to
    """
    bank = models.ForeignKey(BankAccount, on_delete=models.SET_NULL, null=True)
    sale = models.ForeignKey(PumpSale, on_delete=models.SET_NULL, null=True)
    sale_add_date = models.DateField(auto_now=True)
    amount = models.CharField(max_length=200, help_text="Amount Deposited")