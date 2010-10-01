import sys
import datetime

from PyQt4 import QtGui , uic
from PyQt4 import QtCore

import ui.UIAssistant as UiAssistant
import AssistantLib 


ui_class, base_class = uic.loadUiType("ui/UIAssistant.ui")
print ui_class 
print base_class

#print assistantUi

class Assistant(ui_class,base_class):
    def __init__(self):
        super(Assistant,self).__init__()
        self.setupUi(self)
        
        pluginTypes=AssistantLib.templateMapping
        for type in pluginTypes:
            self.CB_pluginTipe.addItem(type)
            
        defaultIds=AssistantLib.defaultNodesIds
        for id in defaultIds:
            self.CB_pluginId.addItem(id)
        
    def getValues(self):
        datas=AssistantLib.pluginDatas
        datas["$PLUGINTYPE"]=self.CB_pluginTipe
        datas["$PLUGINNAME"]=self.TX_pluginName
        datas["$AUTHOR"]=self.TX_authorName
        datas["$DATE"]=datetime.datetime.now()
        datas["$DOCS"]=datetime.datetime.now()       
        
        
App=QtGui.QApplication(sys.argv)
AssistantApp = Assistant()
AssistantApp.show()
App.exec_()