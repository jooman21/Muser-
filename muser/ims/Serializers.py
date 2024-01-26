from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *
from accounts.models import User, Group, Department
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


user = get_user_model(),


# permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')

# group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'permissions')


class updateuserGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


# user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active',
                  'department_id', 'date_joined', 'groups', 'user_permissions', 'admin_name', 'Phone_number', 'password')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active',
                  'department', 'date_joined', 'groups', 'admin_name', 'Phone_number')


class UserUpdateinfoSerializer(serializers.ModelSerializer):
    dark_mood = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('dark_mode',)


class AdminUpdateUserPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('password',)

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return make_password(value)


class CreateNewUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    department_id = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    Phone_number = serializers.CharField(required=True)
    is_staff = serializers.BooleanField(required=True)
    is_active = serializers.BooleanField(required=True)
    admin_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'Phone_number', 'department_id', 'password', 'is_staff', 'is_active', 'admin_name')

    def validate(self, data):
        # Check if the request user is in the database
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError(
                'User with this username already exists.')

        # Check if the username is not empty
        if not data['username']:
            raise serializers.ValidationError('Username cannot be empty.')

        if not data['admin_name']:
            raise serializers.ValidationError('admin name cannot be empty.')
        # Check if the phone number is not empty
        if not data['Phone_number']:
            raise serializers.ValidationError('Phone number cannot be empty.')

        # Check if the email is correctly filled
        if not data['email']:
            raise serializers.ValidationError('Email cannot be empty.')

        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        data['password'] = make_password(data['password'])

        return data


class CreateNewSuperUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    department_id = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    Phone_number = serializers.CharField(required=True)
    is_superuser = serializers.BooleanField(required=True)
    is_staff = serializers.BooleanField(required=True)
    is_active = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'Phone_number',
                  'department_id', 'password', 'is_staff', 'is_active', 'is_superuser')

    def validate(self, data):
        # Check if the request user is in the database
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError(
                'User with this username already exists.')

        # Check if the username is not empty
        if not data['username']:
            raise serializers.ValidationError('Username cannot be empty.')

        # Check if the phone number is not empty
        if not data['Phone_number']:
            raise serializers.ValidationError('Phone number cannot be empty.')

        # Check if is_staff, is_active, and is_superuser are all True
        if not all([data['is_staff'], data['is_active'], data['is_superuser']]):
            raise serializers.ValidationError(
                'is_staff, is_active, and is_superuser must be True.')

        # Check if the email is correctly filled
        if not data['email']:
            raise serializers.ValidationError('Email cannot be empty.')

        # Additional password validation
        try:
            validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        # Hash the password before saving
        data['password'] = make_password(data['password'])

        return data


class DeactivateUserAccount(serializers.ModelSerializer):
    is_superuser = serializers.BooleanField(required=True)
    is_staff = serializers.BooleanField(required=True)
    is_active = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('is_superuser', 'is_staff', 'is_active')


# Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_name', 'description')


class DepartmentUserSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'department_name', 'users']


# category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('category_name', 'category_department', 'description')


class updateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('category_name', 'description')


# itemGroup
class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemGroup
        fields = '__all__'


class UpdateItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemGroup
        fields = ('group_name', 'group_category')


# spareGroup
class spareGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = spareGroup
        fields = '__all__'


class UpdatespareGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = spareGroup
        fields = ('sparegroup_name', 'sparegroup_category')


# Warehouse
class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = wareHouse
        fields = '__all__'


class UpdateWareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = wareHouse
        fields = ('warehouse_location', 'wareHouse_name')


# thresholdItems
class thresholdItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = thresholdItems
        fields = '__all__'


class CreateLowStockthresholdItemsgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = thresholdItems
        fields = ('low_stock_level', 'department', 'itemsGroup_threshold')


class CreateHighStockthresholdItemsgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = thresholdItems
        fields = ('High_stock_level', 'department', 'itemsGroup_threshold')

# threshold Spare


class CreateLowthresholdSpareSerializer(serializers.ModelSerializer):
    class Meta:
        model = thresholdItems
        fields = ('low_stock_level', 'department', 'spare_item_group')


class CreateHighthresholdSpareSerializer(serializers.ModelSerializer):
    class Meta:
        model = thresholdItems
        fields = ('High_stock_level', 'department', 'spare_item_group')


# crossDock
class CrossDockSerializer(serializers.ModelSerializer):
    class Meta:
        model = crossDock
        fields = '__all__'

# item
class itemSerializer(serializers.ModelSerializer):
   class Meta:
        model =item
        fields = '__all__'

class ItemPiceSerializer(serializers.ModelSerializer):
   class Meta:
        model =item
        fields = ('item_name','item_brand','item_serial_number','item_barcode','item_import_date','description','group', 'user','department','item_warehouse')


class ItemSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ('item_name','item_brand','item_serial_number','item_barcode','is_set', 'subsets','item_import_date','description','group', 'user','department','item_warehouse')




class SpareItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = spareItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = ('id', 'item_name', 'item_brand',
                  'item_serial_number', 'item_barcode')


class orderPersonnelSerializer(serializers.ModelSerializer):
    item = OrderItemSerializer()

    class Meta:
        model = takeoutOrders
        fields = '__all__'


class MaintainableItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = maintainableItem
        fields = '__all__'


class DamagedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = damagedItem
        fields = '__all__'
