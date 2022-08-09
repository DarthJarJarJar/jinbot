import requests
import json
id = "414906"

class SearchKino:
    def __init__(self, key) -> None:
        self.key = key
        res = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=88637c22a27d11937d1168157cf81ce9&language=en-US&query={key}&page=1")
        resulttemp = json.loads(res.text)
        result = resulttemp['results']
        res_list = []
        for movie in result:
            res_list.append({'name': movie['original_title'], 'date': movie['release_date'], 'id':movie['id']})
        self.results = res_list

class Kino:
    def __init__(self, id) -> None:
        self.id = id
        res = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=88637c22a27d11937d1168157cf81ce9&language=en-US")
        self.data = json.loads(res.text)
        data = json.loads(res.text)
        self.description = data['overview']
        self.runtime = data['runtime']
        self.title = data['title']
        self.tagline = data['tagline']
        res2 = requests.get(f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=88637c22a27d11937d1168157cf81ce9&language=en-US")
        credits: dict = json.loads(res2.text)
        print(credits['crew'])
        credits.fromkeys

    
kino = Kino(id)

    