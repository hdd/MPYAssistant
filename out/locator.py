import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaRender as OpenMayaRender
 
nodeTypeName = "myCustomLocator"
nodeTypeId = OpenMaya.MTypeId(0x87079)
 
glRenderer = OpenMayaRender.MHardwareRenderer.theRenderer()
glFT = glRenderer.glFunctionTable()
 
class myNode(OpenMayaMPx.MPxLocatorNode):
    def __init__(self):
        OpenMayaMPx.MPxLocatorNode.__init__(self)
 
    def draw(self, view, path, style, status):
 
        view.beginGL()
 
        glFT.glBegin(OpenMayaRender.MGL_POINTS)
        glFT.glPointSize(4)        
        glFT.glVertex3f(0.0, 0.0, 0.0)
        view.setDrawColor( OpenMaya.MColor(0.1, 0.2, 0.7) ); # Set color as desired
        glFT.glEnd()
 
        view.endGL()
 
 
def nodeCreator():
    return OpenMayaMPx.asMPxPtr(myNode())
 
def nodeInitializer():
    return OpenMaya.MStatus.kSuccess
 
def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    try:
        plugin.registerNode(nodeTypeName, nodeTypeId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kLocatorNode)
    except:
        sys.stderr.write( "Failed to register node: %s" % nodeTypeName)
 
def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    try:
        plugin.deregisterNode(nodeTypeId)
    except:
        sys.stderr.write( "Failed to deregister node: %s" % nodeTypeName)