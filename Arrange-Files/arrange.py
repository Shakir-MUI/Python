import os
path = os.getcwd()
def arrange(folder_path):
    os.chdir(folder_path)
    folders = os.listdir()
    unique_folder = []
    for i in folders:
        folder = i.split('.')[-1]
        if folder not in unique_folder:
            unique_folder.append(folder)
            os.mkdir(folder)
        
    for i in folders:
        ext = i.split('.')[-1]
        old_path = os.path.join(folder_path,i)
        new_path = os.path.join(folder_path+"\\"+ext,i)
        os.rename(old_path,new_path)


arrange(path)