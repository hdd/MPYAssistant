import os
import sys
import glob
import cStringIO

pluginDatas={}
pluginDatas["$PLUGINTYPE"]=None
pluginDatas["$PLUGINNAME"]=None
pluginDatas["$AUTHOR"]=None
pluginDatas["$DATE"]=None
pluginDatas["$DOCS"]=None

templateExtension=".tpy"

templateMapping={}
templateMapping["simple"]="simpleNode"
templateMapping["deformer"]="deformerNode"


def getCurrentPath():
    """
    return the path of the current file
    """
    currentFile=__file__
    return os.path.dirname(currentFile)


def getFileTemplate(pluginDatas):
    """
    return the file template for the given type
    """
    returnTemplate=None
    currentPath = getCurrentPath()
    templateFolder="%s/templates/"%currentPath
    if os.path.exists(templateFolder):
        templates= glob.glob("%s/*.%s"%(templateFolder,templateExtension))
        
        if not templates:
            raise Exception , "No template file has been found"
        
        for template in templates:
            templateName=os.path.basename(template).split(".")[0]
            
            if not pluginDatas["$PLUGINTYPE"]:
                raise Exception ,"No template name has been provided"
            
            if templateName == pluginDatas["$PLUGINTYPE"]:
                returnTemplate=template
    else:
        raise Exception ,"No template folder has been found"
    
    return returnTemplate


def writeFile(datas,pluginDatas):
    """
    return the replaced file
    """
    if not datas:
        return Exception , "an error occured file datas is empty "
    
    returnFile=None
    currentPath = getCurrentPath()
    pluginFolder="%s/out/"%currentPath
    if os.path.exists(pluginFolder):
        pluginName="%s.py"%pluginDatas["$PLUGINNAME"]
        pluginOut=os.path.join(pluginFolder,pluginName)
        outFile = open(pluginOut,"w")
        outFile.write(datas)
        outFile.close()
    

def fillTemplate(templateFile,pluginDatas):
    """
    fill the template with the given plugin specs
    """
    file = open(templateFile,"r")
    lines=file.readlines()
    
    returnDatas=[]
    for line in lines:
        if line.find("$") != -1:
            for variable , replacement in pluginDatas.iteritems():
                if not replacement:
                    raise Exception , "A missing fariable has been found : %s" %variable
                if line.find(variable) != -1:
                    returnDatas.append(line.replace(variable,replacement))
        else:
            returnDatas.append(line)
            
    returnFile = "".join(returnDatas)
    file.close()    
    return returnFile


def generate(pluginDatas):
    """
    generate the plugin using the provided plugin data
    """
    template=getFileTemplate(pluginDatas)
    file =fillTemplate(template,pluginDatas)
    writeFile(file,pluginDatas)  
    