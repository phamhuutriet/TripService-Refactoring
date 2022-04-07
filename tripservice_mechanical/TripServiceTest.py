import unittest
from unittest.mock import Mock
from TripService import TripService
from UserNotLoggedInException import UserNotLoggedInException
from User import User
from Trip import Trip
from tripservice_mechanical.UserBuilder import UserBuilder


class TestableTripService(TripService):
    def __init__(self, logged_state, tripDAO):
        super().__init__(tripDAO)
        self.logged_state = logged_state

    def find_trip_by_user(self, user):
        return user.get_trips()


class TripServiceTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.UNLOGGED_USER = None
        self.LOGGED_USER = User()
        self.ANOTHER_USER = User()
        self.tripDAO = Mock()

    def test_should_throw_an_exception_when_the_user_is_not_logged_in(self):
        trip_service = TripService(self.tripDAO)

        with self.assertRaises(UserNotLoggedInException):
            trip_service.getTripsByUser(self.ANOTHER_USER, self.UNLOGGED_USER)

    def test_should_return_empty_trip_list_if_user_not_friend_with_logged_user(self):
        trip_service = TripService(self.tripDAO)
        friend = UserBuilder.aUser().friends_with(self.LOGGED_USER).with_trips().build()

        self.tripDAO.find_trip.return_value = friend.get_trips()

        self.assertEqual(len(trip_service.getTripsByUser(friend, self.LOGGED_USER)), 0)

    def test_should_return_a_len_1_trip_list_if_user_is_friend_with_logged_user(self):
        trip_service = TripService(self.tripDAO)
        friend = UserBuilder.aUser().friends_with(self.LOGGED_USER).with_trips(Trip()).build()

        self.tripDAO.find_trip.return_value = friend.get_trips()

        self.assertEqual(len(trip_service.getTripsByUser(friend, self.LOGGED_USER)), 1)

    def test_should_return_a_len_5_trip_list_if_user_is_friend_with_logged_user(self):
        trip_service = TripService(self.tripDAO)

        friend = UserBuilder.aUser() \
            .friends_with(self.LOGGED_USER) \
            .with_trips(Trip(), Trip(), Trip(), Trip()) \
            .build()

        self.tripDAO.find_trip.return_value = friend.get_trips()

        self.assertEqual(len(trip_service.getTripsByUser(friend, self.LOGGED_USER)), 4)


if __name__ == "__main__":
    unittest.main()
