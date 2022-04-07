import unittest
from TripService import TripService
from UserNotLoggedInException import UserNotLoggedInException
from DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException

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

  def test_should_throw_an_exception_when_the_user_is_not_logged_in(self):
    trip_service = TestableTripService(self.UNLOGGED_USER)

    with self.assertRaises(UserNotLoggedInException):
      trip_service.getTripsByUser(self.UNLOGGED_USER)  
  
  
    
if __name__=="__main__":
  unittest.main()