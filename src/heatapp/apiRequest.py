import requests
import urllib.parse
from Crypto.Hash import MD5
import json

import logging

_LOGGER = logging.getLogger(__name__)

class ApiRequest():
    """Class with logic required to perform api requests towards the heatapp service"""
    headers = { 'Accept': 'application/json, application/xml, text/plain, text/html, *.*', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }

    def __init__(self):
        """Constructor for the apiRequest Class."""

    def _sortPropertiesInObject(self, valueObject):
        return sorted(valueObject.__dict__.items(), key=lambda val: val[0])
        #placeholder
    
    def _prepareRequestBodyForHash(self, urlencodedString):
        urlencodedString = urlencodedString.replace('%2C', ',').replace('%5B', '[').replace('%5D', ']')
        """Replace dots for comma in case of temperature being passed"""
        #if(urlencodedString.find("temperature") != -1):
        #    urlencodedString = urlencodedString.replace('.', ',')
        return urlencodedString

    def request(self, uri, credentials, requestBody):
        #test = urllib.parse.urlparse(requestBody)
        sortedRequestBody = self._sortPropertiesInObject(requestBody)
        urlencodedBody=urllib.parse.urlencode(sortedRequestBody, encoding='utf-8')
        urlencodedBodyPreparedForHash=self._prepareRequestBodyForHash(urlencodedBody)
        urlencodedBodyPreparedForHash = urlencodedBodyPreparedForHash.replace('&', '|')
        urlencodedBodyPreparedForHash = urlencodedBodyPreparedForHash + "|" + credentials.authorizationToken
        md5 = MD5.new()
        md5.update(bytes(urlencodedBodyPreparedForHash, 'utf-8'))
        test = md5.hexdigest()
        urlencodedBody = urlencodedBody + "&request_signature=" + test
        response = requests.post(uri, headers=self.headers, data=urlencodedBody)
        _LOGGER.debug(
            "request send to: %s ",
        uri)
        _LOGGER.debug(
            "response to request is %s", response.content
        )
        responseObject = json.loads(response.content)
        return responseObject
        
