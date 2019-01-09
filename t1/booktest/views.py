from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo

# Create your views here.
def index(request):
    #return HttpResponse("Hello World!")
    #加载模板文件
    booklist = BookInfo.objects.all()
    #temp = loader.get_template('booktest/index.html')
    #定义模板上下文，给模板文件传数据
    context ={'books':booklist}
    #模板渲染,产生标准的html内容
    #res_htm = temp.render()
    #return HttpResponse(res_htm,{'books':booklist})
    return render(request,'booktest/index.html',context)
def index2(request):
    return HttpResponse("老铁，没毛病")