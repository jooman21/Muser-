# Generated by Django 5.0.1 on 2024-01-26 10:35

import django.db.models.deletion
import ims.validator
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('total_groups', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('category_department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Item_department', to='accounts.department')),
            ],
        ),
        migrations.CreateModel(
            name='itemGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('totalItem', models.PositiveIntegerField(default=0)),
                ('group_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='ims.category')),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_brand', models.CharField(max_length=50)),
                ('item_serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('is_set', models.BooleanField(blank=True, default=False)),
                ('subsets', models.JSONField(default=dict, null=True)),
                ('item_import_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=150)),
                ('suplier_information', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_for', to='accounts.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_user', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ims.itemgroup')),
            ],
        ),
        migrations.CreateModel(
            name='spareGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sparegroup_name', models.CharField(max_length=50, unique=True)),
                ('sparedescription', models.TextField(blank=True, max_length=150, null=True)),
                ('totalSpare', models.PositiveIntegerField(default=0)),
                ('sparegroup_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='spareCategory', to='ims.category')),
            ],
        ),
        migrations.CreateModel(
            name='spareItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_name', models.CharField(max_length=50)),
                ('item_brand', models.CharField(max_length=50)),
                ('item_serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('is_set', models.BooleanField(default=False)),
                ('spare_import_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=150)),
                ('suplier_information', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='spareItem_for', to='accounts.department')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ims.sparegroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_spareItem', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='maintainableItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_spare', models.BooleanField(blank=True, null=True)),
                ('is_on_site', models.BooleanField(blank=True, null=True)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('item_brand', models.CharField(blank=True, max_length=50, null=True)),
                ('item_serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('out_for_maintain_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('site_location', models.CharField(blank=True, max_length=50, null=True)),
                ('cause_for_maintenance', models.TextField(max_length=150)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='maintainableItem_department', to='accounts.department')),
                ('item_to_be_maintained', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='item_to_be_maintained', to='ims.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='maintainableItem', to=settings.AUTH_USER_MODEL)),
                ('spare_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='maintainableItem', to='ims.spareitem')),
            ],
        ),
        migrations.CreateModel(
            name='damagedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_spare', models.BooleanField(blank=True, null=True)),
                ('is_on_site', models.BooleanField(blank=True, null=True)),
                ('site_location', models.CharField(blank=True, max_length=50, null=True)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('item_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('item_brand', models.CharField(blank=True, max_length=50, null=True)),
                ('item_serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('suplier_information', models.CharField(max_length=50)),
                ('damaged_date', models.DateTimeField(auto_now_add=True)),
                ('cause_for_damage', models.TextField(max_length=250)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='damagedItem_department', to='accounts.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='damaged_items_user', to=settings.AUTH_USER_MODEL)),
                ('item_damaged', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='item_damaged', to='ims.item')),
                ('spare_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='damaged_items', to='ims.spareitem')),
            ],
        ),
        migrations.CreateModel(
            name='takeoutOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_set', models.BooleanField(default=False)),
                ('total_itemset', models.PositiveIntegerField(blank=True, null=True)),
                ('total_itemPices', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=150)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('take_out_date', models.DateField(blank=True, null=True)),
                ('delivered_date', models.DateField(blank=True, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.item')),
                ('spare_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.spareitem')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders_created', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_taken_out', to=settings.AUTH_USER_MODEL)),
                ('user3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_delivered', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='thresholdItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_stock_level', models.PositiveIntegerField(blank=True, null=True)),
                ('High_stock_level', models.PositiveIntegerField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items_threshold', to='accounts.department')),
                ('itemsGroup_threshold', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_threshold', to='ims.itemgroup')),
                ('spare_item_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='spare_parts_accessories', to='ims.sparegroup')),
            ],
        ),
        migrations.CreateModel(
            name='wareHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wareHouse_name', models.CharField(max_length=100)),
                ('warehouse_location', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='warehouse_department', to='accounts.department')),
            ],
        ),
        migrations.CreateModel(
            name='transactionReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_file', models.FileField(upload_to='uploads/itemsreport/%Y/%m/%d/', validators=[ims.validator.crossdock_file_extension, ims.validator.file_size_1_10])),
                ('delivery_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='delivery_user_report', to='ims.takeoutorders')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itemsreport_for', to='accounts.department')),
                ('warehouse_center', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='report_from_warehouse', to='ims.warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='spareitem',
            name='warehouse_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='spareItem_location', to='ims.warehouse'),
        ),
        migrations.CreateModel(
            name='maintenanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('item_brand', models.CharField(max_length=50)),
                ('item_serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('site_returned_from', models.CharField(max_length=50)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='returned_maintainableItem_department', to='accounts.department')),
                ('maintain_history', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='maintainance_history', to='ims.maintainableitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='returned_maintainableItem', to=settings.AUTH_USER_MODEL)),
                ('main_warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='returned_form_maintainace', to='ims.warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='maintainableitem',
            name='Main_warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='maintainable_item_warehouse', to='ims.warehouse'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items_location', to='ims.warehouse'),
        ),
        migrations.CreateModel(
            name='crossDock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100, unique=True)),
                ('file', models.FileField(unique=True, upload_to='uploads/crossDock/%Y/%m/%d/', validators=[ims.validator.crossdock_file_extension, ims.validator.file_size_1_10])),
                ('arrival_date', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='crossDock_for', to='accounts.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='crossDock', to=settings.AUTH_USER_MODEL)),
                ('warehouse_center', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='crossDock_location', to='ims.warehouse')),
            ],
        ),
    ]
