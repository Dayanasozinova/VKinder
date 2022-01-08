from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk = vk_api.VkApi(token='0059adfe554cc8f08cad4a866d8875065d4bff6dc4ba9cf31daab47c1dca5e730413453727bd2a86817a7')
longpoll = VkLongPoll(vk)

keyboard = VkKeyboard(inline=True)

class BOT:
    def __init__(self, token):
        self.vk = None
        self.token = token

    def write_msg_hello(self, user_id):
        keyboard.add_button('М', VkKeyboardColor.PRIMARY)
        keyboard.add_button('Ж', VkKeyboardColor.NEGATIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': f"Привет. Я помогу тебе найти пару мечты."
                                                                        f"Давай определимся кого будем искать.",
                                         'random_id': randrange(10 ** 7),
                                         'keyboard': keyboard.get_keyboard()})

    def longpoll_listen(self):
        self.vk = vk_api.VkApi(token=self.token)
        return VkLongPoll(self.vk).listen()

    def write_msg_photo_not(self, user_id, message):
        keyboard.add_button('Дальше.', VkKeyboardColor.POSITIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'keyboard': keyboard.get_keyboard()})
    #
    # def write_msg_auth(self, user_id, message):
    #     self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
    #                                      'keyboard': keyboard.get_keyboard()})

    def write_msg_3_photo(self, user_id, message, owner_id, media_id1, media_id2, media_id3):
        keyboard.add_button('Дальше.', VkKeyboardColor.POSITIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': f'photo{owner_id}_{media_id1}, '
                                                       f'photo{owner_id}_{media_id2},'
                                                       f'photo{owner_id}_{media_id3}',
                                         'keyboard': keyboard.get_keyboard()})

    def write_msg_2_photo(self, user_id, message, owner_id, media_id1, media_id2):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': f'photo{owner_id}_{media_id1}, '
                                                       f'photo{owner_id}_{media_id2}',
                                         'keyboard': keyboard.get_keyboard()})

    def write_msg_1_photo(self, user_id, message, owner_id, media_id1):
        keyboard.add_button('Дальше.', VkKeyboardColor.POSITIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': f'photo{owner_id}_{media_id1}',
                                         'keyboard': keyboard.get_keyboard()})

    def send_mes(self, user_id, text, keyboard=None, template=None):
        self.vk.method('messages.send', {'user_id': user_id, 'message': text,
                                         'random_id': randrange(10 ** 7),
                                         'keyboard': keyboard,
                                         'template': template})


bot1 = BOT('0059adfe554cc8f08cad4a866d8875065d4bff6dc4ba9cf31daab47c1dca5e730413453727bd2a86817a7')
