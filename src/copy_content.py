import os
import shutil

def copy_content():
    path = os.path.abspath(path='.')

    public_folder_exist = os.path.exists('./public')
    if public_folder_exist is False:
        os.mkdir("./public")

    static_folder_exist = os.path.exists('./static')
    folder_content = None
    if static_folder_exist:
        folder_content = os.listdir(path='./static')

    if folder_content != None:
        static_join_path = os.path.join(path, "static")
        public_join_path = os.path.join(path, "public")
        copy_files_and_folders(folder_content, static_join_path, public_join_path)
        return static_join_path
    else:
        return "The folder doesn't exist"

def copy_files_and_folders(content, src, dst):
    for item in content:
        new_item_path = src + f"/{item}"
        is_item_a_file = os.path.isfile(new_item_path)
        try:
            if is_item_a_file:
                shutil.copy(new_item_path, dst)
            else:
                os.mkdir(f"./public/{item}")
                folder_content = os.listdir(path=new_item_path)
                copy_files_and_folders(folder_content, new_item_path, f"{dst}/{item}")
        except:
            print("File already exist", item)
