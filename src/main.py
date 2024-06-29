from generate_page import generate_page, generate_page_recursive
from textnode import TextNode

def main():

    from_path = "./content/index.md"
    template_path = "./templates/template.html"
    dest_path = "./public/"
    # generate_page(from_path, template_path, dest_path)
    generate_page_recursive("./content", template_path, dest_path)

main()

