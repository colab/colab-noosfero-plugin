
from django.test import TestCase, Client


class NoosferoTest(TestCase):

    def setUp(self):
        self.client = Client()
