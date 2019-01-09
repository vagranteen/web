from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

# Register your models here.
#模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hcomment']
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)