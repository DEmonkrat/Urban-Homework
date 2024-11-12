# ____________User class__________________________________________________
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.orig_pass = password

    def __repr__(self):
        return f'Пользователь: {self.nickname}, возраст: {self.age}'

    def __str__(self):
        return f'Пользователь: {self.nickname}, возраст: {self.age}'

    def get_params(self):
        return [self.nickname, self.age]

    def reg_params(self):
        return [self.nickname, self.orig_pass, self.age]

    def get_pass(self):
        return self.password


# ____________Video class__________________________________________________
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        if isinstance(duration, str):  # Если длительность строка, то "разбираем" на ч. и мин.
            time = duration.split(':')
            self.duration = int(time[0]) * 3600 + int(time[1]) * 60
        else:
            self.duration = duration  # Если длительность число, то поросто присваиваем
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        adult_status = ''  # Формируем сообщение о фильме с названием, длительностью и статусом
        adult_status = 'Фильм для взрослых (18+)' if self.adult_mode else 'Фильм для всей семьи'
        return f'Название: {self.title}. Длительность: {self.duration // 3600}:{self.duration % 3600 / 60:.0f} ч. ' + adult_status

    def data(self):
        return [self.title, self.duration, self.time_now, self.adult_mode]

    def set_tnow(self, time):
        self.time_now = time

    def inc_tnow(self, time):
        self.time_now += time


# ____________UrTube class__________________________________________________
class UrTube:
    def __init__(self, tube_title):
        self.title = tube_title
        self.users = {}  # Для удобства/быстроты поиска пользователей/фильмов введены словари.
        self.videos = {}  # Ключом является имя пользователя/название фильма, а значением соответствующий класс
        self.curent_user = None

    def log_in(self, nickname, password):  # _________login____________
        if nickname in self.users:  # Смотрим есть ли пользователь в списке Пользователей
            if self.users[nickname].get_pass() == hash(
                    password):  # Смотрим совпадают ли хэши паролей, если пользователь найден
                self.curent_user = self.users[nickname]  # Curent_user будет пользователь класса User
                self.cur_user()  # Вывести текущего пользователя
            else:  # Пароли не совпадают
                print('Пароль неверный, проверьте ввод данных (раскладка, CapsLock)')
        else:  # Пользователь не найден
            print(f'Пользователя с ником {nickname} не найдено')

    def register_u(self, nickname, password, age):  # _________register_____________
        if nickname in self.users:  # Если пользователь с таким ником уже сть
            print(f'Пользователь с ником {nickname} уже существует.')
            print(f'Проверьте данные или авторизуйтесь')
        else:
            self.users[nickname] = User(nickname, password, age)  # Создаем пользователя класса User
            # print(f'Зарегистрирован пользователь {self.users[nickname].get_params()[0]}')
            self.log_in(nickname, password)  # Автоматическая авторизация после регистрации

    def log_out(self):
        self.curent_user = None

    def add_v(self, *args_v):  # _______________add video_________________
        for object_v in args_v:
            if isinstance(object_v, Video):  # Проверяем объекты на принадлежность классу Video
                if object_v.data()[0] in self.videos:  # Смотрим есть ли название фильма в списке фильмов
                    print(f'Фильм с названием "{object_v.data()[0]}" уже есть в библиотеке')
                else:
                    self.videos[object_v.data()[0]] = object_v

    def get_videos(self, str_to_find):  # ___________get videos_______________
        vid_list = [title for title in self.videos.keys() if str_to_find.casefold() in title.casefold()]
        if vid_list:
            return vid_list
        else:
            return f'По параметрам "{str_to_find}" ничего не найдено'

    def watch_video(self, title):  # ___________watch videos_______________
        from time import sleep
        vid_to_wtch = self.videos.get(title, None)

        # _________________________________________________________________________
        def broadcast():  # Создадим ф-цию Трансляция, чтобы не писать одно и то же
            nonlocal vid_to_wtch
            print(f'Фильм {vid_to_wtch.data()[0]}.')
            print('Приятного просмотра')
            print('Время просмотра: ', end='')
            while vid_to_wtch.data()[2] < vid_to_wtch.data()[1]:
                print(vid_to_wtch.data()[2], end=' ')
                vid_to_wtch.inc_tnow(1000)
                sleep(.1)
            print(vid_to_wtch.data()[1])
            vid_to_wtch.set_tnow(0)  # Сброс текущего времени просмотра
            print('Конец просмотра')
            # _________________________________________________________________________

        if vid_to_wtch:  # Проверка на наличие фильма
            if self.curent_user != None:  # Фильм есть. Проверка на авторизацию
                if vid_to_wtch.data()[3]:  # Фильм есть. Авторизован. Проверка на adult
                    if self.curent_user.get_params()[1] >= 18:  # Пройдены все проверки
                        broadcast()
                    else:  # Фильм есть. Авторизован. НЕТ 18 ЛЕТ !
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:  # Фильм есть. Авторизован. Проверка на adult не требуется
                    broadcast()
            else:  # Фильм есть. НЕ АВТОРИЗОВАН !
                print('Войдите в аккаунт, чтобы смотреть видео')
        else:  # Фильм НЕ НАЙДЕН !
            print(f'Фильм {title} не обнаружен')

    def cnt_users(self):
        return len(self.users)

    def all_users(self):  # _______________list all users_________________
        print('Пользователи:')
        if not self.users:
            print('Отсутствуют')
        else:
            for u_data in self.users.values():
                print(f'Ник: {u_data.get_params()[0]}, возраст: {u_data.get_params()[1]}')

    def all_videos(self):  # _______________list all videos_________________
        print('Фильмы:')
        if not self.videos:
            print('Отсутствуют')
        else:
            for v_data in self.videos.values():
                # print(f'Название: {v_data.data()[0]}, длительность: {v_data.data()[1]//3600}:{v_data.data()[1]%3600/60:.0f} ч.')
                print(v_data)

    def cnt_videos(self):
        return len(self.videos)

    def cur_user(self):
        if self.curent_user:
            print(f'Текущий пользователь: {self.curent_user.get_params()[0]}')
        else:
            print('Пользователь не авторизован')


print('Создаем 3 пользоватлей')
user_1 = User('DEmon', 'Password', 40)
user_2 = User('Oleg', 'Password_1', 29)
user_3 = User('Dasha', 'Pswrd', 6)

print(user_1)
print(user_2)
print(user_3)
print()

print('Создаем 2 видео')
vid_1 = Video('Маугли', '1:48')
vid_2 = Video('Аватар XXX', 9300, adult_mode=True)
print(vid_1)
print(vid_2)
print()

print('Создаем канал YouTube')
youtube = UrTube('YouTube')
youtube.all_users()
print()

print('Регистрируем 3 пользователей')
youtube.register_u(*user_1.reg_params())
youtube.all_users()
print('_______________________________')
youtube.register_u(*user_2.reg_params())
youtube.all_users()
print('_______________________________')
youtube.register_u(*user_3.reg_params())
youtube.all_users()
print('_______________________________')
print('Проверяем на повторную регистрацию 1-ого пользователя')
youtube.register_u(*user_1.reg_params())
print()

print('Проверяем корректный/некорректный логин/пароль')
youtube.log_in('Masha', 'SuperParoll')
youtube.log_in('DEmon', 'Pass')
youtube.log_in('DEmon', 'Password')
youtube.log_in('Oleg', 'Password_1')
print('Проверяем logut')
youtube.log_out()
youtube.cur_user()
print()

print('Проверяем корректность добавления фильмов')
youtube.all_videos()
print('_______________________________')
youtube.add_v(vid_1, vid_2, user_1, 234, 'sdfd', Video('Для чего девушкам парень программист?', 1000, adult_mode=True),
              Video('Urban the best', 5600))
youtube.all_videos()
print()

print(f'Всего фильмов: {youtube.cnt_videos()}')
print(f'Всего пользователей: {youtube.cnt_users()}')
print()

print('Проверяем корректность поиска метода get_videos')
print('Ищем: ПАР')
print(youtube.get_videos('ПАР'))
print('Ищем: UrbaN')
print(youtube.get_videos('UrbaN'))
print('Ищем: !')
print(youtube.get_videos('!'))
print('Ищем: А')
print(youtube.get_videos('А'))
print()

print('Проверяем работу метода watch_video')
youtube.cur_user()
youtube.watch_video('Аватар')
youtube.watch_video('Маугли')
youtube.log_in('Dasha', 'Pswrd')
youtube.watch_video('Маугли')
print('Попытка просмотра Дашей фильма для взрослых')
youtube.watch_video('Аватар XXX')
print('_______________________________')
youtube.log_in('DEmon', 'Password')
youtube.watch_video('Аватар XXX')
youtube.videos['Маугли'].data()
