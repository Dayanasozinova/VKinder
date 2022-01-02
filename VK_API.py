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
            'birth_year': bdata,
            'status': 1,
            'v': '5.131',
            'access_token': self.token
        }
        res_1 = requests.get(URL, params=params)
        res_1 = res_1.json()
        return res_1

    def users_search_men(self, city, bdata):
        URL = 'https://api.vk.com/method/users.search'
        params = {
            'sex': 2,
            'city': city,
            'birth_year': bdata,
            'status': 1,  # статус положение
            'v': '5.131',
            'access_token': self.token
        }
        res_men = requests.get(URL, params=params)
        res_men = res_men.json()
        return res_men


vk1 = API_VK('file_vk.txt')
