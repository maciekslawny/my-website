from json import loads
from requests import get


def load_repos():
    slownik = {}
    url = 'https://api.github.com/users/maciekslawny/repos'
    repos = loads(get(url).text) 
    return repos





