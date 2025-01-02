import os

directory_path = '/python/chapter-1-ps'

contents =os.listdir(directory_path)

for item in contents:
    print(item)