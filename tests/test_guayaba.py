import unittest

from common.guayaba import _guayaba


class GuayabaTest(unittest.TestCase):
    def setUp(self):
        # self.task = Task("Dummy task", False)
        pass

    def tearDown(self):
        # To be implemented if required
        pass

    def test_guayaba(self):
        self.assertEqual(
            _guayaba("green", "blue"), {"argA": "green", "argB": "blue"}
        )
