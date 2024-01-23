from django.http import HttpResponse
from musics.models import Product


def add(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    p = Product(name=name, price=price)
    p.save()
    return HttpResponse("<p>成功添加</p>")


def gall(request):
    li = Product.objects.all()
    a = ''
    for v in li:
        print("==================")
        print(v.name)
        a += v.name + ' '
    return HttpResponse(f"<p> {a} </p>")


def update(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.name = "西瓜"
    product.save()
    return HttpResponse("<p>修改成功</p>")


def delete(request):
    id = request.GET.get("id")
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponse("<p>刪除成功</p>")
