from json import loads
from requests import get


def load_repos():
    """Function gets repos from API and sorts them according to updated date"""
    
    url = 'https://api.github.com/users/maciekslawny/repos'
    repos = loads(get(url).text) 

    dates_repos = []
    for repo in repos:
        date_repo = [repo['updated_at'], repo]
        dates_repos.append(date_repo)
    dates_repos.sort(reverse=True)
    sorted_repos = []
    for repo in dates_repos:
        sorted_repos.append(repo[1])
    
    return sorted_repos

    



load_repos()
