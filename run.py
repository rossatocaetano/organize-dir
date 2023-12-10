import os
from organize import Organize
from config import config

base_directory = config['dir']

if os.path.exists(base_directory):
    select_dir = Organize(base_directory)
    dir_checkpoint = select_dir.select_dir()
    select_dir.organize_dir(dir_checkpoint)
else:
    print(f"The directory '{base_directory}' does not exist.")