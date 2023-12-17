class Activator:
    def __init__(self, attributes: dict):
        for key, value in attributes.items():
            #ToDo: search for specific attributes
            setattr(self, key, value)\
            
    @classmethod
    def activators_from_json(cls, activators_json: list):
        """Converts a list of activators into a dict of activators, using call sing as key"""
        activators = {}
        for activator_json in activators_json:
            activators[activator_json['Callsign']] = Activator(attributes=activator_json)
        return activators