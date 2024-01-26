# from .models import *
# from accounts.models import *
# from django.forms import ModelForm, TextInput, Textarea, IntegerField, BooleanField, FileField
# from django import forms
# from django.utils import timezone

# from django.forms.widgets import DateInput


# class CategoryForm(ModelForm):
#     class Meta:
#         department = forms.ModelChoiceField(
#             queryset=Department.objects.all(), empty_label="Select  department")
#         model = category
#         fields = ['category_name', 'category_department',
#                   'total_groups', 'description']
#         widgets = {
#             'category_name': forms.TextInput(),
#             'category_department': forms.Select(),
#             'total_groups': forms.TextInput(),
#             'description': forms.Textarea()
#         }


# class ItemGroupForm(ModelForm):
#     class Meta:
#         cate = forms.ModelChoiceField(
#             queryset=category.objects.all(), empty_label="Select  category")
#         model = itemGroup
#         fields = ['group_name', 'group_category', 'description']
#         widgets = {
#             'group_name': forms.TextInput(),
#             'group_category': forms.Select(),
#             'description': forms.Textarea()
#         }


# class wareHouseForm(ModelForm):
#     class Meta:
#         model = wareHouse
#         department = forms.ModelChoiceField(
#             queryset=Department.objects.all(), empty_label="Select  department")
#         fields = ['wareHouse_name', 'warehouse_location', 'department']
#         widgets = {
#             'wareHouse_name': forms.TextInput(),
#             'warehouse_location': forms.TextInput(),
#             'department': forms.Select(),
#         }


# class ItemForm(ModelForm):
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(), empty_label="Select  department")
#     group = forms.ModelChoiceField(
#         queryset=itemGroup.objects.all(), empty_label="Select  itemGroup")
#     item_warehouse = forms.ModelChoiceField(
#         queryset=wareHouse.objects.all(), empty_label="Select warehouse")
#     is_set = forms.BooleanField(
#         required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(), empty_label="Select user")

#     class Meta:
#         model = item
#         fields = [
#             'item_name',
#             'item_brand',
#             'item_serial_number',
#             'item_barcode',
#             'is_set',
#             'total_item_set',
#             'total_item_Pices',
#             'description',
#             'suplier_information',
#         ]
#         widgets = {
#             'item_name': forms.TextInput(),
#             'item_brand': forms.TextInput(),
#             'item_serial_number': forms.TextInput(),
#             'item_barcode': forms.TextInput(),
#             'total_item_set': forms.TextInput(),
#             'total_itemPices': forms.TextInput(),
#             'item_import_date': forms.DateTimeField(),
#             'description': forms.Textarea(),
#             'suplier_information': forms.TextInput(),
#             'department': forms.Select(),
#             'item_warehouse': forms.Select(),
#         }


# class SpareItemForm(ModelForm):
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(), empty_label="Select  department")
#     group = forms.ModelChoiceField(
#         queryset=itemGroup.objects.all(), empty_label="Select  itemGroup")
#     warehouse_location = forms.ModelChoiceField(
#         queryset=wareHouse.objects.all(), empty_label="Select warehouse")
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(), empty_label="Select user")
#     is_set = forms.BooleanField(
#         required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

#     class Meta:
#         model = spareItem
#         fields = [
#             'spare_name',
#             'item_brand',
#             'item_serial_number',
#             'item_barcode',
#             'is_set',
#             'total_itemset',
#             'total_itemPices',
#             'description',
#             'suplier_information',
#         ]
#         widgets = {
#             'spare_name': forms.TextInput(),
#             'item_brand': forms.TextInput(),
#             'item_serial_number': forms.TextInput(),
#             'item_barcode': forms.TextInput(),
#             'total_item_set': forms.TextInput(),
#             'total_item_pices': forms.TextInput(),
#             'description': forms.Textarea(),
#             'suplier_information': forms.TextInput(),
#             'department': forms.Select(),
#             'warehouse_location': forms.Select(),
#         }


# class OrderToTakeOutForm(ModelForm):
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(), empty_label="Select user")
#     item_to_ordered = forms.ModelChoiceField(
#         queryset=item.objects.all(), empty_label="Select item")
#     sapre_item_to_be_ordered = forms.ModelChoiceField(
#         queryset=spareItem.objects.all(), empty_label="Select item")
#     is_set = forms.BooleanField(
#         required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
#     is_spare = forms.BooleanField(
#         required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
#     take_out_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
#     delivered_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

#     class Meta:
#         model = takeoutOrders
#         fields = ['item_to_ordered', 'sapre_item_to_be_ordered', 'is_set', 'is_spare', 'total_itemset', 'total_itemPices', 'description',
#                   'take_out_date', 'delivered_date', 'user2', 'user3']
#         widgets = {
#             'item_to_ordered': forms.Select(),
#             'sapre_item_to_be_ordered': forms.Select(),
#             'total_itemset': forms.TextInput(),
#             'total_itemPices': forms.TextInput(),
#             'description': forms.Textarea(),

#         }

#         def __init__(self, *args, **kwargs):
#             super(OrderToTakeOutForm, self).__init__(*args, **kwargs)
#             self.fields['item_to_ordered'].required = False
#             self.fields['sapre_item_to_be_ordered'].required = False
#             self.fields['sapre_item_to_be_ordered'].required = False
#             self.fields['is_set'].required = False
#             self.fields['is_spare'].required = False
#             self.fields['take_out_date'].required = False
#             self.fields['delivered_date'].required = False
#             self.fields['user2'].required = False
#             self.fields['user3'].required = False

#         def clean(self):
#             cleaned_data = super().clean()
#             print('cleaned_data:', cleaned_data)
#             return cleaned_data

# # class TakeOutForm(ModelForm):

# #     class Meta:
# #         model = takeoutOrders
# #         fields = ['user2', 'item']


# class CrossDockForm(ModelForm):
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(), empty_label="Select  department")
#     warehouse_center = forms.ModelChoiceField(
#         queryset=wareHouse.objects.all(), empty_label="Select warehouse")
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(), empty_label="Select user")

#     class Meta:
#         model = crossDock
#         fields = [
#             'file',
#             'filename',
#             'warehouse_center',
#             'department'
#         ]
#     widgets = {
#         'file': forms.FileField(),
#         'filename': forms.TextInput(),
#         'warehouse_center': forms.Select(),
#         'department': forms.Select(),
#     }


# class maintainableItemForm(ModelForm):
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(), empty_label="Select  department")
#     item_to_be_maintained = forms.ModelChoiceField(required=False,
#                                                    queryset=item.objects.all(), empty_label="Select  maintainable item")
#     spare_item = forms.ModelChoiceField(queryset=spareItem.objects.all(
#     ), empty_label="Select spare for  maintainable item")
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(), empty_label="Select user")
#     Main_warehouse = forms.ModelChoiceField(
#         queryset=wareHouse.objects.all(), empty_label="Select warehouse")
#     is_set = forms.BooleanField(
#         required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
#     is_spare = forms.BooleanField(
#         required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

#     return_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

#     class Meta:
#         model = maintainableItem
#         fields = [
#             'is_spare',
#             'spare_item',
#             'item_to_be_maintained',
#             'department',
#             'Main_warehouse',
#             'is_set',
#             'is_spare',
#             'cause_for_maintenance',
#             'return_date'

#         ]
#     widgets = {
#         'spare_item': forms.Select(),
#         'item_to_be_maintained': forms.Select(),
#         'department': forms.Select(),
#         'Main_warehouse': forms.Select(),
#         'cause_for_maintenance': forms.Textarea(),
#     }

#     def clean(self):
#         cleaned_data = super().clean()
#         print('cleaned_data:', cleaned_data)
#         return cleaned_data


# class returnedMaintainaceItemForm(ModelForm):
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(), empty_label="Select  department")
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(), empty_label="Select user")
#     Main_warehouse = forms.ModelChoiceField(
#         queryset=wareHouse.objects.all(), empty_label="Select warehouse")
#     return_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

#     class Meta:
#         model = maintenanceHistory
#         fields = [
#             'item_name',
#             'item_brand',
#             'item_serial_number',
#             'item_barcode',
#             'return_date',
#         ]
#         widgets = {
#             'item_name': forms.TextInput(),
#             'item_brand': forms.TextInput(),
#             'item_serial_number': forms.TextInput(),
#             'item_barcode': forms.TextInput(),
#         }


# class DamagedItemForm(ModelForm):
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(), empty_label="Select  department")
#     spare_item = forms.ModelChoiceField(
#         queryset=spareItem.objects.all(), empty_label="Select  Damaged item")
#     item_damaged = forms.ModelChoiceField(
#         queryset=item.objects.all(), empty_label="Select  Damaged item")
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(), empty_label="Select user")
#     is_spare = forms.BooleanField(
#         required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

#     class Meta:
#         model = damagedItem
#         fields = [
#             'spare_item',
#             'item_damaged',
#             'is_spare',
#             'department',
#             'cause_for_damage',

#         ]
#     widgets = {
#         'spare_item': forms.Select(),
#         'item_damaged': forms.Select(),
#         'department': forms.Select(),
#         'cause_for_damage': forms.Textarea(),

#     }


# class thresholdItemsForms(ModelForm):
#     threshold_item = forms.ModelChoiceField(
#         queryset=itemGroup.objects.all(), empty_label="Select  Damaged item")
#     spare_item = forms.ModelChoiceField(
#         queryset=spareItem.objects.all(), empty_label="Select damagedItem")
#     department = forms.ModelChoiceField(
#         queryset=Department.objects.all(), empty_label="Select  department")

#     class Meta:
#         model = thresholdItems
#         fields = '__all__'
#     widgets = {
#         'threshold_item': forms.Select(),
#         'spare_item': forms.Select(),
#         'low_stock_level': forms.TextInput(),
#         'High_stock_level': forms.TextInput(),
#         'department': forms.Select(),
#     }
