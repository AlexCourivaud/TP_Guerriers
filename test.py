import unittest
from code.avatarClass import Avatar
from code.warrior_Class import Warrior
from code.thief_Class import Thief
from code.wizard_Class import Wizard
from code.shop_Class import Merchant

class TestAvatar(unittest.TestCase):
    def test(self):
        test_avatar = Avatar(name="Roger", life=100, power=20, magic=0, gold=1000, potion = 10)
        self.assertEqual(test_avatar.name, "Roger", "wrong input for the name")


if __name__ == '__main__':
    unittest.main()