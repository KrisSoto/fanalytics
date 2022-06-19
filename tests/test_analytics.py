import unittest
import copy
import pandas as pd
from fanalytics.analytics import BaseFanalytics


class AnalyticsTestcase(unittest.TestCase):
    def setUp(self):
        self.base = BaseFanalytics([2020])

    def test_parse_data(self):
        test_data = pd.DataFrame()
        new_data = pd.read_csv('resources/play_by_play_2020.csv.gz',
                               compression='gzip', low_memory=False)
        test_data = test_data.append(new_data, sort=True)
        test_data.reset_index(drop=True, inplace=True)
        compare = test_data.compare(self.base.data)
        self.assertEqual(compare.size, 0)

    def test_rank_subset(self):
        ranking_data = \
            copy.deepcopy(self.base.data[self.base.data.defteam=='MIA'])
        ranking_data = ranking_data.groupby('passer').agg({
            'qb_epa': 'mean',
            'play_id': 'count'
        })
        ranking_data = self.base.rank_subset(ranking_data, 'qb_epa', 32)
        print(ranking_data)
        ja = ranking_data['qb_epa'][0]
        self.assertEqual(ja, 0.598331928104618)


if __name__ == '__main__':
    unittest.main()
