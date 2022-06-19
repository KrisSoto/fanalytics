import pandas as pd
import logging

logger = logging.getLogger(__name__)
log_level = logging.INFO
logging.basicConfig(level=log_level)


class BaseFanalytics:
    """
    Class Variables:

    self.years - the years to collect data
    self.data - DataFrame with all data
    """
    def __init__(self, years):
        """
        :param years: an array of years to collect
        """
        if type(years) is not list:
            logger.error(f'years parameter must be an array')
            exit(0)
        self.years = years
        self.data = pd.DataFrame()
        self.parse_data()

    def parse_data(self):
        for year in self.years:
            new_data = pd.read_csv(
                'https://github.com/guga31bb/nflfastR-data/'
                'blob/master/data/play_by_play_'
                + str(year) + '.csv.gz?raw=True',
                compression='gzip', low_memory=False)
            self.data = self.data.append(new_data, sort=True)
            self.data.reset_index(drop=True, inplace=True)

    def _clean_data(self):
        """
        operations to clean self.data

        :return: None
        """
        # ensure all 'pass' type plays are labeled pass
        # and that all run plays are correctly labeled run
        self.data.loc[self.data['pass'] == 1, 'play_type'] = 'pass'
        self.data.loc[self.data['rush'] == 1, 'play_type'] = 'run'

    def rank_subset(self, subset, key, num_values):
        """
        Will rank a df subset using the key and return a ranked list
        with the length of num_values

        :param subset: a df with a subset of data
        :param key: key to rank subset by
        :param num_values: the length of the list to return
        :return: a list of dictionary values, ranked.
        """
        logger.info(f'Getting rankings from DataFrame subset by key: {key} '
                    f'to get the top {num_values}.')
        ranked = subset.sort_values(by=key, ascending=False)
        return ranked.head(num_values)
