from django.shortcuts import render
from djangoweliang.models import MyUser,House,Reviews
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from weidu import weidu
from cutwords import cutwords
import json
import logging
from django.http import HttpResponse


# Create your views here.
def index(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'blog/index.html', content)

def analyse_reci(request):
    city_list = House.objects.values_list('city', flat=True).distinct()
    query_city = request.GET.get('city', '北京')
    f = query_city + 'detail.xlsx'
    reci_list = cutwords(f)
    content = {
        'reci_list': json.dumps(reci_list),
        'city_list': city_list,
    }
    return render(request, 'blog/analyse_reci.html', content)


def analyse_data(request):
    city_list = House.objects.values_list('city', flat=True).distinct()
    query_city = request.GET.get('city', '成都')
    f = query_city+'detail.xlsx'
    weidu_list = weidu(f)
    content = {
        'weidu_list': json.dumps(weidu_list),
        'city_list': city_list,
    }
    return render(request,'blog/analyse_data.html',content)

def signup(request):

    #authenticate()函数用来检查用户名和密码是否和账户匹配
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage')) #HttpResponseRedirect()的参数是一个跳转地址,用来使用户的浏览器跳转到该地址
    state = None
    if request.method == 'POST': #判断POST或GET方法来对表单采取不同的处理方式
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else: #如果是GET方法，则创建新用户
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', ''))
                new_my_user.save()
                state = 'success'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'blog/signup.html', content)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'blog/login.html', content)

def logout(request):
    auth.logout(request) #Django的logout()函数将会确保用户注销,以及终止它们的ession
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'blog/set_password.html', content)

def search_data(request):
    user = request.user if request.user.is_authenticated() else None
    city_list = House.objects.values_list('city', flat=True).distinct()
    query_city = request.GET.get('city', 'all')
    if (not query_city) or House.objects.filter(city=query_city).count() is 0:
        query_city = 'all'
        house_list = House.objects.all()
    else:
        house_list = House.objects.filter(city=query_city)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        house_list = House.objects.filter(Q(name__contains=keyword)|Q(price__contains=keyword))#(name__contains =keyword)
        query_city = 'all'

    paginator = Paginator(house_list, 10)
    page = request.GET.get('page')
    try:
        house_list = paginator.page(page)
    except PageNotAnInteger:
        house_list = paginator.page(1)
    except EmptyPage:
        house_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'search_data',
        'city_list': city_list,
        'query_city': query_city,
        'house_list': house_list,
    }
    return render(request, 'blog/search_data.html', content)

def detail(request):
    user = request.user if request.user.is_authenticated() else None
    house_id = request.GET.get('id', '')
    house = House.objects.get(pk=house_id)
    description_list = Reviews.objects.filter(namer = house.name)
    content = {
        'user': user,
        'active_menu': 'search_data',
        'house': house,
        'description_list': description_list,
    }
    return render(request, 'blog/detail.html', content)