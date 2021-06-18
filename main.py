__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import zipfile

def clean_cache():
    # If it already exists, it deletes everything in the cache folder
    if os.path.exists(cache_dir_path):
        with os.scandir(cache_dir_path) as files:
            for file in files:
                os.remove(file)
    # creates an empty folder cache in the current directory
    else:
        os.mkdir(cache_dir_path)
    return

def cache_zip(file_path, cache_dir_path):
    # unpack the indicated zip file into a clean cache folder.
    with zipfile.ZipFile(file_path, 'r') as zipobj:
        zipobj.extractall(path = cache_dir_path)
    return

def cached_files():
    # returns a list of all the files in the cache.
    cached_files  = []
    with os.scandir(cache_dir_path) as files:
        for file in files:
            # Files should be specified in absolute terms. No folders should be included in the list.
            if file.is_file():
                cached_files.append(os.path.abspath(file))
    return cached_files

def find_password(cached_files):
    # read the text in each file to see if the password is in there.
    # Once found, find_password should return this password string
    for filename in cached_files:
        with open(filename, "r") as file:
            for line in file:
                if 'password' in line:
                    find_password = line.split()[1]
    return find_password

current_dir = os.getcwd()
cache_dir = 'cache'
cache_dir_path = os.path.join(current_dir, cache_dir)
file_path = current_dir + '/data.zip'

if __name__ == '__main__':
    clean_cache()
    cache_zip(file_path, cache_dir_path)
    print(cached_files())
    cached_files = cached_files()
    print(find_password(cached_files))
