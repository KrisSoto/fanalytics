import unittest
from fanalytics.qb import QbFanalytics


class MyQbTestCase(unittest.TestCase):
    def setUp(self):
        self.qb = QbFanalytics([2021], {
            'name': 'T.Tagovailoa',
            'curr_team': 'MIA',
            'position': 'QB'
        })

    def test_mean_qb_epa(self):
        epas = self.qb.mean_qb_epas()
        tua_epa, all_epas = epas[(epas['passer'] == 'T.Tagovailoa')]
        self.assertEqual(0.06638715787668398, tua_epa['qb_epa'].item())


if __name__ == '__main__':
    unittest.main()
