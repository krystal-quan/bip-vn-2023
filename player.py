class Player:
    def __init__(self, id, first_name, second_name, goals_scored, assists, total_points, 
                 minutes, goals_conceded, creativity, influence, threat, bonus, bps, 
                 ict_index, clean_sheets, red_cards, yellow_cards, selected_by_percent, 
                 value, position):
        self._id = id
        self._first_name = first_name
        self._second_name = second_name
        self._goals_scored = goals_scored
        self._assists = assists
        self._total_points = total_points
        self._minutes = minutes
        self._goals_conceded = goals_conceded
        self._creativity = creativity
        self._influence = influence
        self._threat = threat
        self._bonus = bonus
        self._bps = bps
        self._ict_index = ict_index
        self._clean_sheets = clean_sheets
        self._red_cards = red_cards
        self._yellow_cards = yellow_cards
        self._selected_by_percent = selected_by_percent
        self._value = value
        self._position = position

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def get_position(self):
        return self._position
    
    def set_position(self, position):
        self._position = position

    def get_full_name(self):
        return str(self._first_name + "_" + self._second_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_second_name(self):
        return self._second_name

    def set_second_name(self, second_name):
        self._second_name = second_name

    def get_goals_scored(self):
        return self._goals_scored

    def set_goals_scored(self, goals_scored):
        self._goals_scored = goals_scored

    def get_assists(self):
        return self._assists

    def set_assists(self, assists):
        self._assists = assists

    def get_total_points(self):
        return self._total_points

    def set_total_points(self, total_points):
        self._total_points = total_points

    def get_minutes(self):
        return self._minutes

    def set_minutes(self, minutes):
        self._minutes = minutes

    def get_goals_conceded(self):
        return self._goals_conceded

    def set_goals_conceded(self, goals_conceded):
        self._goals_conceded = goals_conceded

    def get_creativity(self):
        return self._creativity

    def set_creativity(self, creativity):
        self._creativity = creativity

    def get_influence(self):
        return self._influence

    def set_influence(self, influence):
        self._influence = influence

    def get_threat(self):
        return self._threat

    def set_threat(self, threat):
        self._threat = threat

    def get_bonus(self):
        return self._bonus

    def set_bonus(self, bonus):
        self._bonus = bonus

    def get_bps(self):
        return self._bps

    def set_bps(self, bps):
        self._bps = bps

    def get_ict_index(self):
        return self._ict_index

    def set_ict_index(self, ict_index):
        self._ict_index = ict_index

    def get_clean_sheets(self):
        return self._clean_sheets

    def set_clean_sheets(self, clean_sheets):
        self._clean_sheets = clean_sheets

    def get_red_cards(self):
        return self._red_cards

    def set_red_cards(self, red_cards):
        self._red_cards = red_cards

    def get_yellow_cards(self):
        return self._yellow_cards

    def set_yellow_cards(self, yellow_cards):
        self._yellow_cards = yellow_cards

    def get_selected_by_percent(self):
        return self._selected_by_percent

    def set_selected_by_percent(self, selected_by_percent):
        self._selected_by_percent = selected_by_percent

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def print_all(self):
        return f"{str(self._id)}  {str(self._first_name)} {str(self._second_name)} {str(self._position)} {str(self._goals_scored)} {str(self._assists)} {str(self._total_points)} {str(self._minutes)} {str(self._goals_conceded)} {str(self._creativity)} {str(self._influence)} {str(self._threat)} {str(self._bonus)} {str(self._bps)} {str(self._ict_index)} {str(self._clean_sheets)} {str(self._red_cards)} {str(self._yellow_cards)} {str(self._selected_by_percent)} {str(self._value)}"
    
    def getPlayerInfo(self):
        return f"{self._id} - {self._first_name} {self._second_name} - {self._position}"

    def reset(self):
        self._goals_scored = -1
        self._assists = -1
        self._total_points = -1
        self._minutes = -1
        self._goals_conceded = -1
        self._creativity = 0.0
        self._influence = 0.0
        self._threat = -1
        self._bonus = 0.0
        self._bps = -1
        self._ict_index = -1
        self._clean_sheets = -1
        self._red_cards = -1
        self._yellow_cards = -1
        self._selected_by_percent = -1
