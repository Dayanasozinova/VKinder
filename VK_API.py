from pprint import pprint
from operator import itemgetter
import requests


class API_VK:
    def __init__(self, file):
        with open(file, 'r') as f:
            token = f.read().strip()
        self.token = token

    def user_get(self, user_id):
        URL = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': user_id,
            'fields': 'id, bdate, city, home_town, relation, sex, ',  # sex 1-женский, 2-мужской, 0-пол не указан
            'v': '5.131',
            'access_token': self.token}
        res_2 = requests.get(URL, params=params)
        res_2 = res_2.json()
        return res_2

    def users_search(self, sex, city, bdata):
        URL = 'https://api.vk.com/method/users.search'
        params = {
            'sex': sex,
            'city': city,
            'count': 1000,
            'birth_year': bdata,
            'status': 1,  # статус положение
            'v': '5.131',
            'access_token': self.token
        }
        data_users = []
        res_men = requests.get(URL, params=params)
        res_men = res_men.json()
        for user in res_men['response']['items']:
            if user['is_closed'] == False:
                id_user = user['id']
                data_users.append(id_user)
        return len(data_users)

    def get_photo(self, user_id):
        URL = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'v': '5.131',
            'access_token': self.token
        }
        res_photo = requests.get(URL, params=params)
        res_photo = res_photo.json()

        data_photo = []
        for photo in res_photo['response']['items']:
            id = photo['id']
            likes = photo['likes']['count']
            coments = photo['comments']['count']
            url_photo = photo['sizes'][-1]['url']
            data_photo.append((likes, coments, id, url_photo))
        sort_data_photo = sorted(data_photo, key=itemgetter(0, 1), reverse= True)
        url_photo_1 = sort_data_photo[0][-1]
        url_photo_2 = sort_data_photo[1][-1]
        url_photo_3 = sort_data_photo[2][-1]
        return url_photo_1, url_photo_2, url_photo_3



        

vk1 = API_VK('file_vk.txt')
pprint(vk1.users_search_men(60, 1999))