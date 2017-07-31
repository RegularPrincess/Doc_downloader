import requests


# переданная функция event вызывается с именем загруженного файла
# path - куда сохранять
# url - откуда скачивать
def download_file(url, event, path=""):
    destination = url.split('/')[-1]
    file = requests.get(url)
    out = open(path + destination, "wb")
    out.write(file.content)
    out.close()
    event(destination)


def download_files(urls, event, path=""):
    for url in urls:
        download_file(url, event, path)


def _fake_event(file_name):
    pass