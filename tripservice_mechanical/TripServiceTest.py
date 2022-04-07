import unittest
from TripService import TripService
from UserNotLoggedInException import UserNotLoggedInException
from DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException
from tripservice import User


class TestableTripService(TripService):
    def __init__(self, logged_state) -> None:
        super().__init__()
        self.logged_state = logged_state

    def get_logged_user(self):
        return self.logged_state


class TripServiceTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.UNLOGGED_USER = None
        self.LOGGED_USER = User()
        self.ANOTHER_USER = User()

    def test_should_throw_an_exception_when_the_user_is_not_logged_in(self):
        trip_service = TestableTripService(logged_state=self.UNLOGGED_USER)

        with self.assertRaises(UserNotLoggedInException):
            trip_service.getTripsByUser(self.ANOTHER_USER)

    def test_should_return_empty_trip_list_if_user_dont_have_friend(self):
        trip_service = TestableTripService(logged_state=self.LOGGED_USER)

        friend = User()
        friend.addFriend(self.ANOTHER_USER)

        self.assertEqual(len(trip_service.getTripsByUser(friend)), 0)


if __name__ == "__main__":
    unittest.main()
