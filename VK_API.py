from random import randrange

import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


class BOT:
    def __init__(self, token):
        self.token = token

    def longpoll_listen(self):
        self.vk = vk_api.VkApi(token=self.token)
        return VkLongPoll(self.vk).listen()

    def write_msg(self, user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })


bot1 = BOT('0059adfe554cc8f08cad4a866d8875065d4bff6dc4ba9cf31daab47c1dca5e730413453727bd2a86817a7')


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


vk1 = API_VK('file_vk.txt')


def call_bot():
    for event in bot1.longpoll_listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request == "привет":
                    vk1.user_get(event.user_id)
                    bot1.write_msg(event.user_id,
                                   f"Здравствуйте, {vk1.user_get(event.user_id)['response'][0]['first_name']}. Кого будем искать?\n"
                                   f"P.S. напишите М или Ж")
                elif request == "М":
                    vk1.users_search(2, vk1.user_get(event.user_id)['response'][0]['city']['id'],
                                     vk1.user_get(event.user_id)['response'][0]['bdate'][-4:])  # для поиска мальчиков
                    bot1.write_msg(event.user_id, "Ищем)")
                elif request == "Ж":
                    print(vk1.users_search(1, vk1.user_get(event.user_id)['response'][0]['city']['id'],
                                     vk1.user_get(event.user_id)['response'][0]['bdate'][-4:]))  # для поиска девочек
                    bot1.write_msg(event.user_id, "Ищем)")
                elif request == "пока":
                    bot1.write_msg(event.user_id, "Всего доброго")
                else:
                    bot1.write_msg(event.user_id, "Не поняла вашего ответа...")
# call_bot()