from django.urls import path, include
from .views import *
from . import views

from django.conf import settings
from django.urls import path
from ims.REST.API import *

urlpatterns = [

    # path('create-category/', views.newCategory, name='create_category'),
    # path('create-warehouse/', views.createWareHouse, name='create_warehouse'),
    # path('create-sapreItem/', views.createSapreItem, name='create_sapreItem'),
    #     path('create-CrossDock/', views.createCrossDock, name='create_CrossDock'),
    #     path('ordering-personnel/', views.ordering_personnel,
    #          name='ordering_personnel'),
    #     path('create-MaintainbaleItem/', views.createMaintainableItem,
    #          name='create_MaintainbaleItem'),
    #     path('create-DamagedItem/', views.createDamagedItem,
    #          name='create_DamagedItem'),
    #     path('create-ThresholdItems/', views.createThresholdItems,
    #          name='create_ThresholdItems'),



    # -------------------------------------------------------------------------------------------------------
    # Permission

    # get all permissions     ---  allpermissions
    path('allpermissions/', allpermissions, name='allpermissions'),


    # -------------------------------------------------------------------------------------------------------
    # Group

    # get user group (all data)      ---  usergroupsalldata
    path('usergroupsalldata/', user_groups_all_data, name='usergroupsalldata'),

    # get specific group data    (using id)          ---  usergroupdata/<str:pk>/
    path('usergroupdata/<str:pk>/', usergroupdata, name='usergroupdata'),

    # create user group (with permission)    ---  createUserGroup
    path('createUserGroup/', createUserGroup, name='createUserGroup'),

    # update specific group permission (using id)  --- updateGroup/<str:pk>/
    path('updateGroup/<str:pk>/', updateGroup, name='updateGroup'),




    # -------------------------------------------------------------------------------------------------------
    # department

    # get department (all data)    --- departments
    path('departments/', allDapartment, name='departmentdetails'),

    # get department (with id)     ---  getdepartment/<str:pk>/
    path('getdepartment/<str:pk>/', getDapartment, name='getdepartment'),

    # create department using (login user id)     ---  createdepartment
    path('createdepartment/', createDepartment, name='createdepartment'),

    # update department name and descriptions (using id)    ---  updatedepartment/<str:pk>/
    path('updatedepartment/<str:pk>/', updateDepartment, name='updatedepartment'),




    # -------------------------------------------------------------------------------------------------------
    # user

    # get user (all data)     ---  users
    path('users/', allUsers, name='users'),

    # get specific user (using id) ---  user/<str:pk>/
    path('user/<str:pk>/', getuser, name='getuser'),

    # User update their dark_mood (using id)  --- updateUserInfo/<str:pk>/
    path('updateUserInfo/<str:pk>/', updateUserInfo, name='updateUserInfo'),

    # update or assign user group  ---  assignUserToGroup/<str:pk>/
    path('assignUserToGroup/<str:pk>/',
         assignUserToGroup, name='assignUserToGroup'),

    # User change password (using id)
    path('changePassword/<str:pk>/', userchangepassword, name='changepassword'),

    # admin update their users info only password (using id)    --- updateUserInfobyadmin/<str:pk>/
    path('updateUserInfobyadmin/<str:pk>/',
         updateUserInfobyadmin, name='updateUserInfobyadmin'),

    # create admin user account (only superuser)  ---  createUserAccount
    path('createUserAccount/', createUserAccountbySU, name='createUserAccount'),

    # createSuperUserAccount is_superuser and ALL (only superuser)    ---  createSupreUserAccount
    path('createSupreUserAccount/', createSupreUserAccountbySU,
         name='createSupreUserAccount'),

    # User delete/deactivate account (using id)  ---  deleteAccount/<str:pk>/
    path('deleteAccount/<str:pk>/', userdeactivate, name='deleteaccount'),

    # filter user by department (using dep id)   ---  userDepartment/<str:pk>/
    path('userDepartment/<str:pk>/', userDepartment, name='userDepartment'),



    # -------------------------------------------------------------------------------------------------------
    # category

    # get all category ---   categories/
    path('categories/', all_Category, name='all_category'),

    # get specific category (using id)  ---     category/<str:pk>/
    path('category/<str:pk>/', Category, name='single_category'),

    # create category   ---     createcategory/
    path('createcategory/', create_category, name='create_category'),

    # update category name and descriptions          ---  updatecategory/<str:pk>/
    path('updatecategory/<str:pk>/', update_category, name='update_category'),

    # filter category by login user               --- userCategory/<str:pk>/
    path('userCategory/', filterUserCategory, name='userCategory'),



    # -------------------------------------------------------------------------------------------------------
    # ItemGroup

    # get all itemGroup data    ---     itemGroups/
    path('itemGroups/', all_itemGroup, name='Groupdetails'),

    # get single item group data    --- itemGroup/<str:pk>/
    path('itemGroup/<str:pk>/', single_itemGroup, name='Groupdetails'),

    # create new itemGroup   -----  createitemGroup/
    path('createitemGroup/', create_itemGroup, name='CreateGroup'),

    # update itemGroup details (using id)     --- updateItemgroup/<str:pk>/
    path('updateitemGroup/<str:pk>/', update_itemGroup, name='updateitemGroup'),





    # -------------------------------------------------------------------------------------------------------
    # spareGroup

    # get all spareGroup data    ---     spareGroups/
    path('spareGroups/', all_spareGroup, name='spareGroupdetails'),

    # get single spare group data    --- spareGroup/<str:pk>/
    path('spareGroup/<str:pk>/', single_spareGroup, name='spareGroupdetails'),

    # create new spareGroup   -----  createspareGroup/
    path('createspareGroup/', create_spareGroup, name='CreatespareGroup'),

    # update spareGroup details (using id)     --- updatespareGroup/<str:pk>/
    path('updatespareGroup/<str:pk>/',
         update_spareGroup, name='updatespareGroup'),



    # -------------------------------------------------------------------------------------------------------
    # warehouse

    # get all WareHouses data    ---     wareHouses/
    path('wareHouses/', all_wareHouse, name='warehouse-detail'),

    # get specific WareHouses data    ---     wareHouse/<str:pk>/
    path('wareHouse/<str:pk>/', single_wareHouse, name='single-warehoue'),

    # create new Warehouses                ----     createWareHouse/
    path('createwareHouse/', create_warehouse, name='create-warehouse'),

    # update Warehouses details (using id)        --- updatewareHouses/<str:pk>/
    path('updatewareHouses/<str:pk>/', update_warehouse, name='update-warehouse'),

    # filter warehouse by login user department         --- userWarehouse/
    path('userWarehouse/', filterUserWarehouse, name='user-Warehouse'),






    # -------------------------------------------------------------------------------------------------------

    # threshold items
    # get all ThresholdItems data    ---     thresholdItems/
    path('thresholdItems/', all_threshold, name='thresholdItems_detail'),

    # get specific ThresholdItems data    ---     thresholdItem/<str:pk>/
    path('thresholdItem/<str:pk>/', threshold, name='get_thresholdItem_detail'),

    # create / set Low ThresholdItems         ---     LowStockthresholditemgroup/
    path('LowStockthresholditemgroup/', create_Low_thresholditemgroup,
         name='LowStockthresholditemgroup/'),

    # create / set High ThresholdItems         ---     HighStockthresholditemgroup/
    path('HighStockthresholditemgroup/', create_High_thresholditemgroup,
         name='HighStockthresholditemgroup/'),


    # delete / set Low ThresholdItems (using id)  ---     deleteLowStockThresholdItem/<str:pk>/

    path('deleteLowStockThresholdItem/<str:pk>/',
         delete_Low_thresholditemgroup, name='delete_LowStock_ThresholdItem'),


    # delete / set High ThresholdItems (using id)  ---    deleteHighStockThresholdItem/<str:pk>/
    path('deleteHighStockThresholdItem/<str:pk>/',
         delete_High_thresholditemgroup, name='delete_HighStock_ThresholdItem'),

    # create / set Low spareThreshold         ---     LowStocksparethreshold/
    path('LowStocksparethreshold/', create_Low_spareThreshold,
         name='LowStock_sparethreshold/'),

    # create / set High spareThreshold        ---     HighStocksparethreshold/
    path('HighStocksparethreshold/', create_High_spareThreshold,
         name='HighStock_sparethreshold/'),

    # delete Low Spare Threshold (using id)   ---     deleteLowStockspareThreshold/<str:pk>/
    path('deleteLowStockspareThreshold/<str:pk>/',
         delete_Low_sparethreshold, name='delete_LowStock_spareThreshold'),

    # delete High Spare Threshold (using id)  ---    deleteHighStockspareThreshold/<str:pk>/
    path('deleteHighStockspareThreshold/<str:pk>/',
         delete_High_sparethreshold, name='delete_HighStock_spareThreshold'),





    # -------------------------------------------------------------------------------------------------------
    # cross docks
    # get all CrossDocks data    ---     crossdocks/
    path('CrossDocks/', all_CrossDock, name='CrossDock_detail'),

    # get specific CrossDocks data    ---     CrossDock/<str:pk>/
    path('CrossDock/<str:pk>/', single_CrossDock, name='one_CrossDock_detail'),

    path('cretaecrossdock/', create_CrossDock, name='create_crossdock'),


#----------------------------------------------------------------
# item
# get all items --------------items/
 path('items/', all_items, name='all_item_detail'),
# get single items --------------single_item/
 path('singleitem/<str:pk>/', single_item, name='get_single_item'),
# create item pices -------------------- cretaeItemPices/
path('createitempices/', create_Item_pices, name='create_Item_pices'),
# create item set -------------------- cretaeItemSet/
path('createItemSet/', create_Item_set, name='create_Item_set'),
# update item pices -------------------- cretaeItemPices/
path('updateitempices/<str:pk>/', update_Item_pices, name='update_Item_pices'),
]
