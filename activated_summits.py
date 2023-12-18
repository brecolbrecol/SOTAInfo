#!/usr/bin/env python3
from lib.SOTAInfo import SOTAInfo

"""
Given a list of activators and a list of references, count how many times each reference was activated by each activator
"""

def activators_christmas():
    return ["EA4GDK","EA4GZU","EA4HCF","EA4HGT","EA4DE","EA4HIH","EA4HTO","EA4FUA","EB4FJV","EA4HNQ","EA4HSS","EA4HFO"]

def proposed_references():
    return ["EA1/SG-017", "EA1/SG-005", "EA4/MD-017", "EA4/MD-045", "EA1/AV-013", "EA1/SG-019", "EA4/MD-047", "EA1/SG-001", "EA4/MD-052","EA4/MD-053","EA4/MD-019","EA4/MD-028","EA4/MD-029","EA4/MD-012"]

if __name__ == "__main__":
    summits_count = {}
    sota_info = SOTAInfo()
    activators_all = sota_info.Activators

    for activator in activators_christmas():
        try:
            activated_references = activators_all[activator].activated_references(year=2023)
            for activated_reference in activated_references:
                reference_name = activated_reference['Summit']
                if not reference_name in summits_count:
                    summits_count[reference_name] = {'count': 1, 'activators': activator}
                elif activator not in summits_count[reference_name]['activators']:
                    summits_count[reference_name]['count'] += 1
                    summits_count[reference_name]['activators'] += ', ' + activator
                else:
                    print(activator + " repeated " + reference_name)
        except:
            print(activator + " not found in SOTA database")

    print("\n== Results ==")
    for reference, data in sorted(summits_count.items(), key=lambda kv: kv[1]['count']):
        if reference.split()[0] in proposed_references():
            print(str(data['count']) + ": " + reference + " -> " + data['activators'])