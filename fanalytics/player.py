import logging

from fanalytics.analytics import BaseFanalytics

logger = logging.getLogger(__name__)
log_level = logging.INFO
logging.basicConfig(level=log_level)

class PlayerFanalytics(BaseFanalytics):
    def __init__(self, years, player_info):
        """
        A base class for all player types

        :param years:
        :param player_info: a dict including:
            name, curr_team, position
        """
        super().__init__(years)
        self.name = player_info.get('name')
        self.team = player_info.get('curr_team')
        self.position = player_info.get('position')
