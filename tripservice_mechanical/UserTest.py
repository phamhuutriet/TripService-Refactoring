import unittest

from tripservice_mechanical.UserBuilder import UserBuilder
from tripservice_mechanical.User import User


class UserTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.BOB = User()
        self.PAUL = User()
        self.ANOTHER_USER = User()

    def test_should_return_true_when_user_is_friend_with_another_user(self):
        user = UserBuilder.aUser().friends_with(self.BOB).build()

        self.assertEqual(self.BOB.is_friend_with(user), True)

    def test_should_return_false_when_user_is_not_friend(self):
        user = UserBuilder.aUser().friends_with(self.BOB).build()

        self.assertEqual(self.PAUL.is_friend_with(user), False)


if __name__ == "__main__":
    unittest.main()