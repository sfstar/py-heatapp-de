class Room():
    """Class information about heatapp users."""

    def __init__(self, id, salutation, firstname, lastname, login, accesslevel, created, imagepath, created_by, notifications, imagehidden, rooms):
        """Constructor for the UserInfo."""
        self.id = id
        self.appid = salutation
        self.actualTemperature = firstname
        self.isComfortMode = lastname
        self.desiredTemperature = login
        self.roomstatus = accesslevel
        self.desiredTempDay = created
        self.desiredTempDay2 = imagepath
        self.desiredTempNight = created_by
        self.scheduleTempMin = notifications
        self.scheduleTempMax = imagehidden
        self.minTemperature = rooms
        self.maxTemperature
        self.cooling
        self.coolingEnabled
        self.imagepath
        self.name
        self.orderindex
        self.originalName
        self.status
        self.groupid
        self.windowPosition

