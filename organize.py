import os
from config import config

class Organize:

    def __init__(self, dir):
        self.dir = dir
        self.max_len = config['max_len']

    def select_dir(self):
        files_dir = self.dir
        files_list = os.listdir(files_dir)
        os.chdir(files_dir)
        return files_list

    def organize_dir(self, files_list):
        cont = 1
        for file in files_list:
            save_file_name = file
            file_name_and_extension = file.split('.')
            file_extension = file_name_and_extension[-1]

            print('-'*20)
            print(f'FILE: {cont}\nNAME: {save_file_name}')

            if len(file_extension) > self.max_len or '.' not in save_file_name:
                file_extension = None

            print(f'FILE EXTENSION: {file_extension}')      

            if file_extension:
                if not os.path.exists(file_extension):
                    path = os.path.join(self.dir,file_extension)
                    os.makedirs(path, exist_ok=True)
                    print(f'ACTION: create dir {path}')
                try:
                    os.rename(f'{file}', f'{file_extension}/{file}')
                    print(f'ACTION: {file} was moved to {file_extension}')
                except Exception as e:
                    print(f'NOTE: Xiii, there are some error here. Error: {e}')
            else:
                print(f'ACTION: None')
                print(f'NOTE: File {file} is a directory')
            print(f'END FILE: {cont}')
            cont = cont + 1

            
        print('-' * 20)
        print('Work Done! :)')

