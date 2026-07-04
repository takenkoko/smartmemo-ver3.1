from django.shortcuts import render,redirect
from .models import Memo, Category
from django.db.models import Q

# Create your views here.
def index(request):
    memos=Memo.objects.all()
    return render(request,"smartmemo/index.html",{
        "memos":memos,
    })

#フォーム作成
def create(request):
    if request.method=="POST":
        
        title=request.POST["title"]
        content=request.POST["content"]
        category_id = request.POST.get("category")

        category = None
        if category_id:
            category = Category.objects.get(id=category_id)

        Memo.objects.create(
            title=title,
            content=content,
            category=category
        )
        return redirect("index")
    return render(request,
                  "smartmemo/create.html",
                  {
                      "categories":Category.objects.all()
                  }
                  )

#編集機能を作成
def edit(request,memo_id):
    memo = Memo.objects.get(id=memo_id)

    #更新処理を作成
    if request.method=="POST":
        
        memo.title=request.POST["title"]
        memo.content=request.POST["content"]

        memo.save()

        return redirect("index")

    return render(request,"smartmemo/edit.html",{
        "memo":memo,
    })

#削除機能を作成
def delete(request,memo_id):
    memo=Memo.objects.get(id=memo_id)

    memo.delete()
    
    return redirect("index")

#検索機能を作成
def search(request):
    keyword = request.GET.get("keyword","")

    memos= Memo.objects.filter(
        Q(title__icontains=keyword)|
        Q(content__icontains=keyword)
    )

    return render(
        request,
        "smartmemo/index.html",
        {
            "memos":memos,
            "keyword":keyword,
        }
    )