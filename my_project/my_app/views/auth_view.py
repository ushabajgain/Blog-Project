from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def login_page(request):
    return render(request,'auth/login_page.html')

def register_page(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password:
            errors['password']= "Password field is empty"

        if not confirm_password:
            errors['confirm_password']= "Confirm password firld is empty"    

        if password != confirm_password:
            errors['confirm_password'] = "Password and confirm password do not match"

        if not username:
            errors['username'] = "Username field is required"    

        if not errors:
            user = User.objects.create(
                username=username,
                email=email
            ) 
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            errors['error']= "Failed to register"
            return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})

    return render(request,'auth/register_page.html',{'errors':errors})