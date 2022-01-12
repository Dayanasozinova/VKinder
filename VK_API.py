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
            'hometown': city,
            'count': 1000,
            'birth_year': bdata,
            'status': 1,  # статус положение
            'v': '5.131',
            'access_token': self.token
        }
        data_users = []
        res_user = requests.get(URL, params=params)
        res_user = res_user.json()
        for user in res_user['response']['items']:
            if user['is_closed'] == False:
                id_user = user['id']
                first_name = user['first_name']
                last_name = user['last_name']
                data_users.append((id_user, first_name, last_name))
        return data_users

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
        # print(res_photo)

        data_photo = []
        for photo in res_photo['response']['items']:
            id = photo['id']
            likes = photo['likes']['count']
            coments = photo['comments']['count']
            url_photo = photo['sizes'][-1]['url']
            data_photo.append((likes, coments, id, url_photo))
        sort_data_photo = sorted(data_photo, key=itemgetter(0, 1), reverse=True)
        id_photo_list = []
        if len(sort_data_photo) >= 3:
            id_photo_1 = sort_data_photo[0][2]
            id_photo_list.append(id_photo_1)
            id_photo_2 = sort_data_photo[1][2]
            id_photo_list.append(id_photo_2)
            id_photo_3 = sort_data_photo[2][2]
            id_photo_list.append(id_photo_3)
        elif len(sort_data_photo) >= 2:
            id_photo_1 = sort_data_photo[0][2]
            id_photo_list.append(id_photo_1)
            id_photo_2 = sort_data_photo[1][2]
            id_photo_list.append(id_photo_2)
        elif len(sort_data_photo) >= 1:
            id_photo_1 = sort_data_photo[0][2]
            id_photo_list.append(id_photo_1)

        return id_photo_list

    def messages_getByld(self, messages_id, tokenb):
        URL = 'https://api.vk.com/method/messages.getById'
        params = {
            'owner_id': messages_id,
            'extended': '1',
            'v': '5.81',
            'access_token': tokenb
        }
        res_mes = requests.get(URL, params=params)
        res_mes = res_mes.json()
        return res_mes





vk1 = API_VK('file_vk.txt')
# print(vk1.get_photo('63531715'))
# print(vk1.user_get('63531715'))
# print(vk1.users_search(1, 'Rfpfym', 1999))
