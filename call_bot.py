from vk_api.longpoll import VkEventType
from BOT import bot1
from VK_API import vk1


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
                    bot1.write_msg(event.user_id, f"Ищем)")
                else:
                    bot1.write_msg(event.user_id, "Не поняла вашего ответа...")

def iter_for_users

call_bot()