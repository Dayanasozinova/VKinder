from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll


class BOT:
    def __init__(self, token):
        self.vk = None
        self.token = token

    def longpoll_listen(self):
        self.vk = vk_api.VkApi(token=self.token)
        return VkLongPoll(self.vk).listen()

    def write_msg_photo_not(self, user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7)})

    def write_msg_3_photo(self, user_id, message, owner_id, media_id1, media_id2, media_id3):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': f'photo{owner_id}_{media_id1}, '
                                                       f'photo{owner_id}_{media_id2},'
                                                       f'photo{owner_id}_{media_id3}'})

    def write_msg_2_photo(self, user_id, message, owner_id, media_id1, media_id2):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': f'photo{owner_id}_{media_id1}, '
                                                       f'photo{owner_id}_{media_id2}'})

    def write_msg_1_photo(self, user_id, message, owner_id, media_id1):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': f'photo{owner_id}_{media_id1}'})


bot1 = BOT('0059adfe554cc8f08cad4a866d8875065d4bff6dc4ba9cf31daab47c1dca5e730413453727bd2a86817a7')
