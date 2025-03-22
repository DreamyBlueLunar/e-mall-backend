from django.db import models

# Create your models here.

# 用户信息表
class UserInfo(models.Model):
    # 用户ID
    id = models.AutoField(primary_key=True)
    # 用户名
    username = models.CharField(max_length=32, null=False)
    # 用户密码
    password = models.CharField(max_length=255, null=False)
    # 用户电话
    telephone = models.CharField(max_length=16, null=False, unique=True)
    # 用户邮箱
    email = models.CharField(max_length=64, null=False, unique=True)
    # 用户类型 -> 1：普通用户，2：商家，3：管理员
    category = models.IntegerField(default=1)

    class Meta:
        db_table = 'user_info'

# # 地址信息表
# class Address(models.Model):
#     # 地址信息ID，可以设置成主键，一个用户不能反复向数据库中注册地址
#     id = models.AutoField(primary_key=True)
#     # 区、街道信息
#     details = models.CharField(max_length=64)
#     # 城市
#     city = models.CharField(max_length=16)
#     # 省、州（我才不乐意写 state 呢）
#     province = models.CharField(max_length=16)
#     # 国家
#     country = models.CharField(max_length=16)
#     # 和这条地址形成映射的用户id，外键，
#     user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'address'