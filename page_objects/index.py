from seleniumbase import BaseCase
import random_mail

class HomePageNetflix(BaseCase):
    path = 'https://www.netflix.com/ar'
    title_page = 'Netflix Argentina: Ve series online, ve películas online'
    iniciar_sesion_btn = '//a[@role="button"]'
    xpath_email2 = '(//input)[1]'
    comenzar_btn = '(//*[@type="submit"])[1]'
    generador = random_mail.GeneradorCorreo()

    def open_page(self):
        self.open(self.path)
    def verify_title(self):
        self.open_page()
        self.assert_title(self.title_page)

    def verify_fake_email(self):
        self.open_page()
        email = self.generador.generar_correo_aleatorio()
        print('\n'+ email+ '\n')
        self.add_text(self.xpath_email2, email)
        self.click(self.comenzar_btn)
        current_url = self.get_current_url()
        print(current_url)
        self.assert_url_contains('signup')