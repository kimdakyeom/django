from django.shortcuts import render, redirect

from normal.forms import NormalForm
from .models import Normal
from django.core.paginator import Paginator


def index(request):
    # pk 기준으로 정렬
    normals = Normal.objects.order_by("-pk")

    # 입력 파라미터
    page = request.GET.get("page", "1")
    # 페이징
    paginator = Paginator(normals, 3)
    page_obj = paginator.get_page(page)
    context = {
        "normals": normals,
        "page_obj": page_obj,
    }
    return render(request, "normal/index.html", context)


def create(request):
    # POST : input 값 가져와서 검증하고 DB에 저장
    if request.method == "POST":
        normal_form = NormalForm(request.POST)
        # 유효성 검사
        if normal_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 인덱스 페이지로
            normal_form.save()
            return redirect("/")
    # GET : Form 제공
    elif request.method == "GET":
        normal_form = NormalForm()
    context = {
        "normal_form": normal_form,
    }
    return render(request, "normal/create.html", context)


def detail(request, pk):
    normal = Normal.objects.get(pk=pk)
    context = {
        "normal": normal,
    }
    return render(request, "normal/detail.html", context)


def update(request, pk):
    # pk 해당하는 db 값 가져오기
    normal = Normal.objects.get(pk=pk)
    # POST : input 값 가져와서 검증하고 DB에 저장
    if request.method == "POST":
        normal_form = NormalForm(request.POST, instance=normal)
        # 유효성 검사
        if normal_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            normal_form.save()
            return redirect("normal:detail", normal.pk)
    # GET : Form 제공
    elif request.method == "GET":
        normal_form = NormalForm(instance=normal)
    context = {
        "normal_form": normal_form,
    }
    return render(request, "normal/update.html", context)


def delete(request, pk):
    normal = Normal.objects.get(pk=pk)
    normal.delete()
    return redirect("/")


def result(request):
    query = request.GET.get("query")
    select = request.GET.get("select")
    if select == "title":
        query = Normal.objects.filter(title__contains=query)
    else:
        query = Normal.objects.filter(content__icontains=query)
    context = {
        "query": query,
    }
    return render(request, "normal/result.html", context)
