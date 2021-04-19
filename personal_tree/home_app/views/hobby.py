from django.shortcuts import render,redirect

def main_func(request):
       
    params = {
        'add_image_bottom':'新規追加',
    }

    return render(request,'hobby.html',params)