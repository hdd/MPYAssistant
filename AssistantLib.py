#    import system modules
import os
import sys
import glob

#    setting up the logger
import logging
logging.basicConfig()
log = logging.getLogger("AssistantLib")
log.setLevel(logging.DEBUG)

#    data replacement
pluginDatas={}
pluginDatas["$PLUGINTYPE"]=None
pluginDatas["$PLUGINNAME"]=None
pluginDatas["$NODEID"]=None
pluginDatas["$AUTHOR"]=None
pluginDatas["$DATE"]=None
pluginDatas["$DOCS"]=None

#    template extension
templateExtension="tpy"

#    template name mapper
templateMapping={}
templateMapping["Simple Node"]="simpleNode"
templateMapping["Simple Command"]="simpleCommand"
templateMapping["Simple Locator"]="simpleLocator"


#    test ids from maya dev-kit
defaultNodesIds=["0x87005",\
                 "0x8700B",\
                 "0x87010",\
                 "0x87012",\
                 "0x87018",\
                 "0x87016",\
                 "0x8700E"]

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
            log.error("No template file has been found")
            raise Exception
        
        for template in templates:
            templateName=os.path.basename(template).split(".")[0]
            if not pluginDatas["$PLUGINTYPE"]:
                log.error("No template name has been provided")
                raise Exception
            
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
        log.error("an error occured file datas is empty ")
        raise Exception
    
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
    if not templateFile:
        raise Exception, "No template has been found" 
    
    file = open(templateFile,"r")
    lines=file.readlines()
    
    returnDatas=[]
    for line in lines:
        if line.find("$") != -1:
            for variable , replacement in pluginDatas.iteritems():
                if not replacement:
                    log.error("A missing variable has been found : %s" %variable)
                    raise Exception
                
                if line.find(variable) != -1:
                    returnDatas.append(line.replace(str(variable),str(replacement)))
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
    