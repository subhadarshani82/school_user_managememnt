from django.shortcuts import render, redirect
from .models import Role, User, pbkdf2_sha256


def dashboard(request):
    total_teach_users = User.objects.filter(role=1).count()
    active_teach = User.objects.filter(role=1, status='Active').count()
    inactive_teach = User.objects.filter(role=1, status='Inactive').count()
    teaches = {'total_teach_user': total_teach_users, 'active_teach': active_teach, 'inactive_teach': inactive_teach}

    total_non_teach_users = User.objects.filter(role=2).count()
    active_non_teach = User.objects.filter(role=2, status='Active').count()
    inactive_non_teach = User.objects.filter(role=2, status='Inactive').count()
    non_teaches = {'total_non_teach_user': total_non_teach_users, 'active_non_teach': active_non_teach,
                   'inactive_non_teach': inactive_non_teach}

    total_students = User.objects.filter(role=3).count()
    active_student = User.objects.filter(role=3, status='Active').count()
    inactive_student = User.objects.filter(role=3, status='Inactive').count()
    students = {'total_students': total_students, 'active_student': active_student,
                'inactive_student': inactive_student}

    return render(request, 'dashboard.html', {'teaches': teaches, 'non_teaches': non_teaches, 'students': students})


def user_role(request):
    if request.method == 'POST':
        role_name = request.POST.get('role')
        role = Role(role_name=role_name)
        print(role)
        role.save()

    return render(request, 'add_role.html')


def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        enc_psw = pbkdf2_sha256.encrypt(password, rounds=20, salt_size=5)
        address = request.POST.get('address')
        role_id = request.POST.get('select_role')
        role = Role.objects.get(id=role_id)
        status = request.POST.get('status')
        print(name, phone, address, email, role, status)
        users = User(name=name, email=email, phone=phone, password=enc_psw, address=address, role=role,
                     status=status)
        users.save()
    return render(request, 'insert_update.html', {'data': [Role.objects.all()]})


def fetch_user(request):
    users = User.objects.all()
    return render(request, 'user_data_table.html', {'data': [users]})


def teaching(request):
    teach = User.objects.filter(role=1)
    return render(request, 'user_data_table.html', {'data': [teach, 'Teaching']})


def non_teaching(request):
    non_teach = User.objects.filter(role=2)
    return render(request, 'user_data_table.html', {'data': [non_teach, 'Non_teaching']})


def student(request):
    student = User.objects.filter(role=3)
    return render(request, 'user_data_table.html', {'data': [student, 'student']})


def delete_user(request, id):
    dlt_user = User.objects.get(pk=id)
    dlt_user.delete()
    return redirect('/')


def get_data_for_update_user(request, id):
    user = User.objects.get(pk=id)
    role=Role.objects.all()
    return render(request, 'insert_update.html', {'data': [role,user]})
def update_user(request,id):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        status=request.POST['status']
        user = User.objects.filter(pk=id)
        user.update(name=name,email=email,phone=phone,status=status)
    return render(request,'insert_update.html')
