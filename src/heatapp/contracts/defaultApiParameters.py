class DefaultApiParams():
    """Class that contains all default required parameters for interacting with the heatapp api"""

    def __init__(self, userId, udid, reqcount = 0, skin = "flat_white"):
        """Constructor for the UserInfo."""
        self.reqcount = reqcount
        self.userid = userId
        self.udid = udid
        self.skin = skin