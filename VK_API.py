from pprint import pprint
from operator import itemgetter
import requests
from Data import registration

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
        if 'city' in res_2['response'][0].keys():
            print(True)
            registration(res_2['response'][0]['id'], res_2['response'][0]['first_name'],
                         res_2['response'][0]['last_name'], res_2['response'][0]['sex'], res_2['response'][0]['bdate'][-4:],
                         res_2['response'][0]['city']['id'])
        else:
            print(None)
            registration(res_2['response'][0]['id'], res_2['response'][0]['first_name'],
                         res_2['response'][0]['last_name'], res_2['response'][0]['sex'], res_2['response'][0]['bdate'][-4:], '',
                         res_2['response'][0]['home_town'])
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


vk1 = API_VK('file_vk.txt')
# print(vk1.get_photo('63531715'))
print(vk1.user_get('63531715'))
# 63531715
# for user in vk1.users_search(vk1.user_get(event.user_id)['response'][0]['sex'], vk1.user_get(event.user_id)['response'][0]['city']['id'], vk1.user_get(event.user_id)['response'][0]['bdate'][-4:]):
#     user_ = user[0]
#     first_name = user[1]
#     last_name = user[2]
#     print(first_name, last_name, vk1.get_photo(user_), len(vk1.get_photo(user_)))
#     # bot1.send_mes(len(vk1.get_photo(user_)))
#     if len(vk1.get_photo(user_)) >= 3:
#         bot1.write_msg_3_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{user_}", user_,
#                                vk1.get_photo(user_)[0], vk1.get_photo(user_)[1], vk1.get_photo(user_)[2])
#         time.sleep(5)
#     elif len(vk1.get_photo(user_)) >= 2:
#         bot1.write_msg_2_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{user_}", user_,
#                                vk1.get_photo(user_)[0], vk1.get_photo(user_)[1])
#         time.sleep(5)
#     elif len(vk1.get_photo(user_)) >= 1:
#         bot1.write_msg_1_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{user_}", user_,
#                                vk1.get_photo(user_)[0])
#         time.sleep(5)
#     else:
#         bot1.write_msg_photo_not(len(vk1.get_photo(user_)), event.user_id,
#                                  f"{first_name} {last_name} https://vk.com/id{user_}")
#         time.sleep(5)

