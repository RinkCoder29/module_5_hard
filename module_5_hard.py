import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def hash_pass(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_pass = self.hash_pass(password)
        for i in self.users:
            if i.nickname == nickname and i.password == hashed_pass:
                self.current_user = i
                print(f"Пользователь {nickname} вошел успешно")
                return
        print("Неверное имя пользователя или пароль")

    def register(self, nickname, password, age):
        if any(i.nickname == nickname for i in self.users):
            print(f"Пользоваетель {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} регистрацию прошел и вошел ")

    def long_out(self):
        print(f"Пользователь {self.current_user.nikname} вышел из системы")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(j.title == video.title for j in self.videos):
                self.videos.append(video)
                print(f"Видео {video.title} добавлено")
            else:
                print(f"Видео {video.title} существет")

    def get_videos(self, search_word):
        return [video.title for video in self.videos
                if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((j for j in self.videos if j.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Просмотр видео '{video.title}':")
        for k in range(video.time_now, video.duration):
            print(f"Секунда {k + 1}")
            time.sleep(1)
        video.time_now = 0
        print("Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

