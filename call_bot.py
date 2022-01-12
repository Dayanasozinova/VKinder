
from vk_api.longpoll import VkEventType
from BOT import bot1
from Data import registration, users_search_db, usdb, iddb
from VK_API import vk1

while True:
    i = 0
    q = 0
    data = [['111', '111', '111']]
    human_id = data[q][i][0]
    first_name = data[q][i][1]
    last_name = data[q][i][2]
    dbuser_get = []
    rdb = {}
    dbid = []

    for event in bot1.longpoll_listen():
        if event.type == VkEventType.MESSAGE_NEW:

            user_id = event.user_id
            dbuser_get.append(vk1.user_get(event.user_id))

            print(f"{dbuser_get[0]['response'][0]['first_name']} {dbuser_get[0]['response'][0]['last_name']}:", event.text)
            if event.text == 'Начать':
                'BOT', bot1.write_msg_hello(event.user_id)

            elif len(event.text) <= 2 and event.text != 'М' and event.text != 'Ж':
                rdb['age'] = 2022 - int(event.text)
                print(rdb['age'])
                if 'city' in dbuser_get[0]['response'][0].keys():
                    registration(dbuser_get[0]['response'][0]['id'], dbuser_get[0]['response'][0]['first_name'],
                                 dbuser_get[0]['response'][0]['last_name'], dbuser_get[0]['response'][0]['sex'],
                                 dbuser_get[0]['response'][0]['bdate'][-4:],
                                 dbuser_get[0]['response'][0]['city']['title'])
                else:
                    registration(dbuser_get[0]['response'][0]['id'], dbuser_get[0]['response'][0]['first_name'],
                                 dbuser_get[0]['response'][0]['last_name'], dbuser_get[0]['response'][0]['sex'],
                                 dbuser_get[0]['response'][0]['bdate'][-4:], 0,
                                 dbuser_get[0]['response'][0]['home_town'])
                bot1.sex(event.user_id)
            elif event.text == 'Я парень':
                if 'city' in dbuser_get[0]['response'][0].keys():
                    bot1.where_your_life(user_id, dbuser_get[0]['response'][0]['city']['title'])
                    bot1.who_your_interesting(event.user_id)
                else:
                    bot1.where_your_life(user_id, dbuser_get[0]['response'][0]['home_town'])
                    bot1.who_your_interesting(event.user_id)
            elif event.text == 'Я девушка':
                if 'city' in dbuser_get[0]['response'][0].keys():
                    bot1.where_your_life(user_id, dbuser_get[0]['response'][0]['city']['title'])
                    bot1.who_your_interesting(event.user_id)
                else:
                    bot1.where_your_life(user_id, dbuser_get[0]['response'][0]['home_town'])
                    bot1.who_your_interesting(event.user_id)


            elif event.text == 'Парень':
                if 'city' in dbuser_get[0]['response'][0].keys():
                    human = vk1.users_search(2, dbuser_get[0]['response'][0]['city']['title'],
                                         rdb['age'])
                    data.append(human)
                    if event.user_id in iddb():
                        pass
                    else:
                        users_search_db(event.user_id, human)


                else:
                    human = vk1.users_search(2, dbuser_get[0]['response'][0]['home_town'],
                                             dbuser_get[0]['response'][0]['bdate'][-4:])
                    data.append(human)
                    if event.user_id in iddb():
                        pass
                    else:
                        users_search_db(event.user_id, human)
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
                    bot1.write_msg_photo_not( event.user_id,
                                             f"{first_name} {last_name} https://vk.com/id{human_id}")



            elif event.text == 'Девушка':
                if 'city' in dbuser_get[0]['response'][0].keys():
                    human = vk1.users_search(1, dbuser_get[0]['response'][0]['city']['title'],
                                             rdb['age'])
                    data.append(human)
                    if event.user_id in iddb():
                        pass
                    else:
                        users_search_db(event.user_id, human)
                else:
                    human = vk1.users_search(1, dbuser_get[0]['response'][0]['home_town'],
                                             dbuser_get[0]['response'][0]['bdate'][-4:])
                    data.append(human)
                    if event.user_id in iddb():
                        pass
                    else:
                        users_search_db(event.user_id, human)
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


                if human_id in usdb(event.user_id):
                    i += 1
                    pass
                else:
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
