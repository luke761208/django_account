from django.shortcuts import render, HttpResponse, redirect
from .models import Record, Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def hello(request):
    return render(request, 'app/hello.html', {})


@login_required
def frontpage(request):
    # 知道使用者是誰
    # user = request.user
    # 給變數，而initial是給他一個預設值
    record_form = RecordForm(initial={'balance_type': '支出'})
    records = Record.objects.filter()  # 從 Record table 中取所有資料
    income_list = [
        record.cash for record in records if record.balance_type == '收入']
    outcome_list = [
        record.cash for record in records if record.balance_type == '支出']
    income = sum(income_list) if len(income_list) != 0 else 0
    outcome = sum(outcome_list) if len(outcome_list) != 0 else 0
    net = income - outcome
    # locals() 會自動抓 def 裡面資料
    return render(request, 'app/index.html', locals())


@login_required
def settings(request):
    # user = request.user
    categories = Category.objects.filter()  # 從 Record table 中取所有資料
    # 我們指定他最後會回傳值到 settings.html這個檔案
    return render(request, 'app/settings.html', locals())


@login_required
def addCategory(request):
    if request.method == 'POST':               # 希望都是用post方法進來而不是get比較保險
        # user = request.user
        posted_data = request.POST             # 是一個dictionary
        category = posted_data['add_cateogry']  # 從 settings.html中取得
        Category.objects.get_or_create(
            category=category)  # get_or_create避免重複資料輸入進去
        # categories = Category.objects.filter()                # 如果不用 redirect
    # return render(request, 'app/settings.html', locals())
    return redirect('/settings')


@login_required
def deleteCategory(request, category):
    user = request.user
    Category.objects.filter(category=category).delete()
    return redirect('/settings')
# @login_required
# def deleteCategory(request, category):
#     user = request.user
#     Category.objects.filter(category=category, user=user).delete()
#     return redirect('/settings')


@login_required
def addRecord(request):
    if request.method == 'POST':
        # user = request.user
        form = RecordForm(user, request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = user
            record.save()
    return redirect('/')


@login_required
def deleteRecord(request):
    if request.method == 'POST':
        id = request.POST['delete_val']    # 找出id，剛剛id是存在name=delete_val裡面
        Record.objects.filter(id=id).delete()  # 取出來後對id做刪除的動作
    return redirect('/')                       # 最後返回首頁
