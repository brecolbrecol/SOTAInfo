#!/usr/bin/env python3
from lib.SOTAInfo import SOTAInfo
import argparse

"""
Given a list of activators and a list of references, count how many times each reference was activated by each activator
"""
class ActivatedSummits:
    def __init__(self, year: int = None):
        self._year = year
        self._summits_count = {}

    @property
    def year(self):
        return self._year

    @property
    def summits_count(self):
        return self._summits_count

    @summits_count.setter
    def summits_count(self,value):
        self._summits_count = value

    def activators_christmas(self):
        return ["EA4GDK","EA4GZU","EA4HCF","EA4HGT","EA4DE","EA4HIH","EA4HTO","EA4FUA","EB4FJV","EA4HNQ","EA4HSS","EA4HFO"]

    def proposed_references(self):
        return ["EA1/SG-017", "EA1/SG-005", "EA4/MD-017", "EA4/MD-045", "EA1/AV-013", "EA1/SG-019", "EA4/MD-047", "EA1/SG-001", "EA4/MD-052","EA4/MD-053","EA4/MD-019","EA4/MD-028","EA4/MD-029","EA4/MD-012"]

    def run(self):
        sota_info = SOTAInfo()
        activators_all = sota_info.Activators

        for activator in self.activators_christmas():
            try:
                activated_references = activators_all[activator].activated_references(year=self.year)
                for activated_reference in activated_references:
                    reference_name = activated_reference['Summit']
                    if not reference_name in self.summits_count:
                        self.summits_count[reference_name] = {'count': 1, 'activators': activator}
                    elif activator not in self.summits_count[reference_name]['activators']:
                        self.summits_count[reference_name]['count'] += 1
                        self.summits_count[reference_name]['activators'] += ', ' + activator
                    else:
                        print(activator + " repeated " + reference_name)
            except:
                print(activator + " not found in SOTA database")
    
    def print_results(self):
        print("\n== Results ==")
        for reference, data in sorted(self.summits_count.items(), key=lambda kv: kv[1]['count']):
            if reference.split()[0] in self.proposed_references():
                print(str(data['count']) + ": " + reference + " -> " + data['activators'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count activations of summit list by given call signs.')
    parser.add_argument('--year', type=int, help='Retrieve only summits activated this year')
    args = parser.parse_args()

    activated_summits = ActivatedSummits(year=args.year)
    activated_summits.run()
    activated_summits.print_results()