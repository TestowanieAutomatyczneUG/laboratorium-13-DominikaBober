class Planets:

    def __iniy__(self):
        self.planet = "ziemia"
    
    def set_planet(self, planet):
        if type(planet) is str:
            self.planet = planet
        else:
            raise Exception("Wrong variable type")

    def give_time(self, seconds):

        if (type(seconds) is float or type(seconds) is int):
            if seconds>0:
                if self.planet.lower() == "ziemia":
                    return round(seconds/31557600,2)
                elif self.planet.lower() == "merkury":
                    return round(seconds/0.2408467/31557600,2)
                elif self.planet.lower() == "wenus":
                    return round(seconds/0.61519726/31557600,2)
                elif self.planet.lower() == "mars":
                    return round(seconds/1.8808158/31557600,2)
                elif self.planet.lower() == "jowisz":
                    return round(seconds/11.862615/31557600,2)
                elif self.planet.lower() == "saturn":
                    return round(seconds/29.447498/31557600,2)
                elif self.planet.lower() == "uran":
                    return round(seconds/84.016846/31557600,2)
                elif self.planet.lower() == "neptun":
                    return round(seconds/164.79132/31557600,2)
                else:
                    raise Exception("Wrong planet name")
            else:
                raise Exception("Wrong time")
        else:
            raise Exception("Wrong variable type")