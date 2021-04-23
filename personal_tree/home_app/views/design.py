from django.shortcuts import render,redirect
import requests
import json

def main_func(request):
       
    params = {
        'add_image_bottom':'新規追加',
    }


    # https://photos.app.goo.gl/jqJdBZauf1vie8kg6

    return render(request,'design.html',params)