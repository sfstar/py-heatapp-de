class Scenes():
    """Class informations about heatapp scenes."""

    def __init__(self, scene, duration, active):
        """Constructor for the Scenes."""
        self.scene = scene
        self.duration = self._convertMinutesToHours(duration) #TODO calculate hourly value based on minute input
        self.active = active

    def _convertMinutesToHours(self, minutes):
        return minutes / 60