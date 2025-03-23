import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.utils import timezone

from authentication.email import makeConfirmCode, sendMail
from authentication.forms import SignUpForm, SignInForm
from authentication.models import UserInfo, ConfirmCode
from eMallBackend import settings

'''
 - 逻辑是，如果确认密码输入不对、电话重复、邮箱重复，注册请求都会被驳回
'''


def signUpUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                message = 'The passwords do not match'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            if UserInfo.objects.filter(telephone=form.cleaned_data['telephone']).exists():
                message = 'Telephone number already registered'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            if UserInfo.objects.filter(email=form.cleaned_data['email']).exists():
                message = 'Email already registered'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            user = UserInfo(username=form.cleaned_data['username'],
                            password=make_password(form.cleaned_data['password']),
                            telephone=form.cleaned_data['telephone'],
                            email=form.cleaned_data['email'], )
            user.save()
            code = makeConfirmCode(user)
            sendMail(user.email, code)
            message = 'Your account has been created'
            # print(message)
            return redirect('/signin')  # 注册成功后重定向到登录页面

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


'''
 - 逻辑是，如果确认密码输入不对、电话重复、邮箱重复，注册请求都会被驳回
'''


def signUpMerchant(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                message = 'The passwords do not match'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            if UserInfo.objects.filter(telephone=form.cleaned_data['telephone']).exists():
                message = 'Telephone number already registered'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            if UserInfo.objects.filter(email=form.cleaned_data['email']).exists():
                message = 'Email already registered'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            user = UserInfo(username=form.cleaned_data['username'],
                            password=make_password(form.cleaned_data['password']),
                            telephone=form.cleaned_data['telephone'],
                            email=form.cleaned_data['email'],
                            category=2)
            user.save()
            code = makeConfirmCode(user)
            sendMail(user.email, code)
            message = 'Your account has been created'
            # print(message)
            return redirect('/signin')  # 注册成功后重定向到登录页面

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


'''
 - 逻辑是，如果确认密码输入不对、电话重复、邮箱重复，注册请求都会被驳回
'''


def signUpManager(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                message = 'The passwords do not match'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            if UserInfo.objects.filter(telephone=form.cleaned_data['telephone']).exists():
                message = 'Telephone number already registered'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            if UserInfo.objects.filter(email=form.cleaned_data['email']).exists():
                message = 'Email already registered'
                # print(message)
                return render(request, 'signup.html', {'form': form, 'message': message})

            user = UserInfo(username=form.cleaned_data['username'],
                            password=make_password(form.cleaned_data['password']),
                            telephone=form.cleaned_data['telephone'],
                            email=form.cleaned_data['email'],
                            category=3)
            user.save()
            code = makeConfirmCode(user)
            sendMail(user.email, code)
            message = 'Your account has been created'
            # print(message)
            return redirect('/signin')  # 注册成功后重定向到登录页面

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def signIn(request):
    if request.session.get('is_login', None):
        return redirect("/home")

    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

        try:
            user = UserInfo.objects.get(username=username)

            if not user.hasConfirmed:
                message = 'User is not confirmed'
                # print(message)
                return render(request, 'signin.html', {'form': form, 'message': message})
            if not check_password(password, user.password):
                message = 'The password does not match'
                # print(message)
                return render(request, 'signin.html', {'form': form, 'message': message})
            message = 'Successfully logged in'
            # print(message)

            if user.category == 1:
                return redirect('/home/index')  # 登录成功后重定向
            elif user.category == 2:
                return redirect('/home/merchant')
            else:
                return redirect('/home/manager')

        except:
            message = 'User does not exist'
            # print(message)
            return render(request, 'signin.html', {'form': form, 'message': message})
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})


def homeIndex(request):
    return render(request, 'home/index.html')


def homeManager(request):
    return render(request, 'home/manager.html')


def homeMerchant(request):
    return render(request, 'home/merchant.html')


def confirmUser(request):
    code = request.GET.get('code', None)

    try:
        confirm = ConfirmCode.objects.get(code=code)
    except:
        message = 'Invalid confirmation request.'
        # print(message)
        return render(request, 'confirm.html', locals())

    # regTime 是带有时区信息的，不用重新设置
    regTime = confirm.regTime
    now = timezone.now()
    if now > regTime + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = 'The email has been out of date! Please sign up again.'
    else:
        confirm.user.hasConfirmed = True
        confirm.user.save()
        confirm.delete()
        message = 'Thank you for confirming your email.'
    # print(message)
    return render(request, 'confirm.html', locals())
