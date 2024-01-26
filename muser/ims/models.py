from django.db import models

from django.db import models
from .validator import crossdock_file_extension, file_size_1_10
import json





class category(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=50, null=False, blank=False)
    category_department = models.ForeignKey(
        "accounts.Department", on_delete=models.PROTECT, null=False, blank=False, related_name='Item_department')
    total_groups = models.PositiveIntegerField(
        default=0, null=False, blank=False)
    description = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.category_name


class itemGroup(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_category = models.ForeignKey(
        category, on_delete=models.PROTECT, blank=True, related_name='category')
    group_name = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(max_length=150, null=True, blank=True)
    totalItem = models.PositiveIntegerField(
        default=0, null=False, blank=False)                                        

    def __str__(self):
        return self.group_name


class spareGroup(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sparegroup_category = models.ForeignKey(
        category, on_delete=models.PROTECT, blank=True, related_name='spareCategory')
    sparegroup_name = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    sparedescription = models.TextField(max_length=150, null=True, blank=True)
    totalSpare = models.PositiveIntegerField(
        default=0, null=False, blank=False)
    def __str__(self):
        return self.sparegroup_name


class wareHouse(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wareHouse_name = models.CharField(max_length=100, null=False, blank=False)
    warehouse_location = models.CharField(
        max_length=50, null=False, blank=False)
    department = models.ForeignKey("accounts.Department", on_delete=models.PROTECT,
                                   null=False, blank=False, related_name='warehouse_department')

    def __str__(self):
        return self.wareHouse_name


class item(models.Model):  # barcode needed
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_name = models.CharField(max_length=50, null=False, blank=False)
    item_brand = models.CharField(max_length=50, null=False, blank=False)
    item_serial_number = models.CharField(max_length=50, null=True, blank=True)
    item_barcode = models.CharField(
        max_length=50, null=True, blank=True)  # focus area
    is_set = models.BooleanField(default=False, null=False, blank=True)
    subsets = models.JSONField(blank=False, null=True, default=dict)
 #focus point
    # total_item_Pices = models.PositiveIntegerField(null=True, blank=True)
    item_import_date = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    description = models.TextField(max_length=150)
    suplier_information = models.CharField(max_length=50)
    group = models.ForeignKey(
        itemGroup, on_delete=models.PROTECT, null=False, blank=False)
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                             related_name='item_user', null=False, blank=False)
    department = models.ForeignKey(
        "accounts.Department", on_delete=models.PROTECT, related_name='item_for', null=False, blank=False)
    item_warehouse = models.ForeignKey(
        wareHouse, on_delete=models.PROTECT, related_name='items_location', null=False, blank=False)
    
    def set_items(self, items_list):
        self.subsets = items_list

    def get_items(self):
        return self.subsets if self.subsets else []

    def __str__(self):
        return self.item_name


class spareItem(models.Model):  # barcode needed
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    spare_name = models.CharField(max_length=50, null=False, blank=False)
    item_brand = models.CharField(max_length=50, null=False, blank=False)
    item_serial_number = models.CharField(max_length=50, null=True, blank=True)
    item_barcode = models.CharField(
        max_length=50, null=True, blank=True)  # need focus
    is_set = models.BooleanField(default=False, null=False, blank=False)
    # total_itemPices = models.PositiveIntegerField(null=True)
    spare_import_date = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    description = models.TextField(max_length=150)
    suplier_information = models.CharField(max_length=50)
    group = models.ForeignKey(
        spareGroup, on_delete=models.PROTECT, null=False, blank=False)
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                             related_name='user_spareItem', null=False, blank=False)
    department = models.ForeignKey("accounts.Department", on_delete=models.PROTECT,
                                   related_name='spareItem_for', null=False, blank=False)
    warehouse_location = models.ForeignKey(
        wareHouse, on_delete=models.PROTECT, related_name='spareItem_location', null=False, blank=False)

    def __str__(self):
        return self.spare_name


class takeoutOrders(models.Model):  # barcode needed
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(
        item, on_delete=models.CASCADE, null=True, blank=True)
    spare_item = models.ForeignKey(
        spareItem, on_delete=models.CASCADE, null=True, blank=True)
    is_set = models.BooleanField(default=False, null=False, blank=False)
    total_itemset = models.PositiveIntegerField(null=True, blank=True)
    total_itemPices = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField(max_length=150, null=False, blank=False)
    order_date = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    user1 = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                              related_name='orders_created', null=False, blank=False)
    user2 = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                              null=True, blank=True, related_name='orders_taken_out')
    take_out_date = models.DateField(null=True, blank=True)
    user3 = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                              null=True, blank=True, related_name='orders_delivered')
    delivered_date = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.is_set:
            return f'The total number of {self.item} are {self.total_itemset} in set'
        else:
            return f'The total number of {self.item} are {self.total_itemPices} in pices'


class crossDock(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    file = models.FileField(upload_to='uploads/crossDock/%Y/%m/%d/', validators=[
                            crossdock_file_extension, file_size_1_10], null=False, blank=False, unique=True)
    arrival_date = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    warehouse_center = models.ForeignKey(
        wareHouse, on_delete=models.PROTECT, related_name='crossDock_location', null=False, blank=False)
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                             related_name='crossDock', null=False, blank=False)
    department = models.ForeignKey("accounts.Department", on_delete=models.PROTECT,
                                   related_name='crossDock_for', null=False, blank=False)
    # file_hash = models.CharField(
    #     max_length=32, unique=True, null=True, blank=True)

    def __str__(self):
        return f'cross dock {self.filename} from {self.warehouse_center} on date {self.arrival_date}'


# file name = totalnumberofitems_department_warehouse_date   &&      file extention = pdf     ///////////////////////
class transactionReport(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report_file = models.FileField(upload_to='uploads/itemsreport/%Y/%m/%d/', validators=[
        crossdock_file_extension, file_size_1_10], null=False, blank=False)
    delivery_user = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                                      related_name='oser_on_transactionReport', null=False, blank=False)
    warehouse_center = models.ForeignKey(
        wareHouse, on_delete=models.PROTECT, related_name='report_from_warehouse', null=False, blank=False)
    department = models.ForeignKey("accounts.Department", on_delete=models.PROTECT,
                                   related_name='itemsreport_for', null=False, blank=False)
    delivery_user = models.ForeignKey(takeoutOrders, on_delete=models.PROTECT, related_name='delivery_user_report',
                                      null=False, blank=False)

    def __str__(self):
        return f'{self.department} from {self.warehouse_center} on {{self.takeout_date}}'


class maintainableItem(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    item_to_be_maintained = models.ForeignKey(
        item, on_delete=models.PROTECT, related_name='item_to_be_maintained', null=True, blank=True)
    is_spare = models.BooleanField(null=True, blank=True)
    spare_item = models.ForeignKey(
        spareItem, on_delete=models.PROTECT, related_name='maintainableItem', null=True, blank=True)
    is_on_site = models.BooleanField(null=True, blank=True)
    item_name = models.CharField(max_length=50, null=True, blank=True)
    item_barcode = models.CharField(
        max_length=50, null=True, blank=True)
    item_brand = models.CharField(max_length=50, null=True, blank=True)
    item_serial_number = models.CharField(max_length=50, null=True, blank=True)
    out_for_maintain_date = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    return_date = models.DateField(null=True, blank=True)
    site_location = models.CharField(max_length=50, null=True, blank=True)
    cause_for_maintenance = models.TextField(
        max_length=150, null=False, blank=False)
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                             related_name='maintainableItem', null=False, blank=False)
    department = models.ForeignKey("accounts.Department", on_delete=models.PROTECT,
                                   related_name='maintainableItem_department', null=False, blank=False)
    Main_warehouse = models.ForeignKey(
        wareHouse, on_delete=models.PROTECT, related_name='maintainable_item_warehouse', null=False, blank=False)

    def __str__(self):
        if self.spare_item:
            return f'The spare part {self.spare_item} is on maintenance starting from {self.out_for_maintain_date} up to {self.return_date}'
        else:
            return f'The item {self.item_to_be_maintained} is on maintenance starting from {self.out_for_maintain_date} up to {self.return_date}'


class maintenanceHistory(models.Model):
    maintain_history = models.ForeignKey(
        maintainableItem, on_delete=models.PROTECT, related_name='maintainance_history', null=False, blank=False)
    item_name = models.CharField(max_length=50, null=False, blank=False)
    item_barcode = models.CharField(
        max_length=50, null=True, blank=True)
    item_brand = models.CharField(max_length=50, null=False, blank=False)
    item_serial_number = models.CharField(max_length=50, null=True, blank=True)
    site_returned_from = models.CharField(
        max_length=50, null=False, blank=False)
    return_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                             related_name='returned_maintainableItem', null=False, blank=False)
    department = models.ForeignKey("accounts.Department", on_delete=models.PROTECT,
                                   related_name='returned_maintainableItem_department', null=False, blank=False)
    main_warehouse = models.ForeignKey(
        wareHouse, on_delete=models.PROTECT, related_name='returned_form_maintainace', null=False, blank=False)


class damagedItem(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_damaged = models.ForeignKey(
        item, on_delete=models.PROTECT, related_name='item_damaged', null=True, blank=True)
    spare_item = models.ForeignKey(
        spareItem, on_delete=models.PROTECT, related_name='damaged_items', null=True, blank=True)
    is_spare = models.BooleanField(null=True, blank=True)
    is_on_site = models.BooleanField(null=True, blank=True)
    site_location = models.CharField(max_length=50, null=True, blank=True)
    item_name = models.CharField(max_length=50, null=True, blank=True)
    item_barcode = models.CharField(
        max_length=50, null=True, blank=True)
    item_brand = models.CharField(max_length=50, null=True, blank=True)
    item_serial_number = models.CharField(max_length=50, null=True, blank=True)
    suplier_information = models.CharField(max_length=50)
    damaged_date = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)
    cause_for_damage = models.TextField(
        max_length=250, null=False, blank=False)
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT,
                             related_name='damaged_items_user', null=False, blank=False)
    department = models.ForeignKey("accounts.Department", on_delete=models.PROTECT,
                                   related_name='damagedItem_department', null=False, blank=False)

    def __str__(self):
        if self.spare_item:
            return f'The spare part {self.spare_item} is damaged on {self.date_of_damaged}'
        else:
            return f'The spare part {self.item_damaged} is damaged on {self.date_of_damaged}'


class thresholdItems(models.Model):
    department = models.ForeignKey('accounts.department', on_delete=models.PROTECT,
                                   related_name='items_threshold', null=False, blank=False)
    itemsGroup_threshold = models.ForeignKey(
        itemGroup, on_delete=models.SET_NULL, related_name='items_threshold', null=True, blank=True)
    spare_item_group = models.ForeignKey(spareGroup, on_delete=models.PROTECT,
                                         related_name='spare_parts_accessories', null=True, blank=True)
    low_stock_level = models.PositiveIntegerField(null=True, blank=True)
    High_stock_level = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        if self.spare_item_group:
            return f'Threshold for {self.spare_item_group} -min {self.low_stock_level} -max {self.High_stock_level}'
        else:
            return f'Threshold for {self.itemsGroup_threshold} -min {self.low_stock_level} -max {self.High_stock_level}'

