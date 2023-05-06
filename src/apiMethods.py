from apiRequest import ApiRequest
from contracts.defaultApiParameters import DefaultApiParams
import json
import re

class ApiMethods():
    """Class with logic required to perform api requests towards the heatapp service"""
    headers = { 'Accept': 'application/json, application/xml, text/plain, text/html, *.*', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }

    def __init__(self, credentials, base_url):
        """Constructor for the ApiMethods."""
        self.base_url=base_url
        self.credentials=credentials

    def _getCorrectUser(self, data, username):
        return None

    def setTemp(self, inputtemperature, roomId):
        dataObject = DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId);
        dataObject.roomid = roomId
        dataObject.change_mode = 0
        dataObject.temperature = inputtemperature
        ApiRequest().request(self.base_url + '/api/room/settemperature', self.credentials, dataObject)

    def getRawRooms(self):
        return ApiRequest().request(self.base_url + '/api/room/list', self.credentials, DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId))

    def getRoomsList(self):
        rawRooms = self.getRawRooms()
        results = []
        for i in range(len(rawRooms["groups"])):
            for j in range(len(rawRooms["groups"][i]["rooms"])):
                results.append({ "name": rawRooms["groups"][i]["rooms"][j]["name"], "data": rawRooms["groups"][i]["rooms"][j]})

        return results

    def getSpecificRoom(self, id):
        rooms = self.getRoomsList()
        for i in range(len(rooms)):
            if id == rooms[i]["data"]["id"]:
                return rooms[i]

    def getWeather(self):
        return ApiRequest().request(self.base_url + '/api/weather', self.credentials, DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId))

    def getScene(self):
        return ApiRequest().request(self.base_url + '/api/scene/status', self.credentials, DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId))

    def getSpecficScene(self, scene):
        scenesResult = self.getScene()
        scenesList = scenesResult["scenes"]
        for i in range(len(scenesList)):
            if scene == scenesList[i]["name"]:
                return scenesList[i]
            else:
                raise ValueError('The specified scene doesn\'t exists.')

    def getSceneRooms(self, scene):
        dataObject = DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId)
        dataObject.scene = scene
        result = ApiRequest().request(self.base_url + '/api/scene/getrooms', self.credentials, dataObject)
        return result["rooms"]

    def getSceneDuration(self, scene):
        dataObject = DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId)
        dataObject.scene = scene
        result = ApiRequest().request(self.base_url + '/api/scene/duration', self.credentials, dataObject)
        return result["duration"]

    def setSceneRooms(self, scene, rooms):
        roomsString = "["
        for i in range(len(rooms)):
            roomsString += rooms[i]["id"] + ","
        scene = { scene: scene }
        roomsString = re.sub(r',s*$', '', roomsString)
        roomsString += "]"
        self.setSceneRoom(scene, roomsString)
        return None

    def setSceneRoom(self, scene, room):
        dataObject = DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId)
        dataObject.rooms = room
        dataObject.scene = scene
        return ApiRequest().request(self.base_url + '/api/scene/setrooms', self.credentials, dataObject)

    def setScene(self, scene):
        dataObject = DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId)
        dataObject.scene = scene["scene"]
        dataObject.active = scene["active"]

        if scene.scene != "Standby":
            dataObject = re.sub(r'/\./g', ',', scene["duration"])
        else:
            dataObject.duration = 1

        return ApiRequest().request(self.base_url + '/api/scene/set', self.credentials, dataObject)

    def getPortalData(self):
        return ApiRequest().request(self.base_url + '/api/portal/access/data', self.credentials, DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId))

    def getUsersList(self):
        return ApiRequest().request(self.base_url + '/api/user/list', self.credentials, DefaultApiParams(userId=self.credentials.userId, udid=self.credentials.deviceId))

    def getWizard(self):
        '''
        Wizard (Profi / Admin Panel) requires admin rights
        First level. Lower level use getServercode
        '''
        return (
            ApiRequest()
            .request(
                self.base_url + '/api/wizard/start',
                self.credentials,
                DefaultApiParams(userId=self.credentials.userId,
                                 udid=self.credentials.deviceId)
            )
            ['heatcom']
        )

    def getServercode(self, servercode):
        '''
        Wizard (Profi / Admin Panel) requires admin rights
        Deeper level. requires Servercode obtained from getWizard
        '''
        dataObject = DefaultApiParams(
            userId=self.credentials.userId, udid=self.credentials.deviceId)
        dataObject.servercode = servercode

        result = ApiRequest().request(self.base_url + '/api/wizard/next',
                                      self.credentials, dataObject)
        return result
