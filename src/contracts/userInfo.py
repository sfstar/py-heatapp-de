class UserInfo():
    """Class information about heatapp users."""

    def __init__(self, id, salutation, firstname, lastname, login, accesslevel, created, imagepath, created_by, notifications, imagehidden, rooms):
        """Constructor for the UserInfo."""
        self.id = id
        self.salutation = salutation
        self.firstname = firstname
        self.lastname = lastname
        self.login = login
        self.accesslevel = accesslevel
        self.created = created
        self.imagepath = imagepath
        self.created_by = created_by
        self.notifications = notifications
        self.imagehidden = imagehidden
        self.rooms = rooms
