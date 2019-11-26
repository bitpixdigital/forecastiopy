class CurrentReq(object):
    currently = None

    def __init__(self, WeatherReq):

        if WeatherReq.has_currently():
            self.currently = WeatherReq.gCurrently()
            for item in self.currently.keys():
                setattr(self, item, self.currently[item])

    def get(self):
        return self.currently
