class CurrentReq(object):
    currently = None

    def __init__(self, weather_req):

        if weather_req.has_currently():
            self.currently = weather_req.gCurrently()
            for item in self.currently.keys():
                setattr(self, item, self.currently[item])

    def get(self):
        return self.currently
