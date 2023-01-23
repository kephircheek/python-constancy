import unittest
from operator import itemgetter

from constancy import Constants


class TestWeekDays(unittest.TestCase):
    def setUp(self):
        self.DAYS = Constants(MON=0, TUE=1, WED=2, THU=3, FRI=4, SAT=5, SUN=6)

    def test_getattribute(self):
        self.assertEqual(self.DAYS.MON, 0)

    def test_getitem(self):
        self.assertEqual(self.DAYS["MON"], 0)

    def test_list(self):
        self.assertListEqual(
            list(self.DAYS), ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        )

    def test_dict(self):
        self.assertDictEqual(
            dict(self.DAYS),
            {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6},
        )

    def test_assign(self):
        with self.assertRaises(AttributeError):
            self.DAYS.MON = 7

    def test_sort(self):
        self.DAYS.sort(key=itemgetter(1), reverse=True)
        self.assertListEqual(
            list(self.DAYS), ["SUN", "SAT", "FRI", "THU", "WED", "TUE", "MON"]
        )
