"""
name   : testNode
author : langeli
"""

import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeName = "testNode"
kPluginNodeId = OpenMaya.MTypeId(0x87005)

#simple Exception
class testNodeError(Exception):
    def __init__(self, value):
        self.value=value
        
    def __str__(self):
        return repr(self.value)

#    node definition
class testNode(OpenMayaMPx.MPxNode):
    # class variables
    inAttr = OpenMaya.MObject()
    outAttr = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self, plug, data):
        
        # Check that the requested recompute is one of the output values
        if plug == testNode.outAttr:
            
            # Read the input values
            inData = data.inputValue(testNode.inAttr)
            inValue = inData.asFloat()
            
            # Compute the output values
            resultValue = inValue*100
            
            # Store them on the output plugs            
            outputHandle = data.outputValue(testNode.outvalue)
            outputHandle.setFloat(resultValue)
            data.setClean(plug)        
            
        else:
            return OpenMaya.MStatus.kUnknownParameter       
        return OpenMaya.MStatus.kSuccess
    
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( testNode() )

def nodeInitializer():
    numAttrIn = OpenMaya.MFnNumericAttribute()
    numAttrOut = OpenMaya.MFnNumericAttribute()
    
    # Setup the input attributes
    testNode.inAttr = numAttrIn.create("inAttr","in",OpenMaya.MFnNumericData.kFloat, 0.0)
    numAttrIn.setStorable(True)
    
    # Setup the output attributes    
    testNode.outAttr = numAttrOut.create("outAttr","out",OpenMaya.MFnNumericData.kFloat, 0.0)
    numAttrOut.setWritable(False)
    numAttrOut.setStorable(False)
    
    # Add the attributes to the node
    testNode.addAttribute(testNode.inAttr)
    testNode.addAttribute(testNode.outAttr)
    
    # Set the attribute dependencies
    testNode.attributeAffects(testNode.inAttr,testNode.outAttr)
    
# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeName, kPluginNodeId, nodeCreator, nodeInitializer)
    except:
        raise testNodeError , "Failed to register node: %s" % kPluginNodeName
    
# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( kPluginNodeId )
    except:
        raise testNodeError , "Failed to deregister node: %s" % kPluginNodeName