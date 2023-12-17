#!/usr/bin/env python3
import json
import pathlib
import traceback
import urllib.request
from lib.Activator import Activator


class SOTAInfo(object):

    def __init__(self, cache_dir: str = "/tmp/SOTAInfo/", associationID: int = 48):
        pathlib.Path(cache_dir).mkdir(parents=True, exist_ok=True)  # ensures tempdir exists
        self.cache_dir = cache_dir
        self.associationID = associationID
        self._activators = self.init_activators()

    @property
    def Activators(self):
        """
        {'Position', 'UserID', 'Callsign', 'Username', 'Points', 'BonusPoints', 'Summits', 'totalPoints', 'Average'}
        :return: json 
        """
        return self._activators

    def init_activators(self):
        """Itializes activators attribute"""
        cache_file_path = pathlib.Path(self.cache_dir + "activators" + str(self.associationID) + ".json")
        if (cache_file_path.exists()):
            with cache_file_path.open(mode="r", encoding="utf-8") as f_activators:
                try:
                    return Activator.dict_from_json(json.load(f_activators))
                except Exception:
                    traceback.print_exc()

        activators = self.fetch_activators()
        with cache_file_path.open(mode="w", encoding="utf-8") as f_activators:
            json.dump(activators, f_activators, indent=2)
        return Activator.dict_from_json(activators)

    def fetch_activators(self):
        print("Fetching association " + str(self.associationID) + " call signs...", end='')
        api_data = urllib.request.urlopen("https://api-db.sota.org.uk/admin/activator_roll?associationID=" +
                                          str(self.associationID)).read()
        print(" done!")
        return json.loads(api_data.decode('utf-8'))


if __name__ == "__main__":
    cumbres_activadas = SOTAInfo()
    datos = cumbres_activadas.Activators
