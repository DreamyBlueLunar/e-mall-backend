from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignUpForm, SignInForm
from Auth.models import UserInfo

def signUpUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # 哈希密码
            form.instance.password = make_password(form.cleaned_data['password'])
            form.save()  # 保存用户信息
            return redirect('/signin')  # 注册成功后重定向到登录页面
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def signInUser(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserInfo.objects.get(username=username)
                if check_password(password, user.password):
                    # 密码正确，登录成功
                    # 处理登录逻辑（例如，设置会话）
                    return redirect('/home')  # 登录成功后重定向
                else:
                    form.add_error('password', 'wrong password')
            except UserInfo.DoesNotExist:
                form.add_error('username', 'user does not exist')
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})

def home(request):
    return render(request, 'home.html')