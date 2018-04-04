from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.ARB.vertex_buffer_object import *
from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGLContext.arrays import *
from OpenGLContext.events.timer import Timer
from OpenGL.arrays import vbo
import random
import numpy as np
from OpenGLContext.scenegraph.basenodes import *

if __name__ == "__main__":
    TestContext.ContextMainLoop()

class TestContext(BaseContext):
    def OnInit(self):
        VERTEX_SHADER = shaders.compileShader
