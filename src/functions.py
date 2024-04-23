import re

def extract_markdown_images(text):
    copy_text = text
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", copy_text)
    return matches
        
def extract_markdown_links(text):
    copy_text = text
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", copy_text)
    return matches
