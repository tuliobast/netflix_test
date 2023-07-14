from seleniumbase import BaseCase

class LoginPageNetflix(BaseCase):
    path = 'https://www.netflix.com/ar/login'
    h1 = '//h1'
    xpath_email1 = '//*[@id="id_userLoginId"]'
    email = 'XXX'
    xpath_password = '//*[@id="id_password"]'
    password = 'Holamundo'
    checkbox = '//*[@class="ui-binary-input login-remember-me"]'

    def open_page(self):
        self.open(self.path)
    def verify_login(self):
        self.open_page()
        self.click(self.iniciar_sesion_btn)
        title = self.get_page_title()
        self.assertNotEquals(title, self.title_page)
        self.assert_text('Inicia sesión', self.h1)

    def verify_error_login(self):
        self.open_page()
        self.verify_login()
        self.add_text(self.xpath_email1, self.email)
        self.add_text(self.xpath_password, self.password)
        self.click(self.checkbox)