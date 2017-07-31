import csv_reader as cd
import file_downloader as fd


def loaded_event(file_name):
    print('Загружено: ' + file_name)


PREFIX = "http://www.ciur.ru"
doc = cd.pars_csv("../blz_ds_koj_UTF-8.csv")
print(doc.keys())
for i, file_size in doc['size']:
    f_size_dot = file_size.replace(',', '.')
    if float(f_size_dot) > 2:
        fd.download_file(PREFIX + doc['url'][i], loaded_event)

