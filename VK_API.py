from random import randrange

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


def call_bot():
    for event in bot1.longpoll_listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request == "привет":
                    bot1.write_msg(event.user_id, f"Хай, {event.user_id}")
                elif request == "пока":
                    bot1.write_msg(event.user_id, "Пока((")
                else:
                    bot1.write_msg(event.user_id, "Не поняла вашего ответа...")
