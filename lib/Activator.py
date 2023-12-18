import urllib
import json

class Activator:
    def __init__(self, attributes: dict):
        self._activated_summits = None
        for key, value in attributes.items():
            #ToDo: search for specific attributes
            # {'Position', 'UserID', 'Callsign', 'Username', 'Points', 'BonusPoints', 'Summits', 'totalPoints', 'Average'}
            setattr(self, key, value)

    def activated_references(self, year: int = None):
        if self._activated_summits is None:
            self._activated_summits = self.fetch_summits(year)
        return self._activated_summits

    def fetch_summits(self, year: int = None):
        msg = "Fetching summits activated by " + self.Callsign
        url = "https://api-db.sota.org.uk/admin/activator_log_by_id?id=" + str(self.UserID)
        if year is not None:
            url += "&year=" + str(year)
            msg += " in " + str(year)

        print( msg + "...", end='')
        api_data = urllib.request.urlopen(url).read()
        print(" done!")

        return json.loads(api_data.decode('utf-8'))

    @classmethod
    def dict_from_json(cls, activators_json: list):
        """Converts a list of activators into a dict of activators, using call sing as key"""
        activators = {}
        for activator_json in activators_json:
            activators[activator_json['Callsign'].upper()] = Activator(attributes=activator_json)
        return activators