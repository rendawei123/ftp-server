# 网络编程

主要收集一些学习Python过程中的网络编程相关知识，涉及socket传输的基本实现，使用wsgi自定义框架以及Django简单使用

### 分页

```
"""
使用方法：

from utils.page import Pagination
def users(request):
    current_page = int(request.GET.get('page',1))

    total_item_count = models.UserInfo.objects.all().count()
    # page_obj = Pagination(current_page,total_item_count,request.path_info)
    page_obj = Pagination(current_page,total_item_count,'/users.html')

    user_list = models.UserInfo.objects.all()[page_obj.start:page_obj.end]

    return render(request,'users.html',{'user_list':user_list,'page_html':page_obj.page_html()})


"""
```

