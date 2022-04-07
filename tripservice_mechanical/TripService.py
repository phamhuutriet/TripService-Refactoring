from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user):
        logged_user = self.get_logged_user()

        if not logged_user:
            raise UserNotLoggedInException()

        if logged_user.is_friend_with(user):
            return self.find_trip_by_user(user)

        return []

    def get_logged_user(self):
        return UserSession.getInstance().getLoggedUser()

    def find_trip_by_user(self, user):
        return TripDAO.findTripsByUser(user)
