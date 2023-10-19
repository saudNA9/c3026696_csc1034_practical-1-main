from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):
    def __init__(self, scale, scale_nature, nature_position, panda_jogging, no_rotate=False):
        ShowBase.__init__(self)

        # Here i verified command-line arguments
        if no_rotate == None:
            no_rotate = False

        # Here i have wrote the scale argument
        if scale != None and scale != 0:
            if scale == 1:
                scale = 0.018
        else:
            scale = 0.009

        #Here i have wrote the scale_nature argument
        if scale_nature == None:
            scale_nature = 0.30

        #Here i have wrote the nature_position argument
        if nature_position != None:
            if nature_position == "left":
                nature_position = [6, 40, 0]

            if nature_position == "right":
                nature_position = [-12, 40, 0]
        else:
            nature_position = [-4, 40, 0]
        #Here i have added the panda_jogging argument
        if panda_jogging == None:
            panda_jogging = 5

        # Here i activated the nature model.
        self.scene = self.loader.loadModel("models/environment")
        # Here we reparent the model in order for it to render.
        self.scene.reparentTo(self.render)
        # On the model,  we use scale and position transformations.
        self.scene.setScale(scale_nature, scale_nature, scale_nature)
        self.scene.setPos(nature_position[0], nature_position[1], nature_position[2])

        if no_rotate == False:
        # Here we add the procedure spinCameraTask to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
        # Here stop spinCameraTask procedure from the task manager.
            self.taskMgr.add(self.stopCameraTask, "StopCameraTask")

        # Here we load the panda actor and transform it.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(scale, scale, scale)
        self.pandaActor.reparentTo(self.render)

        # Here the animation should be looped.
        self.pandaActor.loop("walk")

        # Here we adjust the playback speed
        self.pandaActor.setPlayRate(panda_jogging, "walk")

        # Here i generated a forest sound.
        ForestSound = self.loader.loadSfx("Forest_Sound.wav")
        ForestSound.setLoop(True)
        ForestSound.play()

        # Here i generated panda sound
        pandaSound = self.loader.loadSfx("Panda_Sound.wav")
        pandaSound.setLoop(True)
        pandaSound.play()

    # Here i created a technique for moving the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
    # Here i created another technique were it stops the camera
    def stopCameraTask(self, task):
        angleDegrees = 0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont