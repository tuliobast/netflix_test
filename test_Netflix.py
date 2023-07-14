from page_objects.index import HomePageNetflix
from page_objects.login import LoginPageNetflix
from page_objects.test import TagNameTest

import random_mail
from random_mail import *

class NetflixTest(HomePageNetflix, LoginPageNetflix, TagNameTest):
    generador = random_mail.GeneradorCorreo()

    def setUp(self):
        super().setUp()
        self.wait(2)
        self.maximize_window()

    def test_validarTituloTest(self):
        self.verify_title()

    def test_startSessionPageTest(self):
        self.verify_login()

    def test_loginToNetflixError(self):
        self.verify_error_login()

    def test_fake_email(self):
        self.verify_fake_email()

    def test_tag_names(self):
        self.print_tags_names('input')

    def tearDown(self):
        super().tearDown()


