# from django.shortcuts import render
# from .models import *
# from accounts.models import *
# from .forms import *
# from django.shortcuts import render, redirect
# from django.contrib import messages

# # new category creation, deleation, updating


# def newCategory(request):
#     if request.method == 'POST':
#         new_cate = CategoryForm(request.POST)
#         if new_cate.is_valid():
#             category_name = new_cate.cleaned_data['category_name']
#             total_groups = new_cate.cleaned_data['total_groups']
#             description = new_cate.cleaned_data['description']
#             department_name = new_cate.cleaned_data['category_department']

#             try:
#                 category_department = Department.objects.get(
#                     department_name=department_name)
#                 print(category_department, "++++++++++++++++++")
#             except Department.DoesNotExist:
#                 messages.error(request, 'Department not found')
#                 return redirect('newCategory')

#             if category.objects.filter(category_name=category_name).exists():
#                 messages.error(request, 'Category Already Exists')
#                 return redirect('create_category')
#                 # create category
#             new_category = category(
#                 category_name=category_name,
#                 total_groups=total_groups,
#                 description=description,
#                 category_department=category_department
#             )
#             new_category.save()
#             messages.info(request, "category created")
#     else:
#         new_cate = CategoryForm()

#         if request.POST.get('update_category_id'):
#             #       # Update the category

#             category_id = request.POST['update_category_id']
#             try:
#                 cate = category.objects.get(id=category_id)
#                 cate.category_name = category_name
#                 cate.total_groups = total_groups
#                 cate.description = description
#                 cate.category_department.add(category_department)
#                 cate.save()
#                 messages.info(request, 'Category updated')
#             except category.DoesNotExist:
#                 messages.error(request, 'Category not found for updating')
#         elif request.POST.get('delete_category_id'):
#            # Delete the category
#             category_id = request.POST['delete_category_id']
#             try:
#                 cate = category.objects.get(id=category_id)
#                 cate.delete()
#                 messages.info(request, 'Category deleted')
#             except category.DoesNotExist:
#                 messages.error(request, 'Category not found for deleting')

#     context = {'new_cate': new_cate}
#     return render(request, 'ims/test.html', context)

# # create item group and update item group


# def createItemgroup(request):

#     if request.method == 'POST':
#         new_grp = ItemGroupForm(request.POST)
#         if new_grp.is_valid():
#             group_name = new_grp.cleaned_data['group_name']
#             grp_category = new_grp.cleaned_data['group_category']
#             description = new_grp.cleaned_data['description']

#         try:
#             group_category = category.objects.get(category_name=grp_category)
#             # print(group_category, "+++++++++++++++")
#         except category.DoesNotExist:
#             messages.error(request, 'category Group not found')
#             return redirect('createItemgroup')

#         if itemGroup.objects.filter(group_name=group_name).exists():
#             messages.error(request, 'Group Already Exists')
#             return redirect('create_Itemgroup')
#             # create category
#         new_group = itemGroup(
#             group_name=group_name,
#             description=description,
#             group_category=group_category
#         )
#         new_group.save()
#         messages.info(request, "Item Group created")
#         # create new item Group
#     else:
#         new_grp = ItemGroupForm()

#         if request.POST.get('update_group_id'):
#             #  update item Group
#             group_id = request.POST['update_group_id']
#             try:
#                 updated_grp = itemGroup.objects.get(id=group_id)
#                 updated_grp.group_name = group_name
#                 updated_grp.description = description
#                 updated_grp.group_category.add(group_category)
#                 updated_grp.save()
#                 messages.info(request, 'item Group updated')
#             except itemGroup.DoesNotExist:
#                 messages.error(request, 'item Group not found for updating')
#     context = {'new_grp': new_grp}
#     return render(request, 'ims/test.html', context)

# # create warehouse, update and delete


# def createWareHouse(request):
#     if request.method == 'POST':
#         new_ware = wareHouseForm(request.POST)
#         if new_ware.is_valid():
#             wareHouse_name = new_ware.cleaned_data['wareHouse_name']
#             warehouse_location = new_ware.cleaned_data['warehouse_location']
#             warehouse_department = new_ware.cleaned_data['department']
#         try:

#             department = Department.objects.get(
#                 department_name=warehouse_department)
#         except Department.DoesNotExist:
#             messages.error(request, 'Department not found')
#             return redirect('createWareHouse')
#         if wareHouse.objects.filter(wareHouse_name=wareHouse_name, department=department).exists():
#             messages.error(request, 'WareHouse Already Exists')
#             return redirect('create_wareHouse')
#             # create new warehouse
#         new_warehouse = wareHouse(
#             wareHouse_name=wareHouse_name,
#             warehouse_location=warehouse_location,
#             department=department)
#         new_warehouse.save()
#         messages.info(request, "warehouse created")
#     else:
#         new_ware = wareHouseForm()

#         if request.POST.get('update_ware_id'):
#             # update the warehouse
#             ware_id = request.POST['update_ware_id']
#             try:
#                 updated_ware = wareHouse.objects.get(id=ware_id)
#                 updated_ware.wareHouse_name = wareHouse_name
#                 updated_ware.wareHouse_name = wareHouse_name
#                 updated_ware.department.add(department)
#                 updated_ware.save()
#                 messages.info(request, 'WareHouse updated')
#             except wareHouse.DoesNotExist:
#                 messages.error(request, 'WareHouse to be updated not found')
#         elif request.POST.get('delete_ware_id'):
#             # Delete the warehouse
#             ware_id = request.POST['delete_ware_id']
#             try:
#                 ware = wareHouse.objects.get(id=ware_id)
#                 ware.delete()
#                 messages.info(request, 'warehouse deleted')
#             except wareHouse.DoesNotExist:
#                 messages.error(request, 'warehouse not found for deleting')
#     context = {'new_ware': new_ware}
#     return render(request, 'ims/test.html', context)

# # create item and delete item ----------------- serial number issue must be fixed !!!  the field must not be empty


# def createItem(request):
#     if request.method == 'POST':
#         new_item = ItemForm(request.POST)
#         if new_item.is_valid():
#             item_name = new_item.cleaned_data['item_name']
#             item_brand = new_item.cleaned_data['item_brand']
#             item_serial_number = new_item.cleaned_data['item_serial_number']
#             item_barcode = new_item.cleaned_data['item_barcode']
#             is_set = new_item.cleaned_data['is_set']
#             total_item_set = new_item.cleaned_data['total_item_set']
#             total_item_Pices = new_item.cleaned_data['total_item_Pices']
#             description = new_item.cleaned_data['description']
#             suplier_information = new_item.cleaned_data['suplier_information']
#             department_name = new_item.cleaned_data['department']
#             itemgroup = new_item.cleaned_data['group']
#             item_ware = new_item.cleaned_data['item_warehouse']
#             user = request.user
#             # print(user, "+++++++++++++++++++", "user")
#         try:
#             department = Department.objects.get(
#                 department_name=department_name)
#             # print(department, "+++++++++++++")
#             group = itemGroup.objects.get(group_name=itemgroup)
#             # print(group, "+++++++++++++")
#             item_warehouse = wareHouse.objects.get(wareHouse_name=item_ware)
#             # print(item_warehouse, "+++++++++++++")
#         except Department.DoesNotExist:
#             messages.error(request, 'Department not found')
#             return redirect('createItem')
#         except itemGroup.DoesNotExist:
#             messages.error(request, 'item group not found')
#             return redirect('createItem')
#         except wareHouse.DoesNotExist:
#             messages.error(request, 'warehouse not found')
#             return redirect('createItem')

#         if item.objects.filter(item_name=item_name, item_brand=item_brand, item_serial_number=item_serial_number).exists():
#             messages.error(request, 'Item Already Exists !!')
#             return redirect('create_item')
#         # create Item
#         newItem = item(item_name=item_name,
#                        item_brand=item_brand,
#                        item_serial_number=item_serial_number,
#                        item_barcode=item_barcode,
#                        is_set=is_set,
#                        total_item_set=total_item_set,
#                        total_item_Pices=total_item_Pices,
#                        description=description,
#                        suplier_information=suplier_information,
#                        department=department,
#                        group=group,
#                        item_warehouse=item_warehouse,
#                        user=user)
#         newItem.save()
#         messages.info(request, "item created")
#     else:
#         new_item = ItemForm()
#         if request.POST.get('delete_item_id'):
#             # delete item
#             item_id = request.POST['delete_item_id']
#             try:
#                 it = item.objects.get(id=item_id)
#                 it.delete()
#                 messages.info(request, "Item deleted")
#             except item.DoesNotExist:
#                 messages.error(request, "item to be deleted not found")

#     context = {'new_item': new_item}
#     return render(request, 'ims/test.html', context)

# # create  spare item and delete item ----------------- serial number issue must be fixed !!!  the field must not be empty


# def createSapreItem(request):
#     if request.method == 'POST':
#         new_spare = SpareItemForm(request.POST)
#         if new_spare.is_valid():
#             spare_name = new_spare.cleaned_data['spare_name']
#             item_brand = new_spare.cleaned_data['item_brand']
#             item_serial_number = new_spare.cleaned_data['item_serial_number']
#             item_barcode = new_spare.cleaned_data['item_barcode']
#             is_set = new_spare.cleaned_data['is_set']
#             total_itemset = new_spare.cleaned_data['total_itemset']
#             total_itemPices = new_spare.cleaned_data['total_itemPices']
#             description = new_spare.cleaned_data['description']
#             suplier_information = new_spare.cleaned_data['suplier_information']
#             department_name = new_spare.cleaned_data['department']
#             itemgroup = new_spare.cleaned_data['group']
#             spare_item_ware = new_spare.cleaned_data['warehouse_location']
#             user = request.user
#         try:
#             department = Department.objects.get(
#                 department_name=department_name)
#             # print(department, "++++++++++++++++++++++++++++++++")
#             group = itemGroup.objects.get(group_name=itemgroup)
#             # print(group, "+++++++++++++")
#             warehouse_location = wareHouse.objects.get(
#                 wareHouse_name=spare_item_ware)
#             # print(item_warehouse, "++++++++++++++++++++++++++++++++++++++")
#         except Department.DoesNotExist:
#             messages.error(request, 'Department not found')
#             return redirect('createSapreItem')
#         except itemGroup.DoesNotExist:
#             messages.error(request, 'item group not found')
#             return redirect('createSapreItem')
#         except wareHouse.DoesNotExist:
#             messages.error(request, 'warehouse not found')
#             return redirect('createSapreItem')
#         if spareItem.objects.filter(spare_name=spare_name, item_brand=item_brand, item_serial_number=item_serial_number).exists():
#             messages.error(request, ' Spare Item Already Exists !!')

#         # create SpareItem
#         newSpare = spareItem(spare_name=spare_name,
#                              item_brand=item_brand,
#                              item_serial_number=item_serial_number,
#                              item_barcode=item_barcode,
#                              is_set=is_set,
#                              total_itemset=total_itemset,
#                              total_itemPices=total_itemPices,
#                              description=description,
#                              suplier_information=suplier_information,
#                              department=department,
#                              group=group,
#                              warehouse_location=warehouse_location,
#                              user=user)
#         newSpare.save()

#         messages.info(request, " Spare item created")

#     else:
#         new_spare = SpareItemForm()
#         if request.POST.get('delete_Spareitem_id'):
#             # delete spare item
#             spareItem_id = request.POST['delete_Spareitem_id']
#             try:
#                 spare_it = spareItem.objects.get(id=spareItem_id)
#                 spare_it.delete()
#                 messages.info(request, " Spare Item deleted")
#             except spareItem.DoesNotExist:
#                 messages.error(request, " Spare item to be deleted not found")
#     context = {'new_spare': new_spare}
#     return render(request, 'ims/test.html', context)

# # full review -------------------------------------------------!!!!


# def ordering_personnel(request):
#     form = None
#     if request.method == 'POST':
#         form = OrderToTakeOutForm(request.POST)
#         if form.is_valid():
#             item_to_order = form.cleaned_data['item_to_ordered']
#             is_spare = form.cleaned_data['is_spare']
#             spare_to_order = form.cleaned_data['sapre_item_to_be_ordered']
#             is_set = form.cleaned_data['is_set']
#             order_total_itemset = form.cleaned_data['total_itemset']
#             order_total_itemPices = form.cleaned_data['total_itemPices']
#             order_description = form.cleaned_data['description']
#             takeout_user = form.cleaned_data['user2']
#             delivery_user = form.cleaned_data['user3']
#             takeout_date = form.cleaned_data['take_out_date']
#             delivered_date = form.cleaned_data['delivered_date']
#             user = request.user
#             try:
#                 item_to_ordered = item.objects.get(
#                     item_name=item_to_order, item_brand=item_to_order, item_serial_number=item_to_order, item_barcode=item_to_order)
#                 sapre_item_to_be_ordered = spareItem.objects.get(
#                     spare_name=spare_to_order, item_brand=spare_to_order, item_serial_number=spare_to_order, item_barcode=spare_to_order)
#             except item.DoesNotExist:
#                 messages.error(request, "Item to order not found")
#                 return redirect(ordering_personnel)
#             except spareItem.DoesNotExist:
#                 messages.error(request, "spare item to order not found")
#                 return redirect(ordering_personnel)
#             if takeoutOrders.objects.filter(item_to_ordered=item_to_ordered, sapre_item_to_be_ordered=sapre_item_to_be_ordered, order_description=order_description).exists():
#                 messages.error(request, "order already pending")
#                 return redirect('ordering_personnel')
#             new_order = takeoutOrders(
#                 item_to_ordered=item_to_ordered,
#                 sapre_item_to_be_ordered=sapre_item_to_be_ordered,
#                 is_spare=is_spare,
#                 is_set=is_set,
#                 order_total_itemset=order_total_itemset,
#                 order_total_itemPices=order_total_itemPices,
#                 order_description=order_description,
#                 takeout_user=takeout_user,
#                 delivery_user=delivery_user,
#                 takeout_date=takeout_date,
#                 delivered_date=delivered_date,
#                 user=user
#             )
#             new_order.save()
#             messages.info(request, "item ordered")
#             return redirect(ordering_personnel)
#         else:
#             form = OrderToTakeOutForm()
#     context = {'form': form}
#     return render(request, 'ims/test.html', context)
# # def takeoutPersonnel(request):
# #     if request.method = 'POST':

# # cross dock file upload not working-------------------------------------------   download file


# def createCrossDock(request):
#     if request.method == 'POST':
#         new_crossDock = CrossDockForm(request.POST)
#         if new_crossDock.is_valid():
#             filename = new_crossDock.cleaned_data['filename']
#             file = new_crossDock.cleaned_data['file']
#             department_name = new_crossDock.cleaned_data['department']
#             crossdock_ware = new_crossDock.cleaned_data['warehouse_center']
#             user = request.user
#             try:
#                 department = Department.objects.get(
#                     department_name=department_name)
#                 # print(department, "+++++++++++++")
#                 warehouse_center = wareHouse.objects.get(
#                     wareHouse_name=crossdock_ware)
#                 # print(warehouse_center, "+++++++++++++")
#             except Department.DoesNotExist:
#                 messages.error(request, 'Department not found')
#                 return redirect('create_CrossDock')
#             except wareHouse.DoesNotExist:
#                 messages.error(request, 'warehouse not found')
#                 return redirect('create_CrossDock')
#             if crossDock.objects.filter(filename=filename, file=file).exists():
#                 messages.error(request, 'Cross Dock Already Exists !!')
#                 return redirect('create_CrossDock')
#         # create cross-dock
#             newDock = crossDock(
#                 filename=filename,
#                 file=file,
#                 department=department,
#                 warehouse_center=warehouse_center,
#                 user=user
#             )
#             newDock.save()
#             messages.info(request, "Cross-Dock created")
#     else:
#         new_crossDock = CrossDockForm()

#         if request.POST.get('delete_dock_id'):
#             # delete cross-dock
#             dock_id = request.POST['delete_dock_id']
#             try:
#                 cross = crossDock.objects.get(id=dock_id)
#                 cross.delete()
#                 messages.info(request, "Cross Dock deleted")

#             except crossDock.DoesNotExist:
#                 messages.error(request, "Cross-Dock to be deleted not found")

#     context = {'new_crossDock': new_crossDock}
#     return render(request, 'ims/test.html', context)

# #

# # create main , update and delete--------------------- issue must be solved is_spare, item_to_be_maintained, spare_item


# def createMaintainableItem(request):
#     new_maintainable_item = None
#     if request.method == 'POST':
#         new_maintainable_item = maintainableItemForm(request.POST)
#         if new_maintainable_item.is_valid():
#             is_set = new_maintainable_item.cleaned_data['is_set']
#             is_spare = new_maintainable_item.cleaned_data['is_spare']
#             maintenance_item_set = new_maintainable_item.cleaned_data['maintenance_item_set']
#             maintenance_item_Pices = new_maintainable_item.cleaned_data['maintenance_item_Pices']
#             cause_for_maintenance = new_maintainable_item.cleaned_data['cause_for_maintenance']
#             maintain_item = new_maintainable_item.cleaned_data['item_to_be_maintained']
#             main_department = new_maintainable_item.cleaned_data['department']
#             maintain_ware = new_maintainable_item['Main_warehouse']
#             main_spare = new_maintainable_item.cleaned_data['spare_item']
#             return_date = new_maintainable_item.cleaned_data['return_date']
#             user = request.user

#             try:
#                 item_to_be_maintained = item.objects.get(
#                     item_name=maintain_item)
#                 department = Department.objects.get(
#                     department_name=main_department)
#                 spare_item = spareItem.objects.get(spare_name=main_spare)
#                 Main_warehouse = wareHouse.objects.get(
#                     wareHouse_name=maintain_ware)
#             except item.DoesNotExist:
#                 messages.error(request, "Item not found")
#                 return redirect(createMaintainableItem)
#             except spareItem.DoesNotExist:
#                 messages.error(request, " Spare Item not found")
#                 return redirect(createMaintainableItem)
#             except Department.DoesNotExist:
#                 messages.error(request, "Department not found")
#                 return redirect(createMaintainableItem)
#             except wareHouse.DoesNotExist:
#                 messages.error(request, "Warehouse not found")
#                 return redirect(createMaintainableItem)
#             if maintainableItem.objects.filter(item_to_be_maintained=item_to_be_maintained, spare_item=spare_item, Main_warehouse=Main_warehouse).exists():
#                 messages.info(request, "Maintainable Item already in place!!")
#                 return redirect(createMaintainableItem)
#             new_main = maintainableItem(
#                 is_set=is_set,
#                 is_spare=is_spare,
#                 maintenance_item_set=maintenance_item_set,
#                 maintenance_item_Pices=maintenance_item_Pices,
#                 cause_for_maintenance=cause_for_maintenance,
#                 item_to_be_maintained=item_to_be_maintained,
#                 spare_item=spare_item,
#                 Main_warehouse=Main_warehouse,
#                 department=department,
#                 return_date=return_date,
#                 user=user
#             )
#             new_main.save()
#             messages.info(request, "Maintainable item in place")
#             # return redirect('create_MaintainableItem')
#     else:
#         maintainableItemForm()
#         if request.POST.get('update_main_id'):
#             # Update maintainable items
#             maintainable_id = request.POST['update_main_id']
#             try:
#                 main = maintainableItem.objects.get(id=maintainable_id)
#                 main.is_set = is_set
#                 main.is_spare = is_spare
#                 main.maintenance_item_set = maintenance_item_set
#                 main.maintenance_item_Pices = maintenance_item_Pices
#                 main.cause_for_maintenance = cause_for_maintenance
#                 main.item_to_be_maintained.add(item_to_be_maintained)
#                 main.department.add(department)
#                 main.spare_item.add(spare_item)
#                 main.Main_warehouse.add(Main_warehouse)
#                 main.return_date = return_date
#                 main.user = user
#                 main.save()
#                 messages.info(request, 'Maintainable item updated')
#             except maintainableItem.DoesNotExist:
#                 messages.error(request, "Maintainable Item not found")
#         elif request.POST.get('delete_main_id'):
#             # Delete maintainable item
#             maintainable_id = request.POST['delete_main_id']
#             try:
#                 main = maintainableItem.objects.get(id=maintainable_id)
#                 main.delete()
#                 messages.info(request, 'Maintainable item deleted')
#             except maintainableItem.DoesNotExist:
#                 messages.error(
#                     request, 'Maintainable item not found for deleting')
#     new_maintainable_item = maintainableItemForm()
#     context = {'new_maintainable_item': new_maintainable_item}
#     return render(request, 'ims/test.html', context)


# def create_remaintaince(request):
#     if request.method == 'POST':
#         re_maintainable_item = returnedMaintainaceItemForm(request.POST)
#         if re_maintainable_item.is_valid():
#             returned_item = re_maintainable_item.cleaned_data['item_name']
#             item_brand = re_maintainable_item.cleaned_data['item_brand']
#             item_serial_number = re_maintainable_item.cleaned_data['item_serial_number']
#             item_barcode = re_maintainable_item.cleaned_data['item_barcode']
#             maintenance_item_Pices = re_maintainable_item.cleaned_data['maintenance_item_Pices']
#             return_date = re_maintainable_item.cleaned_data['return_date']
#             main_department = re_maintainable_item.cleaned_data['department']
#             maintain_ware = re_maintainable_item['Main_warehouse']
#             user = request.user

#             try:
#                 Main_warehouse = wareHouse.objects.get(
#                     wareHouse_name=maintain_ware)
#                 department = Department.objects.get(
#                     department_name=main_department)
#             except wareHouse.DoesNotExist:
#                 messages.error(request, "warehouse not found")
#                 return redirect(create_remaintaince)
#             except Department.DoesNotExist:
#                 messages.error(request, "Department not found")
#                 return redirect(create_remaintaince)
#             if returnedMaintainaceItem.objects.filter(returned_item=returned_item, item_brand=item_brand, item_serial_number=item_serial_number).exists():
#                 messages.info(
#                     request, "This Item already returned from maintainance!!")
#                 return redirect(create_remaintaince)
#             re_main = returnedMaintainaceItem(
#                 returned_item=returned_item,
#                 item_brand=item_brand,
#                 item_serial_number=item_serial_number,
#                 item_barcode=item_barcode,
#                 maintenance_item_Pices=maintenance_item_Pices,
#                 return_date=return_date,
#                 Main_warehouse=Main_warehouse,
#                 department=department,
#                 user=user
#             )
#             re_main.save()
#         else:
#             returnedMaintainaceItemForm()
#         if request.POST.get('update_remain_id'):
#             # Update maintainable items
#             re_maintainable_id = request.POST['update_remain_id']
#             try:
#                 re_main = returnedMaintainaceItem.objects.get(
#                     id=re_maintainable_id)
#                 re_main.item_name = returned_item
#                 re_main.item_brand = item_brand
#                 re_main.item_barcode = item_barcode
#                 re_main.item_serial_number = item_serial_number
#                 re_main.department.add(department)
#                 re_main.Main_warehouse.add(Main_warehouse)
#                 re_main.return_date = return_date
#                 re_main.user = user
#                 re_main.save()
#                 messages.info(request, 'Maintainable item updated')
#             except returnedMaintainaceItem.DoesNotExist:
#                 messages.error(request, "Maintainable Item not found")
#         elif request.POST.get('delete_main_id'):
#             # Delete maintainable item
#             re_maintainable_id = request.POST['delete_re_main_id']
#             try:
#                 main = returnedMaintainaceItem.objects.get(
#                     id=re_maintainable_id)
#                 main.delete()
#                 messages.info(request, ' Returned Maintainable item deleted')
#             except returnedMaintainaceItem.DoesNotExist:
#                 messages.error(
#                     request, ' returned Maintainable item not found for deleting')
#     re_maintainable_item = returnedMaintainaceItemForm()
#     context = {'re_maintainable_item': re_maintainable_item}
#     return render(request, 'ims/test.html', context)

# # create damGED    ONLY-------------------- issue must be solved is_spare, item_to_be_maintained, spare_item


# def createDamagedItem(request):
#     new_damaged = None
#     if request.method == 'POST':
#         new_damaged = DamagedItemForm(request.POST)
#         if new_damaged.is_valid():
#             is_spare = new_damaged.cleaned_data['is_spare']
#             Damaged_spareitem = new_damaged.cleaned_data['spare_item']
#             damged_item = new_damaged.cleaned_data['item_damaged']
#             damaged_department = new_damaged.cleaned_data['department']
#             damaged_item_Pices = new_damaged.cleaned_data['damaged_item_Pices']
#             cause_for_damage = new_damaged.cleaned_data['cause_for_damage']
#             user = request.user
#             try:
#                 item_damaged = item.objects.get(item_name=damged_item)
#                 department = Department.objects.get(
#                     department_name=damaged_department)
#                 spare_item = spareItem.objects.get(
#                     spare_name=Damaged_spareitem)
#             except item.DoesNotExist:
#                 messages.error(request, "Item not found")
#                 return redirect('create_DamagedItem')
#             except spareItem.DoesNotExist:
#                 messages.error(request, " Spare Item not found")
#                 return redirect('create_DamagedItem')
#             except Department.DoesNotExist:
#                 messages.error(request, "Department not found")
#                 return redirect('create_DamagedItem')
#             if damagedItem.objects.filter(item_damaged=item_damaged, spare_item=spare_item).exists():
#                 messages.error(request, "Damaged  Item already in place!!")
#                 return redirect(createDamagedItem)
#             newDamaged = damagedItem(
#                 is_spare=is_spare,
#                 spare_item=spare_item,
#                 item_damaged=item_damaged,
#                 department=department,
#                 damaged_item_Pices=damaged_item_Pices,
#                 cause_for_damage=cause_for_damage,
#                 user=user
#             )
#             newDamaged.save()
#             messages.info(request, "Damaged is registered")
#     else:
#         DamagedItemForm()
#         if request.POST.get('delete_dam_id'):
#             # Delete damaged item
#             damged_id = request.POST['delete_dam_id']
#             try:
#                 dam = damagedItem.objects.get(id=damged_id)
#                 dam.delete()
#             except damagedItem.DoesNotExist:
#                 messages.error(request, "Damaged to be deleted not found")
#     new_damaged = DamagedItemForm()
#     context = {'new_damaged': new_damaged}
#     return render(request, 'ims/test.html', context)

# # CREATE, UPDATE AND DELETE THRESHOLD


# def createThresholdItems(request):
#     stockItems = None
#     if request.method == 'POST':
#         stockItems = thresholdItemsForms(request.POST)
#         if stockItems.is_valid():
#             High_stock_level = stockItems.cleaned_data['High_stock_level']
#             low_stock_level = stockItems.cleaned_data['low_stock_level']
#             Threshold_dept = stockItems.cleaned_data['department']
#             Threshold_spare = stockItems.cleaned_data['spare_item']
#             Thre_item_grp = stockItems.cleaned_data['threshold_item']
#             user = request.user
#             try:
#                 department = Department.objects.get(
#                     department_name=Threshold_dept)
#                 spare_item = spareItem.objects.get(spare_name=Threshold_spare)
#                 threshold_item = itemGroup.objects.get(
#                     group_name=Thre_item_grp)
#             except Department.DoesNotExist:
#                 messages.error(request, "Department not found")
#                 return redirect('create_ThresholdItems')
#             except spareItem.DoesNotExist:
#                 messages.error(request, "Spare Item not found")
#                 return redirect('create_ThresholdItems')
#             except item.DoesNotExist:
#                 messages.error(request, "Item group not found")
#                 return redirect('create_ThresholdItems')
#             if thresholdItems.objects.filter(spare_item=spare_item, threshold_item=threshold_item).exists():
#                 messages.info(request, "Thershold  Item already in place!!")
#                 return redirect('create_ThresholdItems')
#             new_threshold = thresholdItems(
#                 High_stock_level=High_stock_level,
#                 low_stock_level=low_stock_level,
#                 department=department,
#                 spare_item=spare_item,
#                 threshold_item=threshold_item,
#                 user=user
#             )
#             new_threshold.save()
#     else:
#         thresholdItemsForms()
#         if request.POST.get('update_thre_id'):
#             # update threshold items
#             thre_id = request.POST['update_thre_id']
#             try:
#                 thre = thresholdItems.objects.get(id=thre_id)
#                 thre.High_stock_level = High_stock_level
#                 thre.low_stock_level = low_stock_level
#                 thre.department.add(department)
#                 thre.spare_item.add(spare_item)
#                 thre.threshold_item.add(threshold_item)
#                 thre.user = user
#                 thre.save()
#                 messages.info(request, "Threshold Item Updated")
#             except thresholdItems.DoesNotExist:
#                 messages.error(request, "Threshold to be  Item not found")
#         elif request.POST.get('delete_thre_id'):
#             # Delete Threshold item
#             thre_id = request.POST['delete_thre_id']
#             try:
#                 thre = thresholdItems.objects.get(id=thre_id)
#                 thre.delete()
#                 messages.info(request, 'Threshold item deleted')
#             except thresholdItems.DoesNotExist:
#                 messages.error(
#                     request, 'Threshold item not found for deleting')
#     stockItems = thresholdItemsForms()
#     context = {'stockItems': stockItems}
#     return render(request, 'ims/test.html', context)
