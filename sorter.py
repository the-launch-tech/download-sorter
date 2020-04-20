#!/usr/bin/env python3

import os, time, shutil

times = 1
code_list = ['py', 'js', 'php', 'html', 'css', 'scss', 'ts', 'json', 'md']
media_list = ['png', 'jpg', 'svg', 'gif', 'm4a', 'mov', 'psd', 'eps', 'ai']
ext_list = ('docx', 'pkg', 'pptx', 'csv', 'xml', 'xls', 'txt', 'word', 'zip', 'wpress', 'directory', 'unknown', 'code', 'media')

src_dir = "/Users/danielgriffiths/Downloads"
category_dirs = dict([(ext, f"{src_dir}/{ext}-archive") for ext in ext_list])

def get_category_path(ext) :
    if ext in ext_list :
        return category_dirs[ext]
    elif ext in media_list :
        return category_dirs['media']
    elif ext in code_list :
        return category_dirs['code']
    elif ext :
        return category_dirs['unknown']
    else :
        return category_dirs['directory']

def move_object(object, destination_path) :
    src = f"{src_dir}/{object}"
    dest = f"{destination_path}/{object}"
    shutil.move(src, dest)

def make_if_not_exists(category_path) :
    if not os.path.exists(category_path) :
        os.makedirs(category_path)

while True:
    print(f'RUNNING {times} TIMES')
    for file in os.listdir(src_dir) :
        if file not in [f"{ext}-archive" for ext in ext_list] :
            name, ext = os.path.splitext(file)
            category_path = get_category_path(ext[1:])
            make_if_not_exists(category_path)
            move_object(object=file, destination_path=category_path)
    time.sleep(10)
    times += 1
