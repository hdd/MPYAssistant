import os
import sys
import datetime

from PyQt4 import QtGui , uic
from PyQt4 import QtCore

import ui.UIAssistant as UiAssistant
import AssistantLib 


ui_class, base_class = uic.loadUiType("ui/UIAssistant.ui")

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
        for type in pluginTypes:
            self.CB_pluginType.addItem(type)
            
        defaultIds=AssistantLib.defaultNodesIds
        for id in defaultIds:
            self.CB_pluginId.addItem(id)
            
        username = os.getenv("USER")
        self.TX_pluginName.setText("Change Me")
        self.TX_authorName.setText(username)
        self.TX_description.setPlainText("fill it with a plugin description")
        
        
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