#/usr/env/bin python

#    default modules
import os
import sys
import datetime

#   qt
from PyQt4 import QtGui , uic
from PyQt4 import QtCore

#    local libs
import AssistantLib 

#    import interface
ui_class, base_class = uic.loadUiType("ui/UIAssistant.ui")

#    interface class
class Assistant(ui_class,base_class):
    
    def __init__(self):
        super(Assistant,self).__init__()
        self.setupUi(self)
        self.fillDefaultValues()
        self.setupConnections()
        
    def setupConnections(self):
        QtCore.QObject.connect(self.BT_generate,QtCore.SIGNAL("clicked()"),self.run)
        
        
    def fillDefaultValues(self):
        pluginTypes=AssistantLib.templateMapping
        
        #    set plugin types
        for type in pluginTypes:
            self.CB_pluginType.addItem(type)
        
        #    set nodeIds
        defaultIds=AssistantLib.defaultNodesIds
        for id in defaultIds:
            self.CB_pluginId.addItem(id)
        
        #    user name
        username = os.getenv("USER")
        self.TX_authorName.setText(username)
        
        #    plugin name
        self.TX_pluginName.setText("Change Me")
        
        # docs
        self.TX_description.setPlainText("fill it with a plugin description")
        
        
        self.WB_about.setUrl(QtCore.QUrl("about.html"))
        
    def run(self):
        
        datas=AssistantLib.pluginDatas
        
        #    get the plugin Type
        cbId = self.CB_pluginType.currentIndex()
        cbText = self.CB_pluginType.itemText(cbId)
        template = AssistantLib.templateMapping[str(cbText)]
        datas["$PLUGINTYPE"]=template
        
        # get the plugin Name
        plugname = str(self.TX_pluginName.text())
        if plugname.find(" ")!=-1:
            raise Exception , "pluginName can't contain spaces"
        
        datas["$PLUGINNAME"]=plugname
        
        datas["$AUTHOR"]=self.TX_authorName.text()
        
        datas["$DATE"]=datetime.datetime.now()
        
        datas["$DOCS"]=self.TX_description.toPlainText()
        
        # run the builder
        AssistantLib.generate(datas)
        
        
        
if __name__ == "__main__":      
    App=QtGui.QApplication(sys.argv)
    AssistantApp = Assistant()
    AssistantApp.show()
    App.exec_()