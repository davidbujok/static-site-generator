from logging import raiseExceptions
import os
from markdownblocks import markdown_to_blocks, markdown_to_html_node

class NoTitleError(Exception):
    pass

def extract_title(blocks):
    for block in blocks:
        if block.startswith("# "):
            return block.lstrip("#")
    raise NoTitleError("Markdown missing heading \"#\"")

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from { from_path } to { dest_path } using { template_path }")
    file_name = from_path.split("/")[-1]
    html_file_name = file_name.split(".")[0] + ".html"
    new_file_path = os.path.join(dest_path, html_file_name)

    markdown_file = open(from_path)
    markdown_read = markdown_file.read()
    title = extract_title(markdown_to_blocks(markdown_read))
    html_nodes = markdown_to_html_node(markdown_read)
    html_files = html_nodes.to_html()
    markdown_file.close()

    template_file = open(template_path)
    template_read = template_file.read()
    replace_title = template_read.replace("{{ Title }}", title)
    template_file.close()
    replace_content = replace_title.replace("{{ Content }}", html_files)
    
    if (new_file_path):
        html_file = open(new_file_path, "w").close()
        html_file = open(new_file_path, "a")
        html_file.write(replace_content)
        html_file.close()
    else:
        html_file = open(new_file_path, "a")
        html_file.write(replace_content)
        html_file.close()


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):

    content = os.listdir(dir_path_content)
    if (content):
        for file in content:
            path_to_file = os.path.join(dir_path_content, file)
            if (os.path.isfile(os.path.join(dir_path_content, file))):
                generate_page(path_to_file, template_path, dest_dir_path)
            else:
                folder_name = path_to_file.split("/")[-1]
                new_dest_folder_name = os.path.join(dest_dir_path, folder_name)
                if not os.path.isdir(new_dest_folder_name):
                    os.mkdir(new_dest_folder_name)
                path_to_folder = path_to_file
                generate_page_recursive(path_to_folder, template_path, new_dest_folder_name)
