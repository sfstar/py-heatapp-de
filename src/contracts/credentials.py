class Credentials():
    """Class contract which contains credential information."""

    def __init__(self, username, password, deviceId, deviceToken, authorizationToken, userId):
        """Constructor for the Scenes."""
        self.username = username
        self.password = password
        self.deviceId = deviceId
        self.deviceToken = deviceToken
        self.authorizationToken = authorizationToken
        self.userId = userId