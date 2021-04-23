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
    
    git_link='a'
    for repo in g.get_user().get_repos(type='owner'):
        params['repository_list'].append(repo.name)
        params['repository_link'].append("https://github.com/mituoka/"+repo.name)
        if repo.name == 'Convenient_tool':

            print(repo.git_url)
            print(repo.url)
            print(repo.pulls_url)
            print(repo.downloads_url)
        params['repository_description'].append(repo.description)

  
    return render(request,'github.html',params)