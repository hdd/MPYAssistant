"""
name   : uGgahPLugin
author : langeli
date   : uGgah 

"""

import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeName = "uGgahPLugin"

#simple Exception
class uGgahPLuginError(Exception):
    def __init__(self, value):
        self.value=value
        
    def __str__(self):
        return repr(self.value)

#    node definition
class uGgahPLugin(OpenMayaMPx.MPxNode):
    # class variables
    inAttr = OpenMaya.MObject()
    outAttr = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self, plug, data):
        
        # Check that the requested recompute is one of the output values
        if plug == uGgahPLugin.outAttr:
            
            # Read the input values
            inData = data.inputValue(uGgahPLugin.inAttr)
            inValue = inData.asFloat()
            
            # Compute the output values
            resultValue = inValue*100
            
            # Store them on the output plugs            
            outputHandle = data.outputValue(uGgahPLugin.outvalue)
            outputHandle.setFloat(resultValue)
            data.setClean(plug)        
            
        else:
            return OpenMaya.MStatus.kUnknownParameter       
        return OpenMaya.MStatus.kSuccess
    
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( uGgahPLugin() )

def nodeInitializer():
    numAttrIn = OpenMaya.MFnNumericAttribute()
    numAttrOut = OpenMaya.MFnNumericAttribute()
    
    # Setup the input attributes
    uGgahPLugin.inAttr = numAttrIn.create("inAttr","in",OpenMaya.MFnNumericData.kFloat, 0.0)
    numAttrIn.setStorable(True)
    
    # Setup the output attributes    
    uGgahPLugin.outAttr = numAttrOut.create("outAttr","out",OpenMaya.MFnNumericData.kFloat, 0.0)
    numAttrOut.setWritable(False)
    numAttrOut.setStorable(False)
    
    # Add the attributes to the node
    uGgahPLugin.addAttribute(uGgahPLugin.inAttr)
    uGgahPLugin.addAttribute(uGgahPLugin.outAttr)
    
    # Set the attribute dependencies
    uGgahPLugin.attributeAffects(uGgahPLugin.inAttr,uGgahPLugin.outAttr)
    
# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeName, kPluginNodeId, nodeCreator, nodeInitializer)
    except:
    
# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( kPluginNodeId )
    except:
