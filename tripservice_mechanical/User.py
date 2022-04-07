from Trip import Trip;


class User:

    def __init__(self):
        self.trips = []
        self.friends = []

    def getFriends(self):
        return self.friends

    def addFriend(self, user):
        self.friends.append(user)

    def addTrip(self, trip):
        self.trips.append(trip)

    def get_trips(self):
        return self.trips

    def is_friend_with(self, user):
        return any(friend is self for friend in user.getFriends())
