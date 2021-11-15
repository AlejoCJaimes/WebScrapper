import os
from pathlib import Path
 
 
def get_file_size(file_path):
    size = os.path.getsize(file_path)
    return size
 
 
def get_file_size_2(file):
    stat = os.stat(file)
    size = stat.st_size
    return size
 
 
def get_file_size_3(file):
    size = Path(file).stat().st_size
    return size
 
 
def convert_bytes(size, unit=None):
    if unit == "KB":
        return print('File size: ' + str(round(size / 1024, 3)) + ' Kilobytes')
    elif unit == "MB":
        return print('File size: ' + str(round(size / (1024 * 1024), 3)) + ' Megabytes')
    elif unit == "GB":
        return print('File size: ' + str(round(size / (1024 * 1024 * 1024), 3)) + ' Gigabytes')
    else:
        return print('File size: ' + str(size) + ' bytes')
 
 
 
file = 'ds_saber_11_2020_1_141120211727.csv'
 
print("Using 1st method : ")
size = get_file_size(file)
 
convert_bytes(size)
convert_bytes(size, "KB")
convert_bytes(size, "MB")
convert_bytes(size, "GB")
 
print("Using Second method : ")
size = get_file_size_2(file)
 
convert_bytes(size)
convert_bytes(size, "KB")
convert_bytes(size, "MB")
convert_bytes(size, "GB")
 
print("Using third method : ")
size = get_file_size_3(file)
 
convert_bytes(size)
convert_bytes(size, "KB")
convert_bytes(size, "MB")
convert_bytes(size, "GB")