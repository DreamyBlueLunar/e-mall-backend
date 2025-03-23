import datetime

from authentication import models
from django.core.mail import EmailMultiAlternatives

from eMallBackend import settings


def hashCode(name, now):
    combined = name + str(now)
    return hash(combined)


def makeConfirmCode(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hashCode(user.username, now)
    models.ConfirmCode.objects.create(code=code, user=user)
    return code


def sendMail(email, code):
    subject = '来自e-mall的注册确认邮件'

    text_content = '''感谢注册e-mall！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>emall_susie.com</a>，\
                    你来编这个东西，我英语不好</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('localhost:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
