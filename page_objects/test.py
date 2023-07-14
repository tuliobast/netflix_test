from seleniumbase import BaseCase

class TagNameTest(BaseCase):
    url = 'https://www.netflix.com/ar'

    def print_tags_names(self, tagName):
        self.open(self.url)
        elements = self.find_elements(tagName)
        if elements:
            print('\n')
            for element in elements:
                print(element.tag_name)
        else:
            print("No se encuentran elementos con esta etiqueta")

