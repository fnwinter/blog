---
layout: post
title: "python detecting duplicated file"
author: "jungjik.lee"
categories: article
tags: [python]
---

# Python으로 중복 파일 찾는 스크립트

## 사진 중에 중복 파일이 있는지 확인이 필요해서 ChatGPT를 활용해 구현함

~~~python
import os
import sys
import hashlib

folder_dict = {}
hash_dict = {}

def calculate_checksum(file_path, algorithm="md5"):
    if algorithm == "md5":
        hash_algorithm = hashlib.md5()
    elif algorithm == "sha1":
        hash_algorithm = hashlib.sha1()
    elif algorithm == "sha256":
        hash_algorithm = hashlib.sha256()
    else:
        raise ValueError("Unsupported algorithm."
                         " Please choose md5, sha1, or sha256.")

    if os.path.exists(file_path):
        checksum = None
        try:
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    hash_algorithm.update(chunk)
                checksum = hash_algorithm.hexdigest()
        except Exception as e:
            print(e)
        return checksum
    return "not exists"

def recursive_file_search(path):
    _path = os.path.abspath(path)
    for root, _, files in os.walk(_path):
        for file in files:
            folder = folder_dict.get(root)
            file_path = os.path.join(root, file)
            hash_value = calculate_checksum(file_path, "md5")
            if not hash_dict.get(hash_value):
                hash_dict[hash_value] = [folder, file]
            else:
                print("found duplicated file", file_path)

def recursive_folder_search(path):
    _path = os.path.abspath(path)
    index_no = 0
    for root, dirs, _ in os.walk(_path):
        for dir in dirs:
            index_no += 1
            dir_path = os.path.join(root, dir)
            folder_dict[dir_path] = index_no
    print(f"folder count {index_no}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)
    current_directory = sys.argv[1]
    print(current_directory)
    recursive_folder_search(current_directory)
    recursive_file_search(current_directory)
~~~

## ChatGPT로 필요 구현을 물어보니까 예제 코드를 쏙쏙 뽑아줘 너무 편하게 구현했다.
## 이래서 GitHub Copilot 를 쓰나보다.