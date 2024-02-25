# each social channel has a type and the current number of followers
# кожен соціальний канал має типта поточну кількість фолловерів
# SocialChannel = tuple[str, int] =

# each post has a message and the timestamp when it should be posted
# кожен допис має повідомлення та відмітку часу, коли його слід опублікувати
# Post = tuple[str, int]


# 1 класи мають бути використані замість кортежів для представлення соціальних каналів та повідомлень.
# в якості початкової точки використовуйте код, доступний для завантаження для цього вправи.

# 2 функція post_a_message покращена. Умовний оператор має перевіряти кожен різновид соціальної
# мережі і потім викликати відповідний метод. Якщо ви хочете додати підтримку нової соціальної мережі,
# вам потрібно буде додати додатковий блок elif, що робить код все більш заплутаним і важким для читання.

# 3 нова версія коду використовує абстракцію для вирішення проблеми.
# def post_a_message(channel: SocialChannel, message: str) -> None:
#     type, _ = channel
#     if type == "youtube":
#         post_to_youtube(channel, message)
#     elif type == "facebook":
#         post_to_facebook(channel, message)
#     elif type == "twitter":
#         post_to_twitter(channel, message)


# def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
#     for post in posts:
#         message, timestamp = post
#         for channel in channels:
#             if timestamp <= time():
#                 post_a_message(channel, message)

from abc import ABC, abstractmethod
from dataclasses import dataclass
from time import time


@dataclass
class SocialChannel(ABC):
    type: str
    followers: int

    @abstractmethod
    def post(self, message: str):
        pass


class YouTubeChannel(SocialChannel):
    def post(self, message: str):
        print(f"Post on YouTube: {message}")


class FacebookChannel(SocialChannel):
    def post(self, message: str):
        print(f"Post on Facebook: {message}")


class TwitterChannel(SocialChannel):
    def post(self, message: str):
        print(f"Post on Twitter: {message}")


@dataclass
class Post:
    message: str
    timestamp: int


def post_a_message(channel: SocialChannel, message: str) -> None:
    channel.post(message)


def process_schedule(posts: list, channels: list) -> None:
    current_time = time()
    for post in posts:
        if post.timestamp <= current_time:
            for channel in channels:
                post_a_message(channel, post.message)


# if __name__ == "__main__":
#     youtube_channel = YouTubeChannel("youtube", 3300)
#     facebook_channel = FacebookChannel("facebook", 4300)
#     twitter_channel = TwitterChannel("twitter", 560)

#     channels = [youtube_channel, facebook_channel, twitter_channel]

#     # get time now
#     current_time = int(time())

#     posts = [
#         Post("message for YouTube", current_time), #post now
#         Post("message for Facebook", current_time - 3600), #post 1 hour ago
#         Post("message for Twitter", current_time - 7200), #post 2 hour ago
#     ]

#     process_schedule(posts, channels)
