import unittest
from app.models import Writer

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = Writer(password = '123')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)