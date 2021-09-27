# 已刪除不必要資訊
from django.contrib import admin
from django.urls import path
from . import views                 # 原本是 from app import views

urlpatterns = [
    path('admin/', admin.site.urls),  # 可以刪除，我自己想看
    path('hello/', views.hello),      # 可以刪除，我自己想看
    path('', views.frontpage),
    path('settings', views.settings),
    path('add_category', views.addCategory),
    path('delete_category', views.deleteCategory),
    # path('delete_category/{{ category.category }}', views.deleteCategory),
    # path('delete_category/(?P<category>\w+)', views.deleteCategory),
    path('add_record', views.addRecord),
    path('delete_record', views.deleteRecord),
]
