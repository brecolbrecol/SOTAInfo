#!/usr/bin/env python3
import json
import pathlib
import traceback
import urllib.request


class SOTAInfo(object):

    def __init__(self, cache_dir: str = "/tmp/SOTAInfo/", associationID: int = 48):
        pathlib.Path(cache_dir).mkdir(parents=True, exist_ok=True)  # ensures tempdir exists
        self.cache_dir = cache_dir
        self.associationID = associationID
        self._callsigns = self.init_callsigns()

    @property
    def Callsigns(self):
        """
        {'Position', 'UserID', 'Callsign', 'Username', 'Points', 'BonusPoints', 'Summits', 'totalPoints', 'Average'}
        :return: json 
        """
        return self._callsigns

    def init_callsigns(self):
        """Itializes callsign attribute"""
        cache_file_path = pathlib.Path(self.cache_dir + "callsigns" + str(self.associationID) + ".json")
        if (cache_file_path.exists()):
            with cache_file_path.open(mode="r", encoding="utf-8") as f_callsigns:
                try:
                    return json.load(f_callsigns)
                except Exception:
                    traceback.print_exc()

        callsigns = self.fetch_callsigns()
        with cache_file_path.open(mode="w", encoding="utf-8") as f_callsigns:
            json.dump(callsigns, f_callsigns, indent=2)
        return callsigns

    def fetch_callsigns(self):
        print("Fetching association " + str(self.associationID) + " call signs...", end='')
        api_data = urllib.request.urlopen("https://api-db.sota.org.uk/admin/activator_roll?associationID=" +
                                          str(self.associationID)).read()
        print(" done!")
        return json.loads(api_data.decode('utf-8'))


if __name__ == "__main__":
    cumbres_activadas = SOTAInfo()
    datos = cumbres_activadas.Callsigns
