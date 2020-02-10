'''
1. команда "расписание"00
'''

import csv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": get_random_id()})

token = "38bd49d5c8c80c9a708afaf884a59eb7822efc6111171a8a76983eded89079ee837844937a49e92fb720c"

vk = vk_api.VkApi(token=token)
answer = 0

longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    try:
        with open("logs.log","r") as f:

            if str(event.user_id) not in f.read():
                write_msg(event.user_id,'Привет. Приветсвую в группе киноклуба "Ок, бумер! ок, зумер". Для подробной информации напиши "Help"')

                with open("logs.log","a") as f:
                    f.write(str(event.user_id)+"\n")
                    print(event.user_id)
    except:
        pass
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            request = event.text

            if request.lower() == "help":
                with open("text/help.txt","r") as f:
                    write_msg(event.user_id,f.read())

            elif request.lower() == "привет":
                with open("text/help.txt","r") as f:
                    write_msg(event.user_id,"Привет! "+f.read())

            elif request.lower() == "подробнее":
                with open("text/info.txt","r") as f:
                    write_msg(event.user_id,f.read())

            elif request.lower() == "расписание":
                with open("schedule.csv","r") as csv_file:
                    csv_reader = csv.reader(csv_file)

                    next(csv_reader)

                    write_msg(event.user_id,"Мы будем смотреть:")

                    for line in csv_reader:
                        write_msg(event.user_id,line[1] + " в " + line[0] + " " + line[2])

                write_msg(event.user_id,"Если хочешь пойти и обсудить один из этих фильмов, то напиши нашему модератору https://vk.com/lika_dan")


            elif request.lower() == "код":
                write_msg(event.user_id,"https://github.com/PythonScriptPlusPlus/bzoomer_vk")

            else:
                write_msg(event.user_id, 'У меня нет такой команды. Чтобы узнать команды и что они делают, напиши "Help"')
