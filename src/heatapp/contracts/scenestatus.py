from .scene import Scene

class SceneStatus():
    """Class information about heatapp users."""

    def __init__(self, test):
        """Constructor for the UserInfo."""
        self.scenes = []
        self.isParty = ""
        self.isBoost = ""
        self.isHoliday = ""
        self.isShower = ""
        self.isLeave = ""
        self.isStandby = ""