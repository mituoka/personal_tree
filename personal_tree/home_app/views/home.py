from django.shortcuts import render,redirect

def main_func(request):
       
    params = {
        'title_name':'PERSONAL TREE',
        'menu_tag1':'お問い合わせ',
        'menu_tag2':'アプリ詳細',
    }

    return render(request,'home.html',params)