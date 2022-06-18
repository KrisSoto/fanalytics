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
            self.data = pd.read_csv(
                'https://github.com/guga31bb/nflfastR-data/'
                'blob/master/data/play_by_play_'
                + str(year) + '.csv.gz?raw=True',
                compression='gzip', low_memory=False)
            self.data = self.data.append(self.data, sort=True)
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