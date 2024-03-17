"""AC (acceptance criteria):

Filenames are passed as plain strings but they must be a Path objects in the concrete function that opens the file itself.
This code works pretty slowly. Change it using multithreading and multiprocessing as we did in the lesson
Add time counters and uncomment the print command in the try/except block. P.S. Use time.perf_counter.
The encryption could simulate the heavy task. No need to achieve the actual encryption
The image downloader MUST download the image for real.
P.S. You don't have to really encrypt the file for this homework but if you would like to practice more you might find this helpful

https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/

AC (Acceptance Criteria):

- Файли передаються як звичайні рядки, але вони повинні бути об'єктами шляху (Path objects)
у конкретній функції, яка відкриває файл сама по собі.

- Цей код працює досить повільно. Змініть його, використовуючи багатопоточність (multithreading)
та багатопроцесність (multiprocessing), як ми робили на уроці.

- Додайте лічильники часу і розкоментуйте команду друку (print) у блоку try/except. P.S. Використовуйте time.perf_counter().

- Шифрування може симулювати важку задачу. Не потрібно досягати фактичного шифрування.

- Завантажувач зображень МУСТ загружати зображення насправді.
P.S. Вам не потрібно дійсно шифрувати файл для цього домашнього завдання, але якщо ви хочете практикуватися більше, вам може бути корисно це:
https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/"""


import os
import threading
import time
from multiprocessing import Process
from pathlib import Path

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path):
    print(f"Processing file from {path} in process {os.getpid()}")
    # Just simulate a heavy computation
    _ = [i for i in range(100_000_000)]
    return path


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    return image_url


if __name__ == "__main__":
    time_for_start = time.perf_counter()

    # file paths
    file_path = "rockyou.txt"
    url_for_image = "https://picsum.photos/1000/1000"

    # multithreading for I/O-bound task
    download_thread = threading.Thread(
        target=download_image, args=(url_for_image,)
    )
    download_thread.start()

    # processing for CPU-bound task
    process = Process(target=encrypt_file, args=(Path(file_path),))
    process.start()

    download_thread.join()
    process.join()

    time_for_end = time.perf_counter()

    print(f"Time for taken = {time_for_end - time_for_start:.2f} seconds")
