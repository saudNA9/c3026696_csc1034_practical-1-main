from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor

class WalkingPanda(ShowBase):
    def __init__(self, scale, scale_nature, nature_position, no_rotate=False):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        if scale != None and scale != 0:
            if scale == 1:
                scale = 0.008
        else:
            scale = 0.004

        if scale_nature == None:
            scale_nature = 0.20

        if nature_position != None:
            if nature_position == "left":
                nature_position = [8, 40, 0]

            if nature_position == "right":
                nature_position = [-16, 40, 0]
        else:
            nature_position = [-6, 40, 0]

        # Load the nature model.
        self.scene = self.loader.loadModel("models/nature")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
         self.scene.setScale(scale_nature, scale_nature, scale_nature)
         self.scene.setPos(nature_position[0], nature_position[1], nature_position[2])

        if no_rotate==False:
            # Add the spinCameraTask procedure to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
            self.taskMgr.add(self.stopCameraTask, "StopCameraTask")

        # transform and load the actor of panda.
        self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(scale, scale, scale)
        self.pandaActor.reparentTo(self.render)

        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def stopCameraTask(self, task):
        angleDegrees = 0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont