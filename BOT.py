from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from settings import token_app
vk = vk_api.VkApi(token_app)
longpoll = VkLongPoll(vk)

keyboard = VkKeyboard(one_time=True)

class BOT:
    def __init__(self, token):
        self.vk = None
        self.token = token


    def empty_mes(self, user_id):
        self.vk.method('messages.send', {'user_id': user_id, 'message': "✅",
                                         'random_id': randrange(10 ** 7),
                                         'keyboard': keyboard.get_empty_keyboard()})
    def write_msg_hello(self, user_id):
        self.vk.method('messages.send', {'user_id': user_id, 'message': f"Привет. Я помогу тебе найти пару мечты."
                                                                        f"Давай заполним твою анкету."
                                                                        f"Сколько тебе лет?",
                                         'random_id': randrange(10 ** 7)})
    def sex(self, user_id):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Я девушка', VkKeyboardColor.SECONDARY)
        keyboard.add_button('Я парень', VkKeyboardColor.SECONDARY)
        self.vk.method('messages.send', {'user_id': user_id, 'message': f"Какой у тебя пол?",
                                         'random_id': randrange(10 ** 7),
                                         'keyboard': keyboard.get_keyboard()})

    def who_your_interesting(self, user_id):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Девушка', VkKeyboardColor.SECONDARY)
        keyboard.add_button('Парень', VkKeyboardColor.SECONDARY)
        self.vk.method('messages.send', {'user_id': user_id, 'message': f"Кто тебе интересен?",
                                         'random_id': randrange(10 ** 7),
                                         'keyboard': keyboard.get_keyboard()})
    def where_your_life(self,user_id, city):

        self.vk.method('messages.send', {'user_id': user_id, 'message': f"Найдем тебе пару в городе {city}.",
                                         'random_id': randrange(10 ** 7)})
    def longpoll_listen(self):
        self.vk = vk_api.VkApi(token=self.token)
        return VkLongPoll(self.vk).listen()

    def write_msg_photo_not(self, user_id, message):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Дальше.', VkKeyboardColor.POSITIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'keyboard': [keyboard.get_empty_keyboard(), keyboard.get_keyboard()]})


    def write_msg_3_photo(self, user_id, message, owner_id, media_id1, media_id2, media_id3):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Дальше.', VkKeyboardColor.POSITIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': [f'photo{owner_id}_{media_id1}, '
                                                       f'photo{owner_id}_{media_id2},'
                                                       f'photo{owner_id}_{media_id3}'],
                                         'keyboard': keyboard.get_keyboard()})

    def write_msg_2_photo(self, user_id, message, owner_id, media_id1, media_id2):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Дальше.', VkKeyboardColor.POSITIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': [f'photo{owner_id}_{media_id1}, '
                                                       f'photo{owner_id}_{media_id2}'],
                                         'keyboard': keyboard.get_keyboard()})

    def write_msg_1_photo(self, user_id, message, owner_id, media_id1):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Дальше.', VkKeyboardColor.POSITIVE)
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),
                                         'attachment': [f'photo{owner_id}_{media_id1}'],
                                         'keyboard': keyboard.get_keyboard()})

    def send_mes(self, user_id, text, keyboard=None, template=None):
        self.vk.method('messages.send', {'user_id': user_id, 'message': text,
                                         'random_id': randrange(10 ** 7),
                                         'keyboard': keyboard,
                                         'template': template})


bot1 = BOT('0059adfe554cc8f08cad4a866d8875065d4bff6dc4ba9cf31daab47c1dca5e730413453727bd2a86817a7')
