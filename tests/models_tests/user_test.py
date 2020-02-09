from tests import OhmTestCase


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []


    def test_get_points_and_email(self):
        assert self.chuck.get_points_and_email() == "Points: 5000 e-mail: test@test.com"

    def test_is_below_tier(self):
        assert self.chuck.is_below_tier('silver')
        assert self.chuck.is_below_tier('bronze')
        assert self.chuck.is_below_tier('carbon') is False
        assert self.justin.is_below_tier('bronze') is False
        assert self.justin.is_below_tier('silver') is False
