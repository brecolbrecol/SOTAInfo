from lib.SOTAInfo import SOTAInfo

if __name__ == "__main__":
    cumbres_activadas = SOTAInfo()
    data = cumbres_activadas.Activators
    ea4hfo = data['EA4HFO']
    print("Points: " + str(ea4hfo.Points))
    blah = ea4hfo.activated_references(year=2023)
    print("Done.")