from django.shortcuts import render,redirect
import requests
import json

def qiita_all_request():
    USER_ID='Aqua_MT'
    URL = "https://qiita.com/api/v2/users/"+ USER_ID+"/items"
    TOKEN = "795547a640bf1781d8c193b3a3a42e10a3709510"
    HEADER = {
        'Authorization': 'Bearer {}'.format(TOKEN),
    }
    response = requests.get(URL, headers=HEADER)
    json_data=response.json()
    return json_data

def main_func(request):
       
    params = {
        'add_image_bottom':'新規追加',
        'article_id':[],
        'qiita_title_list':[],
        'article_like_count':[],
        'update_time':[]
    }

    json_data=qiita_all_request()

    if request.method =='GET':
        for data in json_data:
        
            params['article_id'].append(data['id'])
            params['qiita_title_list'].append(data['title'])
            params['article_like_count'].append(data['likes_count'])
            # params['qiita_title_list'].update({data['title']:data['likes_count']})
            params['update_time'].append(data['updated_at'])

    if request.method =='POST':
        search_title=request.POST.get('search_title')
        for data in json_data:
            if search_title in data['title']:
                params['article_id'].append(data['id'])
                params['qiita_title_list'].append(data['title'])
                params['article_like_count'].append(data['likes_count'])
                # params['qiita_title_list'].update({data['title']:data['likes_count']})
                params['update_time'].append(data['updated_at'])




    return render(request,'qiita.html',params)