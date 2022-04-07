from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user):
        logged_user = self.get_logged_user()
        isFriend = False
        tripList = []
        if logged_user:
            isFriend = self.is_friend(user, logged_user)
            if isFriend:
                tripList = self.find_trip_by_user(user)
            return tripList
        else:
            raise UserNotLoggedInException()

    def get_logged_user(self):
        return UserSession.getInstance().getLoggedUser()

    def find_trip_by_user(self, user):
        return TripDAO.findTripsByUser(user)

    def is_friend(self, user, logged_user):
        return any(friend is logged_user for friend in user.getFriends())