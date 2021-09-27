from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
balance_type = ((u'收入', u'收入'), (u'支出', u'支出'))


class Category(models.Model):
    category = CharField(max_length=20)
    # 增加user
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    # 讓 category 顯示 category 名稱
    def __str__(self):
        return self.category


class Record(models.Model):
    data = DateField()        # 打錯了應該是date打成data，但修改0001_initial.py無法改，暫時先如此
    description = CharField(max_length=300)
    category = ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cash = IntegerField()
    balance_type = CharField(max_length=2, choices=balance_type)
    # user = models.ForeignKey(
    # User, null=True, on_delete=models.CASCADE)   # 增加user

    # 讓 Record 顯示 description 名稱
    def __str__(self):
        return self.description


# 因為在一開始建立資料庫時打錯(把date打成data)測試此方法
class Quiz(models.Model):
    question_text = models.CharField(max_length=200)

    class Meta:
        managed = True
        app_label = 'quiz'
        db_table = 'preexist'
