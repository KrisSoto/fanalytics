import copy
import logging
from fanalytics.player import PlayerFanalytics


logger = logging.getLogger(__name__)
log_level = logging.INFO
logging.basicConfig(level=log_level)


class QbFanalytics(PlayerFanalytics):
    def __init__(self, years, player_info):
        """

        :param years:
        :param player_info: a dict including:
            name, curr_team
        """
        player_info['position'] = 'QB'
        super().__init__(years, player_info)
        self.qb_data = None
        self._get_qb_data()

    def _get_qb_data(self):
        """
        Sets qb_data class variable
        :return: only data related to QB
        """
        return copy.deepcopy(self.data.loc[self.data['passer'] == self.name])

    def mean_qb_epas(self, min_plays=500):
        """
        Gets the average qb EPA for years selected

        :return: This QB, All QBs EPA
        """
        logger.info("Getting mean of QB EPA.. if its good")
        qbs = self.data.groupby(['passer', 'posteam'], as_index=False).agg({
            'qb_epa': 'mean',
            'play_id': 'count'
        })
        qbs = qbs.loc[qbs.play_id > min_plays]
        return qbs[(qbs['passer'] == self.name)], qbs


"""
For testing purposes
"""
if __name__ == '__main__':
    qb = QbFanalytics([2021], {
        'name': 'T.Tagovailoa',
        'curr_team': 'MIA',
        'position': 'QB'
    })
    tua_epa, all_epas = qb.mean_qb_epas()
    print(tua_epa['qb_epa'], '\n', all_epas)