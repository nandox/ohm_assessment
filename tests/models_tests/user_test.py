from tests import OhmTestCase


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []


    def test_get_points_and_email(self):
        assert self.chuck.get_points_and_email() == "Points: 0 e-mail: test@test.com"
