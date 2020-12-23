from contracts.scenes import Scenes

class SceneManager():
    """Class that interacts with an apimethods object to control scenes / create an one stop point for interacting with scenes"""
    headers = { 'Accept': 'application/json, application/xml, text/plain, text/html, *.*', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8' }

    def __init__(self, apiMethodsObj):
        """Constructor for the apiMethods."""
        self.apiMethodsObj = apiMethodsObj

    def isMemberOfScene(self, id, scene):
        sceneRooms = self.apiMethodsObj.getSceneRooms(scene)
        for i in range(len(sceneRooms)):
            if sceneRooms[i] == id:
                return True
        #If no match found return false
        return False

    def clearSceneRooms(self, scene):
        return self.apiMethodsObj.setSceneRooms(scene, [])

    def getMembersOfScene(self, scene):
        return self.apiMethodsObj.getSceneRooms(scene)

    def isSceneActive(self, scene):
        sceneStatus = self.apiMethodsObj.getSpecficScene(scene)
        return sceneStatus.isActive

    def addMemberToScene(self, id, scene, active):
        if self.isMemberOfScene(id, scene):
            if self.isSceneActive(scene):
                #Nothing todo scene already active and member exists
                return
        else:
            sceneRooms = self.apiMethodsObj.getSceneRooms(scene)
            sceneRooms.append(id)
            self.apiMethodsObj.setSceneRooms(scene, sceneRooms)
        
        #reset scene for newly specified duration if already active
        duration = self.apiMethodsObj.getSceneDuration(scene)
        if self.isSceneActive(scene):
            self.apiMethodsObj.setScene(Scenes(scene, duration, False))
        
        self.apiMethodsObj.setScene(Scenes(scene, duration, True))

    def removeMemberFromScene(self, id, scene, active):
        if self.isMemberOfScene(id, scene) == False:
            #room not part of scene. Therefore, nothing left to do
            return
        
        sceneRooms = self.apiMethodsObj.getSceneRooms(scene)
        for i in range(len(sceneRooms)):
            if sceneRooms[i] == id:
                sceneRooms.remove(sceneRooms[i])
        #reset scene for newly specified duration if already active
        duration = self.apiMethodsObj.getSceneDuration(scene)        
        if self.isSceneActive(scene):
            self.apiMethodsObj.setScene(Scenes(scene, duration, False))

        self.apiMethodsObj.setSceneRooms(scene, sceneRooms)        

        active = False
        if len(sceneRooms) > 0:
            active = True

        self.apiMethodsObj.setScene(Scenes(scene, duration, active))

        
