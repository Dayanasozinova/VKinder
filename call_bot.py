import time

from vk_api.longpoll import VkEventType
from BOT import bot1
from VK_API import vk1


def call_bot():
    for event in bot1.longpoll_listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request == "Ж":
                    for user in vk1.users_search(1, 60, 1999):
                        user_ = user[0]
                        first_name = user[1]
                        last_name = user[2]
                        print(first_name, last_name, vk1.get_photo(user_), len(vk1.get_photo(user_)))
                        # bot1.send_mes(len(vk1.get_photo(user_)))
                        if len(vk1.get_photo(user_)) >= 3:
                            bot1.write_msg_3_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{user_}", user_, vk1.get_photo(user_)[0], vk1.get_photo(user_)[1], vk1.get_photo(user_)[2])
                            time.sleep(5)
                        elif len(vk1.get_photo(user_)) >= 2:
                            bot1.write_msg_2_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{user_}", user_, vk1.get_photo(user_)[0], vk1.get_photo(user_)[1])
                            time.sleep(5)
                        elif len(vk1.get_photo(user_)) >= 1:
                            bot1.write_msg_1_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{user_}", user_, vk1.get_photo(user_)[0])
                            time.sleep(5)
                        else:
                            bot1.write_msg_photo_not(len(vk1.get_photo(user_)), event.user_id,
                                          f"{first_name} {last_name} https://vk.com/id{user_}")
                            time.sleep(5)

                        pass
                else:
                    bot1.write_msg(event.user_id, "Не поняла вашего ответа...")

call_bot()