import unittest
from TripDAO import TripDAO
from User import User
from DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException


class TripDAOTest(unittest.TestCase):

    def test_should_raise_exception_when_find_trip(self):
        with self.assertRaises(DependendClassCallDuringUnitTestException):
            TripDAO().find_trip(User())


if __name__ == "__main__":
    unittest.main()