import unittest
from fanalytics.qb import QbFanalytics

class MyQbTestCase(unittest.TestCase):
    def test_mean_qb_epa(self):
        qb = QbFanalytics([2021], {
            'name': 'T.Tagovailoa',
            'curr_team': 'MIA',
            'position': 'QB'
        })
        mean_qb_epa = qb.mean_qb_epa()
        epas = qb.mean_qb_epa()
        tua_epa = epas[(epas['passer'] == 'T.Tagovailoa')]
        self.assertEqual(0.06638715787668398, tua_epa['qb_epa'].item())


if __name__ == '__main__':
    unittest.main()
