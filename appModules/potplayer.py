# -*- coding: utf-8 -*-

# appModule for Daum potplayer (automatic reading subtitle and play information)
# Copyright <2016> aheu <advck1123 at GMail Dot com>, license details <license.txt>
'''Release Note
- 0.1: Initial release
- 0.2: Improve sub and message notify function
- 0.3 Add support potplayer mini and add readme
'''

import api
import appModuleHandler
import controlTypes
import eventHandler
from NVDAObjects.window import Window
import ui

class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		obj = api.getForegroundObject()
		obj.name = obj.windowText
		if obj.windowClassName == 'PotPlayer' and obj.role == controlTypes.ROLE_STATICTEXT and not obj.name == "":
			ui.message(obj.name)
			nextHandler()
