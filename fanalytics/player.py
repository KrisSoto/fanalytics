from fanalytics.analytics import BaseFanalytics


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
