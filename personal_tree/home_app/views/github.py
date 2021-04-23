from django.shortcuts import render,redirect
from github import Github


def main_func(request):
       
    params = {
        'repository_list':[],
        'repository_link':[],
        'repository_description':[],
    }

    token = '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'
    # or using an access token
    g = Github(token)
    
    for repo in g.get_user().get_repos(type='owner'):
        params['repository_list'].append(repo.name)
        params['repository_link'].append("https://github.com/mituoka/"+repo.name)
        params['repository_description'].append(repo.description)

  
    return render(request,'github.html',params)