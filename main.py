from organize import Organize

#insert in the 'dir' variable the directory to organize as the model
#dir = r"C:\Users\my_user\paste-to-organize

dir = 'insert the directory path as insctructions above'
select_dir = Organize(dir)
dir_checkpoint = select_dir.select_dir()
select_dir.organize_dir(dir_checkpoint)