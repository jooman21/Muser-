from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ims.Serializers import *
from ims.forms import *
from accounts.forms import *
import hashlib

# # String to be hashed
# my_string = "Hello, World!"

# # Create an MD5 hash object
# hash_object = hashlib.md5()

# # Update the hash object with the bytes-like object (encoded string)
# hash_object.update(my_string.encode())

# # Get the hexadecimal representation of the hash
# hashed_string = hash_object.hexdigest()

# Print the result
# print("Original String:", my_string)
# print("MD5 Hash:", hashed_string)



from django.shortcuts import get_object_or_404

# use ---------------
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# ------------------------


@api_view(['GET'])  # get all permissions     ---     allpermissions
def allpermissions(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:

            perm = Permission.objects.all()
            serializer = PermissionSerializer(perm, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        empty_msg = "Invalid request"
        return Response({'error': empty_msg}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])  # get user group (all data)     ---     usergroupsalldata
def user_groups_all_data(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            if Group.objects.all().exists():
                groups = Group.objects.all()
                serializer = GroupSerializer(groups, many=True)
                return Response(serializer.data)
            else:
                empty_msg = "No data available."
                return Response({'error': empty_msg}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# get user group detail (using id)     ---     usergroupdata/<str:pk>/
@api_view(['GET'])
def usergroupdata(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:

            if not Group.objects.filter(id=pk).exists():
                empty_msg = "No data available."
                return Response({'error': empty_msg}, status=status.HTTP_404_NOT_FOUND)
            elif Group.objects.get(id=pk):
                group = Group.objects.get(id=pk)
                serializer = GroupSerializer(group, many=False)
                return Response(serializer.data)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        empty_msg = "No data available."
        return Response({'error': empty_msg}, status=status.HTTP_404_NOT_FOUND)


# create user group (with permission)    ---   createUserGroup
@api_view(['POST'])
def createUserGroup(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:

            name = request.data.get('name')
            if Group.objects.filter(name=name).exists():
                return Response({'detail': 'Group Already Exists!!'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = GroupCreationSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    empty_msg = "Invalid inputs. Check your form"
                    return Response({'error': empty_msg}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# update specific group permission (using id)  --- updateGroup/<str:pk>/
@api_view(['PATCH'])
def updateGroup(request, pk):
    if request.method == 'PATCH':
        if request.user.is_authenticated and request.user.is_superuser:
            name = request.data.get('name')
            perm = request.data.get('permissions')

            try:
                group = Group.objects.get(id=pk)
                if group.name == name:

                    serializer = GroupCreationSerializer(
                        group, data=request.data)
                    if serializer.is_valid():
                        group.permissions.set(perm)
                        group.save()
                        return Response({'success': 'Group updated successfully.'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'error': 'Could not update group, check your form'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'error': 'Unknown Group.'}, status=status.HTTP_404_NOT_FOUND)

            except Group.DoesNotExist:
                return Response({'error': 'Group does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# -------------------------------------------------------------------------------------------------------

# department


@api_view(['GET'])  # get department (with id)  --- departments/<str:pk>/
def getDapartment(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_staff:
            if Department.objects.filter(id=pk).exists():
                dep = Department.objects.get(pk=pk)
                serializer = DepartmentSerializer(dep, many=False)
                return Response(serializer.data)
            else:
                return Response({'error': 'Unknown Department'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])    # get department (all data)  --- departments
def allDapartment(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_staff:
            try:
                dep = Department.objects.all()
                serializer = DepartmentSerializer(dep, many=True)
                return Response(serializer.data)

            except Department.DoesNotExist:
                return Response({'detail': 'Departmen doesnot Exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# create department using (login user id)  --- createdepartment
@api_view(['POST'])
def createDepartment(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:

            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                department_name = serializer.validated_data.get(
                    'department_name')
                user = request.user
                if Department.objects.filter(department_name=department_name).exists():

                    return Response({'detail': 'Department Already Exists!!'}, status=status.HTTP_400_BAD_REQUEST)

                elif User.objects.filter(id=user.id).exists():
                    serializer.save(user=user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'error': 'Invalid method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# update department name (using id)     --- updatedepartment/<str:pk>/
@api_view(['PATCH'])
def updateDepartment(request, pk):
    if request.method == 'PATCH':
        if request.user.is_authenticated and request.user.is_superuser:
            try:
                if Department.objects.filter(id=pk).exists():
                    serializer = DepartmentUpdateSerializer(data=request.data)
                    if serializer.is_valid():
                        department = Department.objects.get(id=pk)
                        department.department_name = serializer.validated_data.get(
                            'department_name')
                        department.description = serializer.validated_data.get(
                            'description')
                        department.save()
                        return Response({'success': 'Department Updated'}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'error': 'Could not update group, check your form'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'error': 'Unknown Department.'}, status=status.HTTP_404_NOT_FOUND)

            except Department.DoesNotExist:
                return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.data)


# -------------------------------------------------------------------------------------------------------

# User


@api_view(['GET'])  # get user (all data) --- users
def allUsers(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            try:
                if User.objects.all().exists():
                    alluser = User.objects.all()
                    serializer = UserSerializer(alluser, many=True)
                    return Response(serializer.data)
                else:
                    empty_msg = "No data available."
                    return Response({'error': empty_msg}, status=status.HTTP_404_NOT_FOUND)
            except User.DoesNotExist:
                return Response({'error': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])  # get specific user (using id)  --- user/<str:pk>/
def getuser(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if User.objects.filter(id=pk).exists():
                    users = User.objects.get(pk=pk)
                    serializer = UserProfileSerializer(users, many=False)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'Unknown User'}, status=status.HTTP_404_NOT_FOUND)
            except User.DoesNotExist:
                return Response({'error': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# User update their dark_mood (using id)  --- updateUserInfo/<str:pk>/
@api_view(['PATCH'])
def updateUserInfo(request, pk):
    if request.method == 'PATCH':
        # authonticate the user before giving access
        if request.user.is_authenticated and request.user.is_superuser:

            try:
                user = User.objects.get(id=pk)

                # Check if the authenticated user is the owner of the profile
                if request.user.id != user.id:
                    return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

                else:
                    serializer = UserUpdateinfoSerializer(
                        instance=user, data=request.data, partial=True)

                    try:
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)

                    except ValidationError as e:
                        # Check if the validation error is related to the password or email field
                        if 'dark_mood' in e.detail:
                            # Take the first error message for password
                            error_msg = e.detail['dark_mood'][0]
                        else:
                            error_msg = 'Could not update user info, check your form'
                    return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# User change password (using id)   ---   userchangepassword/<str:pk>/
@api_view(['PATCH'])
def userchangepassword(request, pk):
    if request.method == 'PATCH':
        # authonticate the user before giving access
        if request.user.is_authenticated and request.user.is_active:
            try:
                user = User.objects.get(id=pk)

                # Check if the authenticated user is the owner of the profile
                if request.user.id == user.id:
                    return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
                # Check if the authenticated username is the same as the user admin_name
                elif request.user.username == user.username:

                    serializer = AdminUpdateUserPasswordSerializer(
                        user, data=request.data, partial=True)

                    try:
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)

                    except ValidationError as e:
                        if 'password' in e.detail:
                            error_msg = e.detail['password'][0]
                        else:
                            error_msg = 'Could not update user info, Check your form'
                    return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Access Denied'}, status=status.HTTP_401_UNAUTHORIZED)

            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# admin update their users info only password (using id)    --- updateUserInfobyadmin/<str:pk>/
@api_view(['PATCH'])
def updateUserInfobyadmin(request, pk):
    if request.method == 'PATCH':
        # authonticate the user before giving access
        if request.user.is_authenticated and request.user.is_staff:

            try:
                user = User.objects.get(id=pk)

                # Check if the authenticated user is the owner of the profile
                if request.user.id == user.id:
                    return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
                # Check if the authenticated username is the same as the user admin_name
                elif request.user.username == user.admin_name:

                    serializer = AdminUpdateUserPasswordSerializer(
                        user, data=request.data, partial=True)

                    try:
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)

                    except ValidationError as e:
                        if 'password' in e.detail:
                            error_msg = e.detail['password'][0]
                        else:
                            error_msg = 'Could not update user info, Check your form'
                    return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Access Denied'}, status=status.HTTP_401_UNAUTHORIZED)

            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

# User delete/deactivate account (using id) --- deleteAccount/<str:pk>/


@api_view(['PATCH'])
def userdeactivate(request, pk):
    if request.method == 'PATCH':
        if request.user.is_authenticated and request.user.is_superuser:
            try:
                user = User.objects.get(id=pk)
                requestUserName = request.user.username
                requestUsersadmin = request.user.admin_name
                # Check if the authenticated user is the owner of the profile
                if request.user.id == user.id:
                    return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
                # Check if the authenticated username is the same as the user admin_name
                elif requestUserName == user.admin_name or requestUsersadmin == user.admin_name:

                    serializer = DeactivateUserAccount(
                        user, data=request.data)

                    try:
                        serializer.is_valid(raise_exception=True)
                        if request.user.is_superuser:
                            serializer.save()
                            return Response({'success': 'User Deactivated'}, status=status.HTTP_200_OK)
                        # return Response(serializer.data, status=status.HTTP_200_OK)

                    except ValidationError as e:
                        error_msg = e.detail
                    return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Access Denied'}, status=status.HTTP_401_UNAUTHORIZED)

            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

# createUserAccount is_active and is_staff (only superuser)   --- createUserAccount


@api_view(['POST'])
def createUserAccountbySU(request):
    # Create a new user by super user
    if request.method == "POST":
        if request.user.is_authenticated and request.user.is_superuser:
            try:
                user = request.user.id
                if User.objects.filter(id=user).exists():
                    serializer = CreateNewUserSerializer(data=request.data)
                    username = request.data.get('username', None)
                    phone = request.data.get('Phone_number', None)

                    if request.user.is_authenticated:
                        if username is None:

                            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

                        elif User.objects.filter(username=username).exists():

                            return Response({"error": "Username already exists"}, status=status.HTTP_409_CONFLICT)
                        elif User.objects.filter(Phone_number=phone).exists():
                            return Response({'error': "Registered Phone Number"}, status=status.HTTP_403_FORBIDDEN)
                        elif serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)

                    else:
                        return Response({"error": "Unknown User"}, status=status.HTTP_403_FORBIDDEN)

                else:
                    return Response({"error": "Unknown User"}, status=status.HTTP_403_FORBIDDEN)

            except ValidationError as e:
                # Check if the validation error is related to the password, email, department_id, Phone_number, or username field
                field_errors = ['password', 'email', 'department_id',
                                'Phone_number', 'username', 'admin_name']
                for field in field_errors:
                    if field in e.detail:
                        error_msg = e.detail[field][0]
                        return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)

                print("Exception in creating user", e)
                return Response({'error': 'Could not create user, check your form'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'error': 'Unauthorized Request'}, status=status.HTTP_403_FORBIDDEN)


# createSuperUserAccount is_superuser and ALL (only superuser)   --- createSupreUserAccount
@api_view(['POST'])
def createSupreUserAccountbySU(request):
    # Create a new user by super user
    if request.method == "POST":
        if request.user.is_authenticated and request.user.is_superuser:

            try:
                user = request.user.id
                if User.objects.filter(id=user).exists():
                    serializer = CreateNewSuperUserSerializer(
                        data=request.data)
                    username = request.data.get('username', None)

                    if request.user.is_authenticated:
                        if username is None:
                            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)
                        elif User.objects.filter(username=username).exists():
                            return Response({"error": "Username already exists"}, status=status.HTTP_409_CONFLICT)

                        elif serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)

                    else:
                        return Response({"error": "Unknown User"}, status=status.HTTP_403_FORBIDDEN)

                else:
                    return Response({"error": "Unknown User"}, status=status.HTTP_403_FORBIDDEN)

            except ValidationError as e:
                # Check if the validation error is related to the password, email, department_id, Phone_number, or username field
                field_errors = ['password', 'email',
                                'department_id', 'Phone_number', 'username']
                for field in field_errors:
                    if field in e.detail:
                        error_msg = e.detail[field][0]
                        return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)

                print("Exception in creating user", e)
                return Response({'error': 'Could not create user, check your form'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'error': 'Unauthorized Request'}, status=status.HTTP_403_FORBIDDEN)


# update or assign user group  ---  assignUserToGroup/<str:pk>/
@api_view(['POST'])
def assignUserToGroup(request, pk):
    if request.method == "POST":

        if request.user.is_authenticated and request.user.is_superuser:

            if Group.objects.filter(id=pk).exists():
                group = Group.objects.get(id=pk)
                # group_serializer = updateuserGroupSerializer(group)

                username = request.data.get('username', None)

                if not username:
                    return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    user = User.objects.get(username=username)

                    # Clear user's existing groups
                    user.groups.clear()

                    # Assign user to the new group
                    group.user_set.add(user)

                    # user.groups.add(group)  # Add user to the group

                    return Response({'Success': f'the user {username}, is assigned to {group} role.'}, status=status.HTTP_200_OK)

                except User.DoesNotExist:
                    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


# filter user by department (using id)  --- userDepartment/<str:pk>/
@api_view(['GET'])
def userDepartment(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_superuser:
            try:
                department = Department.objects.get(id=pk)
                users = User.objects.filter(department=department)
                if not users.exists():
                    return Response({'message': 'Department has no users'}, status=status.HTTP_200_OK)
                else:
                    # Serialize the department and users
                    department_serializer = DepartmentUserSerializer(
                        department)
                    user_serializer = UserSerializer(users, many=True)

                    response_data = {
                        'department': department_serializer.data,
                        'users': user_serializer.data,
                    }

                    return Response(response_data, status=status.HTTP_200_OK)

            except Department.DoesNotExist:
                return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


# -------------------------------------------------------------------------------------------------------

# category


# permission required
# get all category --- categories/
@api_view(['GET'])
def all_Category(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if category.objects.exists():
                    categorys = category.objects.all()
                    serializer = CategorySerializer(categorys, many=True)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No record found'}, status=status.HTTP_404_NOT_FOUND)
            except category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


# permission required
# get specific category (using id)  ---     category/<str:pk>/
@api_view(['GET'])
def Category(request, pk):
    if request.user.is_authenticated and request.user.is_active:
        try:
            if category.objects.exists() and category.objects.filter(id=pk).exists():

                categorys = category.objects.get(id=pk)
                serializer = CategorySerializer(categorys, many=False)
                return Response(serializer.data)
            else:
                return Response({'error': 'No record found'}, status=status.HTTP_404_NOT_FOUND)
        except category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


# permission required
# create category   ---     createcategory/
@api_view(['POST'])
def create_category(request):
    if request.method == 'POST':
        department = request.data.get('category_department')
        if Department.objects.exists() and Department.objects.filter(id=department).exists():
            try:
                if not request.user.is_authenticated:
                    return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
                elif not request.user.is_staff:
                    return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)

                serializer = CreateCategorySerializer(
                    data=request.data, partial=True)

                name = request.data.get('category_name')

                if category.objects.filter(category_name=name).exists():
                    return Response({'detail': 'Category Already Exists!!'}, status=status.HTTP_403_FORBIDDEN)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except category.DoesNotExist:
                return Response({'error': 'Category Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Method doesnot allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# update category name and descriptions          ---  updatecategory/<str:pk>/
@api_view(['PATCH'])
def update_category(request, pk):
    if request.method == 'PATCH':

        try:
            if not request.user.is_authenticated:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            elif not request.user.is_staff:
                return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)

            if category.objects.filter(id=pk).exists():
                cate = category.objects.get(id=pk)
                serializer = updateCategorySerializer(
                    cate, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Category Doesnot Exists.'}, status=status.HTTP_404_NOT_FOUND)
        except category.DoesNotExist:
            return Response({'detail': 'Category Not Found.'}, status=status.HTTP_404_NOT_FOUND)


# filter category by login user               --- userCategory/<str:pk>/
@api_view(["GET"])
def filterUserCategory(request):
    if request.method == 'GET':

        try:
            if not request.user.is_authenticated:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            elif not request.user.is_staff:
                return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)

            userDep = request.user.department
            if category.objects.filter(category_department=userDep).exists():
                cate = category.objects.filter(category_department=userDep)
                categories = CategorySerializer(cate, many=True)
                return Response(categories.data, status=status.HTTP_200_OK)

            else:
                return Response({'detail': 'No Available Categories are Found'}, status=status.HTTP_404_NOT_FOUND)
        except category.DoesNotExist:
            return Response({'detail': 'Category Not Found.'}, status=status.HTTP_404_NOT_FOUND)


# -------------------------------------------------------------------------------------------------------
# itemGroup

# permission required
# get all itemGroup data                  ---     itemGroups/
@api_view(['GET'])
def all_itemGroup(request):
    if request.method == 'GET':
        try:
            if not request.user.is_authenticated and not request.user.is_active:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if itemGroup.objects.exists():
                grp = itemGroup.objects.all()
                serializer = ItemGroupSerializer(grp, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response({"message": "No Data Available"}, status=status.HTTP_404_NOT_FOUND)
        except itemGroup.DoesNotExist:
            return Response({'detail': 'Item Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Error": "Unknown Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# get single item group data              ---     itemGroup/<str:pk>/
@api_view(['GET'])
def single_itemGroup(request, pk):
    if request.method == 'GET':
        try:
            if not request.user.is_authenticated and not request.user.is_active:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if itemGroup.objects.exists() and itemGroup.objects.filter(id=pk):

                grp = itemGroup.objects.get(id=pk)
                serializer = ItemGroupSerializer(grp, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response({"message": "No Data Available"}, status=status.HTTP_404_NOT_FOUND)
        except itemGroup.DoesNotExist:
            return Response({'detail': 'Item Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Error": "Unknown Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# create new itemGroup                    ---     createitemGroup/
@api_view(['POST'])
def create_itemGroup(request):
    if request.method == 'POST':
        try:
            if not request.user.is_authenticated and not request.user.is_active:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            group_category = request.data.get('group_category', None)
            groupName = request.data.get('group_name', None)

            if itemGroup.objects.filter(group_name=groupName):
                return Response({"message": "This group already exists."}, status=status.HTTP_409_CONFLICT)

            if not category.objects.exists():
                return Response({"message": "Category Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)

            elif category.objects.filter(id=group_category):

                serializer = ItemGroupSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    c = category.objects.get(id=group_category)
                    c.total_groups += 1
                    c.save()

                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"message": "Unknown Category"}, status=status.HTTP_404_NOT_FOUND)

        except itemGroup.DoesNotExist:
            return Response({'detail': 'Item Group does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# update itemGroup details (using id)     ---     updateItemgroup/<str:pk>/
@api_view(['PATCH'])
def update_itemGroup(request, pk):
    if request.method == 'PATCH':
        requested_group_category = request.data.get('group_category', None)
        requested_group_name = request.data.get('group_name', None)

        try:
            if not request.user.is_authenticated or not request.user.is_active:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if itemGroup.objects.filter(id=pk).exists():

                if itemGroup.objects.filter(group_name=requested_group_name, group_category=requested_group_category):
                    return Response({"error": "Duplication errors."}, status=status.HTTP_409_CONFLICT)
                elif not itemGroup.objects.filter(group_category=requested_group_category):
                    return Response({'error': 'Item Group category does not exist'}, status=status.HTTP_404_NOT_FOUND)

                # the itemGroup to be updated
                old_group = itemGroup.objects.get(pk=pk)

                # the group_category from itemGroup to be updated
                old_group_category = old_group.group_category

                # the Itemgroup category id that wil be updated
                old_category_id = old_group_category.id

                serializer = UpdateItemGroupSerializer(
                    old_group, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()

                    # the category ID that the Old ItemGroup is onit
                    old_category_obj = category.objects.get(id=old_category_id)

                    # check the requested data has the itemGroup category and then it is simmilar with the new patched data category
                    if requested_group_category and requested_group_category != old_category_id:

                        # getting the  patched data category ID from the requested data itemGroup
                        new_requested_group_category = itemGroup.objects.get(
                            id=requested_group_category)

                        # getting the category id from new_requested_group_category
                        new_category_obj = category.objects.get(
                            id=new_requested_group_category.id)

                        # Decrease the total_groups in the category table for the old catagory and add up on the new catagory total_groups (by 1)
                        if old_category_obj.total_groups > 0:

                            # updating the  old category total_groups number
                            old_category_obj.total_groups -= 1
                            old_category_obj.save()

                            # updating the new category total_groups number
                            new_category_obj.total_groups += 1
                            new_category_obj.save()

                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"message": "The specified itemGroup was not found."}, status=status.HTTP_404_NOT_FOUND)

        except itemGroup.DoesNotExist:
            return Response({'detail': 'Item Group does not exist'}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response({"Error": "Unknown Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# -------------------------------------------------------------------------------------------------------
# SpareGroup

# permission required
# get all spareGroup data    ---     spareGroups/
@api_view(['GET'])
def all_spareGroup(request):
    if request.method == 'GET':
        try:
            if not request.user.is_authenticated and not request.user.is_active:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if spareGroup.objects.exists():
                grp = spareGroup.objects.all()
                serializer = spareGroupSerializer(grp, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response({"message": "No Data Available"}, status=status.HTTP_404_NOT_FOUND)
        except spareGroup.DoesNotExist:
            return Response({'detail': 'Spare Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Error": "Unknown Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# get single spare group data    --- spareGroup/<str:pk>/
@api_view(['GET'])
def single_spareGroup(request, pk):
    if request.method == 'GET':
        try:
            if not request.user.is_authenticated and not request.user.is_active:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if spareGroup.objects.exists() and spareGroup.objects.filter(id=pk):

                grp = spareGroup.objects.get(id=pk)
                serializer = spareGroupSerializer(grp, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response({"message": "No Data Available"}, status=status.HTTP_404_NOT_FOUND)
        except spareGroup.DoesNotExist:
            return Response({'detail': 'Spare Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Error": "Unknown Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# create new spareGroup                    ---     createspareGroup/
@api_view(['POST'])
def create_spareGroup(request):
    if request.method == 'POST':
        try:
            if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            sparegroup_category = request.data.get('sparegroup_category', None)
            sparegroupname = request.data.get('sparegroup_name', None)

            if spareGroup.objects.filter(sparegroup_name=sparegroupname):
                return Response({"message": "This group already exists."}, status=status.HTTP_409_CONFLICT)

            if not category.objects.exists():
                return Response({"message": "Category Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)

            elif category.objects.filter(id=sparegroup_category):

                serializer = spareGroupSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    c = category.objects.get(id=sparegroup_category)
                    c.total_groups += 1
                    c.save()

                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"message": "Unknown Category"}, status=status.HTTP_404_NOT_FOUND)

        except spareGroup.DoesNotExist:
            return Response({'detail': 'Spare Group does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# permission required
# update spareGroup details (using id)     --- updatespareGroup/<str:pk>/
@api_view(['PATCH'])
def update_spareGroup(request, pk):
    if request.method == 'PATCH':
        requested_group_category = request.data.get(
            'sparegroup_category', None)
        requested_sparegroup_name = request.data.get(
            'sparegroup_name', None)
        try:
            if not request.user.is_authenticated or not request.user.is_active:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if spareGroup.objects.filter(id=pk).exists():

                if spareGroup.objects.filter(sparegroup_name=requested_sparegroup_name, sparegroup_category=requested_group_category):
                    return Response({"error": "Duplication errors."}, status=status.HTTP_409_CONFLICT)
                elif not spareGroup.objects.filter(sparegroup_category=requested_group_category):
                    return Response({'error': 'Spare Group category does not exist'}, status=status.HTTP_404_NOT_FOUND)

                old_group = spareGroup.objects.get(pk=pk)

                old_group_category = old_group.sparegroup_category

                old_category_id = old_group_category.id

                serializer = UpdatespareGroupSerializer(
                    old_group, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()

                    old_category_obj = category.objects.get(id=old_category_id)

                    if requested_group_category and requested_group_category != old_category_id:

                        new_requested_group_category = spareGroup.objects.get(
                            id=requested_group_category)

                        new_category_obj = category.objects.get(
                            id=new_requested_group_category.id)

                        if old_category_obj.total_groups > 0:

                            old_category_obj.total_groups -= 1
                            old_category_obj.save()

                            new_category_obj.total_groups += 1
                            new_category_obj.save()

                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"message": "Spare Item Group not found."}, status=status.HTTP_404_NOT_FOUND)

        except spareGroup.DoesNotExist:
            return Response({'detail': 'Spare Group does not exist'}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response({"Error": "Unknown Request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# -------------------------------------------------------------------------------------------------------

# Warehouse


# Permission required
# get all WareHouses data    ---     wareHouses/
@api_view(['GET'])
def all_wareHouse(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if wareHouse.objects.exists():
                    categorys = wareHouse.objects.all()
                    serializer = WareHouseSerializer(categorys, many=True)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No record found'}, status=status.HTTP_404_NOT_FOUND)
            except wareHouse.DoesNotExist:
                return Response({'error': 'Warehouse not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Unauthorized Method'}, status=status.HTTP_401_UNAUTHORIZED)


# get specific WareHouses data    ---     wareHouse/<str:pk>/
@api_view(['GET'])
def single_wareHouse(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if wareHouse.objects.exists() and wareHouse.objects.filter(id=pk).exists():

                    categorys = wareHouse.objects.get(id=pk)
                    serializer = WareHouseSerializer(categorys, many=False)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No record found'}, status=status.HTTP_404_NOT_FOUND)
            except wareHouse.DoesNotExist:
                return Response({'error': 'Warehouse not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)


# Permission required
# create new Warehouses      ----     createwareHouse/
@api_view(['POST'])
def create_warehouse(request):
    if request.method == 'POST':
        department = request.data.get('department')
        if Department.objects.exists() and Department.objects.filter(id=department).exists():
            try:
                if not request.user.is_authenticated:
                    return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
                elif not request.user.is_staff:
                    return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)

                serializer = WareHouseSerializer(data=request.data)

                name = request.data.get('wareHouse_name')

                if wareHouse.objects.filter(wareHouse_name=name).exists():
                    return Response({'detail': 'Category Already Exists!!'}, status=status.HTTP_403_FORBIDDEN)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except wareHouse.DoesNotExist:
                return Response({'error': 'Warehouse Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Method doesnot allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# update warehouse name and warehouse location          ---  updatewareHouses/<str:pk>/
@api_view(['PATCH'])
def update_warehouse(request, pk):
    if request.method == 'PATCH':
        try:
            if not request.user.is_authenticated:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            elif not request.user.is_staff:
                return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)

            if wareHouse.objects.filter(id=pk).exists():
                warehouse = wareHouse.objects.get(id=pk)
                serializer = UpdateWareHouseSerializer(
                    warehouse, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Warehouse Doesnot Exists.'}, status=status.HTTP_404_NOT_FOUND)
        except wareHouse.DoesNotExist:
            return Response({'detail': 'Warehouse Not Found.'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Method doesnot allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# filter warehouse by login user               --- userWarehouse/<str:pk>/      ****** where to use it
@api_view(["GET"])
def filterUserWarehouse(request):
    if request.method == 'GET':
        try:
            if not request.user.is_authenticated:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            elif not request.user.is_staff:
                return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)

            userDep = request.user.department
            if wareHouse.objects.filter(department=userDep).exists():
                ware = wareHouse.objects.filter(department=userDep)
                warehouses = WareHouseSerializer(ware, many=True)
                return Response(warehouses.data, status=status.HTTP_200_OK)

            else:
                return Response({'detail': 'No Available Warehouse are Found'}, status=status.HTTP_404_NOT_FOUND)
        except wareHouse.DoesNotExist:
            return Response({'detail': 'Warehouse Not Found.'}, status=status.HTTP_404_NOT_FOUND)


# -------------------------------------------------------------------------------------------------------

# Threshold


# permission required
# get all ThresholdItems data    ---     thresholdItems/
@api_view(['GET'])
def all_threshold(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if thresholdItems.objects.exists():
                    thresholds = thresholdItems.objects.all()
                    serializer = thresholdItemsSerializer(
                        thresholds, many=True)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No record found'}, status=status.HTTP_404_NOT_FOUND)
            except thresholdItems.DoesNotExist:
                return Response({'error': 'Threshold itmes not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Access Denied'}, status=status.HTTP_404_NOT_FOUND)


# permission required
# get specific ThresholdItems data    ---     thresholdItem/<str:pk>/
@api_view(['GET'])
def threshold(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if thresholdItems.objects.exists() and thresholdItems.objects.filter(id=pk).exists():

                    categorys = thresholdItems.objects.get(id=pk)
                    serializer = thresholdItemsSerializer(
                        categorys, many=False)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No Record Found'}, status=status.HTTP_404_NOT_FOUND)
            except category.DoesNotExist:
                return Response({'error': 'Threshold Item not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Access Denied'}, status=status.HTTP_404_NOT_FOUND)


# permission required
# create / set Low ThresholdItems         ---     LowStockthresholditemgroup/
@api_view(['POST'])
def create_Low_thresholditemgroup(request):
    if request.method == 'POST':
        department = request.data.get('department')
        if Department.objects.exists() and Department.objects.filter(id=department).exists():
            try:
                if request.user.is_authenticated and request.user.is_staff:

                    serializer = CreateLowStockthresholdItemsgroupSerializer(
                        data=request.data)

                    name = request.data.get('itemsGroup_threshold', None)
                    low_stock = request.data.get('low_stock_level', None)
                    if low_stock == None:
                        return Response({'detail': 'No Defined Low Stock Value'}, status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)

                    if not itemGroup.objects.filter(id=name).exists():
                        return Response({'error': 'ItemGroup Doesnot Exists!!'}, status=status.HTTP_403_FORBIDDEN)

                    if thresholdItems.objects.filter(itemsGroup_threshold=name, low_stock_level__isnull=False).exists():
                        return Response({'detail': 'ItemGroup Already Assigned!'}, status=status.HTTP_403_FORBIDDEN)

                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            except thresholdItems.DoesNotExist:
                return Response({'error': 'Items Group or Spare Parts Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Method doesnot allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# create / set High ThresholdItems         ---     HighStockthresholditemgroup/
@api_view(['POST'])
def create_High_thresholditemgroup(request):
    if request.method == 'POST':
        department = request.data.get('department')
        if Department.objects.exists() and Department.objects.filter(id=department).exists():
            try:
                if request.user.is_authenticated and request.user.is_staff:

                    serializer = CreateHighStockthresholdItemsgroupSerializer(
                        data=request.data)

                    name = request.data.get('itemsGroup_threshold')
                    High_stock = request.data.get('High_stock_level')
                    if High_stock == None:
                        return Response({'detail': 'No Defined High Stock Value'}, status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)

                    if not itemGroup.objects.filter(id=name).exists():
                        return Response({'error': 'ItemGroup Doesnot Exists!!'}, status=status.HTTP_403_FORBIDDEN)

                    if thresholdItems.objects.filter(itemsGroup_threshold=name, High_stock_level__isnull=False).exists():
                        return Response({'detail': 'ItemGroup Already Assigned!'}, status=status.HTTP_403_FORBIDDEN)

                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            except thresholdItems.DoesNotExist:
                return Response({'error': 'Items Group or Spare Parts Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Method doesnot allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# delete Low ThresholdItems (using id)  ---     deleteLowStockThresholdItem/<str:pk>/
# permission required
@api_view(['DELETE'])
def delete_Low_thresholditemgroup(request, pk):
    if request.method == 'DELETE':
        try:

            if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if not thresholdItems.objects.filter(id=pk).exists:
                return Response({'error': 'Threshold Items Not Found'}, status=status.HTTP_404_NOT_FOUND)

            deltresh = thresholdItems.objects.get(id=pk)

            # Ensure that the ThresholdItem matches the specified department, item group, and low stock level
            if (deltresh.department__id != request.data.get('department', None) or
                deltresh.itemsGroup_threshold != request.data.get('itemsGroup_threshold', None) or
                    deltresh.low_stock_level != request.data.get('low_stock_level', None)):
                return Response({'error': 'Threshold Item does not match provided criteria'}, status=status.HTTP_400_BAD_REQUEST)

            deltresh.delete()

            return Response({'detail': 'Item Group Removed'}, status=status.HTTP_204_NO_CONTENT)
        except thresholdItems.DoesNotExist:
            return Response({'detail': 'Threshold Items Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('the exception e', e, '++++++++++++++++++++++')
            return Response({'error': 'An error occurred while deleting the ThresholdItem'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# delete High ThresholdItems (using id)  ---    deleteHighStockThresholdItem/<str:pk>/
# permission required
@api_view(['DELETE'])
def delete_High_thresholditemgroup(request, pk):
    if request.method == 'DELETE':
        try:

            if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if not thresholdItems.objects.filter(id=pk).exists:
                return Response({'error': 'Threshold Items Not Found'}, status=status.HTTP_404_NOT_FOUND)

            deltresh = thresholdItems.objects.get(id=pk)

            # Ensure that the ThresholdItem matches the specified department, item group, and low stock level
            if (deltresh.department__id != request.data.get('department', None) or
                deltresh.itemsGroup_threshold != request.data.get('itemsGroup_threshold', None) or
                    deltresh.High_stock_level != request.data.get('High_stock_level', None)):
                return Response({'error': 'Threshold Item does not match provided criteria'}, status=status.HTTP_400_BAD_REQUEST)

            deltresh.delete()

            return Response({'detail': 'Item Group Removed'}, status=status.HTTP_204_NO_CONTENT)
        except thresholdItems.DoesNotExist:
            return Response({'detail': 'Threshold Items Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('the exception e', e, '++++++++++++++++++++++')
            return Response({'error': 'An error occurred while deleting the ThresholdItem'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# for spare Thresholds

# permission required
# create / set Low spareThreshold         ---     LowStocksparethreshold/
@api_view(['POST'])
def create_Low_spareThreshold(request):
    if request.method == 'POST':
        department = request.data.get('department')
        if Department.objects.exists() and Department.objects.filter(id=department).exists():
            try:
                if request.user.is_authenticated and request.user.is_staff:

                    serializer = CreateLowthresholdSpareSerializer(
                        data=request.data)

                    name = request.data.get('spare_item_group', None)
                    low_stock = request.data.get('low_stock_level', None)
                    if low_stock == None:
                        return Response({'detail': 'No Defined Low Stock Value'}, status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)

                    if not spareGroup.objects.filter(id=name).exists():
                        return Response({'error': 'Spare Group Doesnot Exists!!'}, status=status.HTTP_403_FORBIDDEN)

                    if thresholdItems.objects.filter(spare_item_group=name, low_stock_level__isnull=False).exists():
                        return Response({'detail': 'Spare Group Already Assigned!'}, status=status.HTTP_403_FORBIDDEN)

                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            except thresholdItems.DoesNotExist:
                return Response({'error': 'Items Group or Spare Parts Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Method doesnot allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# permission required
# create / set High spareThreshold        ---     HighStocksparethreshold/
@api_view(['POST'])
def create_High_spareThreshold(request):
    if request.method == 'POST':
        department = request.data.get('department')
        if Department.objects.exists() and Department.objects.filter(id=department).exists():
            try:
                if request.user.is_authenticated and request.user.is_staff:

                    serializer = CreateHighthresholdSpareSerializer(
                        data=request.data)

                    name = request.data.get('spare_item_group')
                    High_stock = request.data.get('High_stock_level')
                    if High_stock == None:
                        return Response({'detail': 'No Defined High Stock Value'}, status=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE)

                    if not spareGroup.objects.filter(id=name).exists():
                        return Response({'error': 'Spare Group Doesnot Exists!!'}, status=status.HTTP_403_FORBIDDEN)

                    if thresholdItems.objects.filter(spare_item_group=name, High_stock_level__isnull=False).exists():
                        return Response({'detail': 'Spare Group Already Assigned!'}, status=status.HTTP_403_FORBIDDEN)

                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            except thresholdItems.DoesNotExist:
                return Response({'error': 'Items Group or Spare Parts Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'detail': 'Method doesnot allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# delete Low Spare Threshold (using id)   ---     deleteLowStockspareThreshold/<str:pk>/
# permission required
@api_view(['DELETE'])
def delete_Low_sparethreshold(request, pk):
    if request.method == 'DELETE':
        try:

            if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if not thresholdItems.objects.filter(id=pk).exists:
                return Response({'error': 'Threshold Items Not Found'}, status=status.HTTP_404_NOT_FOUND)

            deltresh = thresholdItems.objects.get(id=pk)

            # Ensure that the ThresholdItem matches the specified department, item group, and low stock level
            if (deltresh.department__id != request.data.get('department', None) or
                deltresh.spare_item_group != request.data.get('spare_item_group', None) or
                    deltresh.low_stock_level != request.data.get('low_stock_level', None)):
                return Response({'error': 'Threshold Item does not match provided criteria'}, status=status.HTTP_400_BAD_REQUEST)

            deltresh.delete()

            return Response({'detail': 'Spare Group Removed'}, status=status.HTTP_204_NO_CONTENT)
        except thresholdItems.DoesNotExist:
            return Response({'detail': 'Threshold Items Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('the exception e', e, '++++++++++++++++++++++')
            return Response({'error': 'An error occurred while deleting the ThresholdItem'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# delete High Spare Threshold (using id)  ---    deleteHighStockspareThreshold/<str:pk>/
# permission required
@api_view(['DELETE'])
def delete_High_sparethreshold(request, pk):
    if request.method == 'DELETE':
        try:

            if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            if not thresholdItems.objects.filter(id=pk).exists:
                return Response({'error': 'Threshold Items Not Found'}, status=status.HTTP_404_NOT_FOUND)

            deltresh = thresholdItems.objects.get(id=pk)

            # Ensure that the ThresholdItem matches the specified department, item group, and low stock level
            if (deltresh.department__id != request.data.get('department', None) or
                deltresh.spare_item_group != request.data.get('spare_item_group', None) or
                    deltresh.High_stock_level != request.data.get('High_stock_level', None)):
                return Response({'error': 'Threshold Item does not match provided criteria'}, status=status.HTTP_400_BAD_REQUEST)

            deltresh.delete()

            return Response({'detail': 'Item Group Removed'}, status=status.HTTP_204_NO_CONTENT)
        except thresholdItems.DoesNotExist:
            return Response({'detail': 'Threshold Items Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('the exception e', e, '++++++++++++++++++++++')
            return Response({'error': 'An error occurred while deleting the ThresholdItem'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(["GET"])
# def filterUserThreshold(request):
#     if request.method == 'GET':

#         try:
#             if not request.user.is_authenticated:
#                 return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
#             elif not request.user.is_staff:
#                 return Response({'error': 'Unauthorized Access'}, status=status.HTTP_401_UNAUTHORIZED)

#             userDep = request.user.department
#             if thresholdItems.objects.filter(department=userDep).exists():
#                 thre = thresholdItems.objects.filter(department=userDep)
#                 thresholds = thresholdItemsSerializer(thre, many=True)
#                 return Response(thresholds.data, status=status.HTTP_200_OK)

#             else:
#                 return Response({'detail': 'No Available Threshold Items  are Found'}, status=status.HTTP_404_NOT_FOUND)
#         except thresholdItems.DoesNotExist:
#             return Response({'detail': 'Threshold Not Found.'}, status=status.HTTP_404_NOT_FOUND)


# -------------------------------------------------------------------------------------------------------
# Cross dock
@api_view(['GET'])
def all_CrossDock(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if crossDock.objects.exists():
                    categorys = crossDock.objects.all()
                    serializer = CrossDockSerializer(categorys, many=True)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No record found'}, status=status.HTTP_404_NOT_FOUND)
            except crossDock.DoesNotExist:
                return Response({'error': 'Cross Dock not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])  # get single cross dock files
def single_CrossDock(request, pk):
    if request.user.is_authenticated and request.user.is_active:
        try:
            if crossDock.objects.exists() and crossDock.objects.filter(id=pk).exists():

                crossdock = crossDock.objects.get(id=pk)
                serializer = CrossDockSerializer(crossdock, many=False)
                return Response(serializer.data)
            else:
                return Response({'error': 'No record found'}, status=status.HTTP_404_NOT_FOUND)
        except category.DoesNotExist:
            return Response({'error': 'Cross Dock not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_CrossDock(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            department = request.data.get('department')
            warehouse_center = request.data.get('warehouse_center')
            if Department.objects.exists() and Department.objects.filter(id=department).exists():
                if wareHouse.objects.exists() and wareHouse.objects.filter(id=warehouse_center).exists():
                    try:
                        file = request.data.get('file')

                        file_hash = calculate_file_hash(
                            file)  # Calculate the file hash

                        serializer = CrossDockSerializer(
                            data=request.data, partial=True, context={'request': request})

                        if crossDock.objects.filter(file_hash=file_hash).first():
                            return Response({'detail': 'CrossDock File  Already Exists!!'}, status=status.HTTP_403_FORBIDDEN)

                        if serializer.is_valid():
                            serializer.save(file_hash=file_hash)
                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    except crossDock.DoesNotExist:
                        return Response({'error': 'Cross Dock Not Found'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'error': 'Warehouse Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'Department Not Found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'detail': 'Method is not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def calculate_file_hash(file):
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    return md5.hexdigest()


# permission required
# get all items      ------items/
@api_view(['GET'])  
def all_items(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if item.objects.exists() and item.objects.all().exists():

                    items = item.objects.all()
                    serializer = itemSerializer(
                        items, many=True)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No Record Found'}, status=status.HTTP_404_NOT_FOUND)
            except thresholdItems.DoesNotExist:
                return Response({'error': 'Item not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Access Denied'}, status=status.HTTP_404_NOT_FOUND)

# permission required
# get single items     ---------single_item/
@api_view(['GET'])
def single_item(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            try:
                if item.objects.exists() and item.objects.filter(id=pk).exists():

                    items = item.objects.get(id=pk)
                    serializer = itemSerializer(
                        items, many=False)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'No Record Found'}, status=status.HTTP_404_NOT_FOUND)
            except thresholdItems.DoesNotExist:
                return Response({'error': 'Item not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Access Denied'}, status=status.HTTP_404_NOT_FOUND)

# permission required
# create new item  in pices                 ---     cretaeItemPices/
@api_view(['POST'])
def create_Item_pices(request):
    if request.method == 'POST':
        try:
            if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            item_serial_number = request.data.get('item_serial_number', None)
            item_barcode = request.data.get('item_barcode', None)
            group =  request.data.get('group', None)
            item_warehouse = request.data.get('item_warehouse', None)
            department = request.data.get('department', None)
          
         
            if item.objects.filter(item_serial_number=item_serial_number, item_barcode=item_barcode).exists():
                return Response({"message": "Item Already Exists."}, status=status.HTTP_409_CONFLICT)
             
            if not Department.objects.exists() and Department.objects.filter(id=department).exists():
                return Response({"message": "Department Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)
            
            if not itemGroup.objects.exists() and itemGroup.objects.filter(id=group).exists():
                return Response({"message": "iTem Group Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)
            if not wareHouse.objects.exists() and wareHouse.objects.filter(id=item_warehouse).exists():
                return Response({"message": "Item Warehouse Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = ItemPiceSerializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               group_id = request.data.get('group', None) 
            #    print(group_id, "=====================")
               i = itemGroup.objects.get(id=group_id)
               i.totalItem += 1
               i.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except item.DoesNotExist:
            return Response({'detail': 'Item does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# permission required
# create new item   in set(subset)                ---     createItemSet/
@api_view(['POST'])
def create_Item_set(request):
    if request.method == 'POST':
        try:
            if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)

            item_serial_number = request.data.get('item_serial_number', None)
            item_barcode = request.data.get('item_barcode', None)
            group =  request.data.get('group', None)
            item_warehouse = request.data.get('item_warehouse', None)
            department = request.data.get('department', None)
            is_set = request.data.get('is_set', None)
            subsets = request.data.get('subsets', None)

            if item.objects.filter(item_serial_number=item_serial_number, item_barcode=item_barcode).exists():
                return Response({"message": "Item Already Exists."}, status=status.HTTP_409_CONFLICT)
             
            if not Department.objects.exists() and Department.objects.filter(id=department).exists():
                return Response({"message": "Department Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)
            
            if not itemGroup.objects.exists() and itemGroup.objects.filter(id=group).exists():
                return Response({"message": "iTem Group Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)
            if not wareHouse.objects.exists() and wareHouse.objects.filter(id=item_warehouse).exists():
                return Response({"message": "Item Warehouse Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)
            
            if is_set and subsets is not None:
                   serializer = ItemSetSerializer(data=request.data)
                   if serializer.is_valid():
                      serializer.save()
                      group_id = request.data.get('group', None) 
                       #print(group_id, "=====================")
                      i = itemGroup.objects.get(id=group_id)
                      i.totalItem += 1
                      i.save()
                      return Response(serializer.data, status=status.HTTP_201_CREATED)
                   else:
                      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': "List all the subsets"})
        except item.DoesNotExist:
            return Response({'detail': 'Item does not exist'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# permission required
# create new item  in pices                 ---     updateItemPices/
@api_view(['PATCH'])
def update_Item_pices(request, pk):
    if request.method == 'PATCH':
        try:
            if item.objects.filter(id=pk).exists():
              if not request.user.is_authenticated and not request.user.is_staff:
                return Response({'error': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
              serializer = ItemPiceSerializer(data=request.data, partial=True)
              if serializer.is_valid():
                 serializer.save()
                 group_id = request.data.get('group', None) 
                 #print(group_id, "=====================")
                 i = itemGroup.objects.get(id=group_id)
                 i.totalItem -= 1
                 i.save()
                 return Response({"detail": "Item successfully updated", "data": serializer.data}, status=status.HTTP_201_CREATED)

              else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                 return Response({'detail': 'Item to be updated does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except item.DoesNotExist:
            return Response({'detail': 'Item does not exist'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)