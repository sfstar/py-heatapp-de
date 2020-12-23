import uuid
from hashlib import md5
from Crypto.Hash import SHA256, MD5
from Crypto.Cipher import AES
import base64
from contracts.credentials import Credentials
import json
import logging
#test
import requests
from contracts.defaultApiParameters import DefaultApiParams

_LOGGER = logging.getLogger(__name__)

class Login():
    """Class with logic required to perform api requests towards the heatapp service"""
    headers = { 'Accept': 'application/json, application/xml, text/plain, text/html, *.*', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }

    def __init__(self, base_url):
        """Constructor for the Login Class."""
        self.base_url=base_url

    def authorize(self, username, password):
        if(not username or not password):
            _LOGGER.error(
                "Error: Please provide the username and password to the library"
            )
        else:
            self.identity = Credentials(username=username, password=password, deviceId=self._generateSystemGUID(),deviceToken="",authorizationToken="",userId="")
            self.identity.deviceToken = self._requestChallengeToken(self.identity)
            return self._login(self.identity)

    def _generateSystemGUID(self):
        """Generate the device id based on the hw information of the machine"""
        return str(uuid.uuid1())

    def _requestChallengeToken(self, credentials):
        challengeTokenBody = {  "udid": credentials.deviceId }
        #parse.urlencode(challengeTokenBody).encode()

        uri=self.base_url + '/api/user/token/challenge'
        #TODO perform request to the heatapp endpoint to get the challenge token
        response = json.loads(requests.post(uri, headers=self.headers, data=challengeTokenBody).content)
        _LOGGER.debug(
            "challenge token response: %s", response
        )
        return response["devicetoken"]

    def _login(self, credentials):
        md5 = MD5.new()
        md5.update(bytes(credentials.password + credentials.deviceToken, 'utf-8'))
        #TODO make the user able to configure the device name that is used to register to heatapp
        loginBody = { "udid": credentials.deviceId, "login": credentials.username, "token": credentials.deviceToken, "hashed": md5.hexdigest(), "devicename": "homeassistant" }
        uri=self.base_url + '/api/user/token/response'
        response = json.loads(requests.post(uri, headers=self.headers, data=loginBody).content)
        _LOGGER.debug(
            "login response: %s", response
        )
        credentials.userId = response["userid"]
        credentials.authorizationToken = self.decrypt2(response["devicetoken_encrypted"], credentials.password)
        return credentials

    def decrypt2(self, encryptedData, decryptkey):
        #preshared initialization vector
        staticIv='D3GC5NQEFH13is04KD2tOg=='
        cryptkey = SHA256.new()
        cryptkey.update(bytes(decryptkey, 'utf-8'))
        cryptkey = cryptkey.digest()
        cipher = AES.new(cryptkey, AES.MODE_CBC, base64.b64decode(staticIv))
        #Note the \x10 is an escaped character that needs to be stripped in order for api calls to work
        decryptedValue = cipher.decrypt(base64.b64decode(encryptedData)).decode('ascii').strip('\x10')
        return decryptedValue
