from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user, logged_user):
        if not logged_user:
            raise UserNotLoggedInException()

        return self.find_trip_by_user(user) if logged_user.is_friend_with(user) else []

    def find_trip_by_user(self, user):
        return TripDAO.findTripsByUser(user)
