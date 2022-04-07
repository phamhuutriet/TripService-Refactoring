from tripservice_mechanical.User import User


class UserBuilder():
    def __init__(self):
        self.friends = []
        self.trips = []

    @classmethod
    def aUser(cls):
        return UserBuilder()

    def friends_with(self, *friends):
        self.friends = friends
        return self

    def with_trips(self, *trips):
        self.trips = trips
        return self

    def build(self):
        new_user = User()
        self.add_friends_to(new_user)
        self.add_trips_to(new_user)
        return new_user

    def add_friends_to(self, new_user):
        for friend in self.friends:
            new_user.addFriend(friend)

    def add_trips_to(self, new_user):
        for trip in self.trips:
            new_user.addTrip(trip)