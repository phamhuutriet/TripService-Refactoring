from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def __init__(self, tripDAO):
        self.tripDAO = tripDAO

    def getTripsByUser(self, user, logged_user):
        self.validate(logged_user)

        return self.find_trip_by_user(user) if logged_user.is_friend_with(user) else self.no_trip()

    def find_trip_by_user(self, user):
        return self.tripDAO.find_trip(user)

    def no_trip(self):
        return []

    def validate(self, logged_user):
        if not logged_user:
            raise UserNotLoggedInException()