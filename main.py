from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.slider import Slider
from os import listdir 

kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class WaistSlider(Slider):
    pass

class ShoulderSlider(Slider):
    pass
	
class ElbowSlider(Slider):
    pass
	
class WristUpDownSlider(Slider):
	pass

class WristTurnSlider(Slider):
	pass

class ClawSlider(Slider):
	pass
	
class SpeedToggleButton(ToggleButton):
    pass	

class SendButton(Button):
	pass

class Container(BoxLayout):
	speed = 1
	waist = 10
	shoulder = 100
	elbow = 110
	wristUpDown = 130
	wristTurn = 150
	claw = 100
	url = ''
	def new_valueWaist(self, *args):
		self.waistValue.text = str(int(args[1]));
		self.waist = int(args[1])
	def new_valueShoulder(self, *args):
		self.shoulderValue.text = str(int(args[1]));
		self.shoulder = int(args[1])
	def new_valueElbow(self, *args):
		self.elbowValue.text = str(int(args[1]));
		self.elbow = int(args[1])
	def new_valueWristUpDown(self, *args):
		self.wristUpDownValue.text = str(int(args[1]));
		self.wristUpDown = int(args[1])
	def new_valueWristTurn(self, *args):
		self.wristTurnValue.text = str(int(args[1]));
		self.wristTurn = int(args[1])
	def new_valueClaw(self, *args):
		self.clawValue.text = str(int(args[1]));
		self.claw = int(args[1])
	def onClickButton(self, *args):
		self.urlValue.text = self.ipValue.text+'/'+ self.waistValue.text + '|'+ self.shoulderValue.text + '|'+ self.elbowValue.text + '|'+ self.wristUpDownValue.text + '|'+ self.wristTurnValue.text + '|'+ self.clawValue.text + '|' + str(self.speed) + '|'
		self.url = self.urlValue.text
	def toggleButtonPress(self,buttonID):
		self.speed = buttonID

class MainApp(App):

    def build(self):
        self.title = 'Robot Arm Controller'
        return Container()

if __name__ == "__main__":
    app = MainApp()
    app.run()