class Textnode:

    def __init__(self, text, text_type, url):

        self.text = text
        self.text_type = text_type
        self.url = url

    def is_equal(self, other):
        return self.__eq__(other)

    def __repr__(self) -> str:
        return f"Text: {self.text} Type: {self.text_type} Url:{self.url}"

