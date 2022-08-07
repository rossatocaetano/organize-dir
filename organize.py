import os

class Organize:

    def __init__(self, dir):
        self.dir = dir

    def select_dir(self):
        files_dir = self.dir
        files_list = os.listdir(files_dir)
        os.chdir(files_dir)
        return files_list

    def organize_dir(self, files_list):
        for file in files_list:
            file_name_and_extension = file.split('.')
            file_extension = file_name_and_extension[-1]

            if not os.path.exists(file_extension):
                path = os.path.join(self.dir,file_extension)
                os.makedirs(path, exist_ok=True)
            else:
                print('This file is a directory')
            try:
                os.rename(f'{file}', f'{file_extension}/{file}')
            except Exception as e:
                print(f'Xiii, there are some error here. Error: {e}')
            
        print('-' * 10)
        print('Work Done! :)')

