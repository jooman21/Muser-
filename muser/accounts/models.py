from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from ims.models import *
from django.contrib.auth.models import Group


class User(AbstractUser):
    # id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50, null=True)
    department = models.ForeignKey(
        'Department', max_length=100, on_delete=models.PROTECT, null=True, related_name='user_department')
    Phone_number = models.CharField(
        max_length=12, null=True, blank=True, unique=True)
    dark_mode = models.BooleanField(default=False, blank=True)


class Department(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             null=False, blank=False, related_name='department_owner')

    def __str__(self):
        return self.department_name


class Message(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=False, null=False)
    date_completed = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    seen = models.BooleanField(default=False, null=False, blank=False)
    cross_docking = models.ForeignKey(
        crossDock, on_delete=models.PROTECT, null=True, blank=True)
    cross_docking = models.BooleanField(default=False, null=False, blank=False)
    maintainable_item = models.ForeignKey(
        maintainableItem, on_delete=models.PROTECT, null=True, blank=True)
    maintaince = models.BooleanField(default=False, null=False, blank=False)
    order_takeout = models.ForeignKey(
        takeoutOrders, on_delete=models.PROTECT, null=True, blank=True)
    takeout = models.BooleanField(default=False, null=False, blank=False)
    damaged_item = models.ForeignKey(
        damagedItem, on_delete=models.PROTECT, null=True, blank=True)
    damaged = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        if self.order_takeout:
            return f'The Item {self.order_takeout} is now in {self.status} On {self.date_completion}  '
        else:
            return f'Cross-Docked {self.cross_docking} On {self.date_completion}'
