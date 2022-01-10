
from vk_api.longpoll import VkEventType
from BOT import bot1
from VK_API import vk1

while True:
    i = 0
    q = 0
    data = [['111', '111', '111']]
    human_id = data[q][i][0]
    first_name = data[q][i][1]
    last_name = data[q][i][2]
    for event in bot1.longpoll_listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f"User_name: {vk1.user_get(event.user_id)['response'][0]['first_name']}")
            print(event.text)
            print('--------')
            rdb = {}
            user_id = event.user_id

            # print(event)
            if event.text == 'Начать':
                bot1.write_msg_hello(event.user_id)
                print(vk1.user_get(event.user_id))
            elif len(event.text) <= 2 and event.text != 'М' and event.text != 'Ж':
                rdb['age'] = event.text
                bot1.sex(event.user_id)
            elif event.text == 'Я парень':
                bot1.who_your_interesting(event.user_id)
            elif event.text == 'Я девушка':
                bot1.who_your_interesting(event.user_id)
            elif event.text == 'Девушка':
                bot1.where_your_life(user_id)
            elif event.text == 'Парень':
                bot1.where_your_life(user_id)

            elif event.text == 'М':
                human = vk1.users_search(2, vk1.user_get(event.user_id)['response'][0]['city']['id'],
                                         vk1.user_get(event.user_id)['response'][0]['bdate'][-4:])
                data.append(human)
                # i += 1
                q += 1
                human_id = data[1][0][0]
                first_name = data[1][0][1]
                last_name = data[1][0][2]
                if len(vk1.get_photo(human_id)) >= 3:
                    bot1.write_msg_3_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0], vk1.get_photo(human_id)[1],
                                           vk1.get_photo(human_id)[2])


                elif len(vk1.get_photo(human_id)) >= 2:
                    bot1.write_msg_2_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0], vk1.get_photo(human_id)[1])

                elif len(vk1.get_photo(human_id)) >= 1:
                    bot1.write_msg_1_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0])

                else:
                    bot1.write_msg_photo_not(len(vk1.get_photo(human_id)), event.user_id,
                                             f"{first_name} {last_name} https://vk.com/id{human_id}")



            elif event.text == 'Ж':
                human = vk1.users_search(1, vk1.user_get(event.user_id)['response'][0]['city']['id'],
                                         vk1.user_get(event.user_id)['response'][0]['bdate'][-4:])
                data.append(human)
                print('Data:', data)
                q += 1
                human_id = data[1][0][0]
                first_name = data[1][0][1]
                last_name = data[1][0][2]
                if len(vk1.get_photo(human_id)) >= 3:
                    bot1.write_msg_3_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0], vk1.get_photo(human_id)[1],
                                           vk1.get_photo(human_id)[2])


                elif len(vk1.get_photo(human_id)) >= 2:
                    bot1.write_msg_2_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0], vk1.get_photo(human_id)[1])

                elif len(vk1.get_photo(human_id)) >= 1:
                    bot1.write_msg_1_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0])

                else:
                    bot1.write_msg_photo_not(len(vk1.get_photo(human_id)), event.user_id,
                                             f"{first_name} {last_name} https://vk.com/id{human_id}")

            elif event.text == 'Дальше.':
                human_id = data[q][i + 1][0]
                first_name = data[q][i + 1][1]
                last_name = data[q][i + 1][2]

                if len(vk1.get_photo(human_id)) >= 3:
                    bot1.write_msg_3_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0], vk1.get_photo(human_id)[1],
                                           vk1.get_photo(human_id)[2])
                    i += 1
                elif len(vk1.get_photo(human_id)) >= 2:
                    bot1.write_msg_2_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0], vk1.get_photo(human_id)[1])
                    i += 1
                elif len(vk1.get_photo(human_id)) >= 1:
                    bot1.write_msg_1_photo(event.user_id, f"{first_name} {last_name} https://vk.com/id{human_id}",
                                           human_id,
                                           vk1.get_photo(human_id)[0])
                    i += 1
                else:
                    bot1.write_msg_photo_not(len(vk1.get_photo(human_id)), event.user_id,
                                             f"{first_name} {last_name} https://vk.com/id{human_id}")
                    i += 1
