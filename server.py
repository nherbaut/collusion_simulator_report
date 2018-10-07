import random
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from mesa.visualization.TextVisualization import (
    TextData, TextGrid, TextVisualization
)

from model import Schelling


class SchellingTextVisualization(TextVisualization):
    '''
    ASCII visualization for schelling model
    '''

    def __init__(self, model):
        '''
        Create new Schelling ASCII visualization.
        '''
        self.model = model




class HappyElement(TextElement):
    '''
    Display a text count of how many happy agents there are.
    '''

    def __init__(self):
        pass

    def render(self, model):
        return "market_price : " + str(model.market_price)


happy_element = HappyElement()

model_params = {
    "agent_count": 3,
    #"density": UserSettableParameter("slider", "Agent density", 0.8, 0.1, 1.0, 0.1)
}

colors=["aliceblue","antiquewhite","antiquewhite1","antiquewhite2","antiquewhite3","antiquewhite4","aqua","aquamarine1","aquamarine2","aquamarine3","aquamarine4","azure1","azure2","azure3","azure4","banana","beige","bisque1","bisque2","bisque3","bisque4","black","blanchedalmond","blue","blue2","blue3","blue4","blueviolet","brick","brown","brown1","brown2","brown3","brown4","burlywood","burlywood1","burlywood2","burlywood3","burlywood4","burntsienna","burntumber","cadetblue","cadetblue1","cadetblue2","cadetblue3","cadetblue4","cadmiumorange","cadmiumyellow","carrot","chartreuse1","chartreuse2","chartreuse3","chartreuse4","chocolate","chocolate1","chocolate2","chocolate3","chocolate4","cobalt","cobaltgreen","coldgrey","coral","coral1","coral2","coral3","coral4","cornflowerblue","cornsilk1","cornsilk2","cornsilk3","cornsilk4","crimson","cyan2","cyan3","cyan4","darkgoldenrod","darkgoldenrod1","darkgoldenrod2","darkgoldenrod3","darkgoldenrod4","darkgray","darkgreen","darkkhaki","darkolivegreen","darkolivegreen1","darkolivegreen2","darkolivegreen3","darkolivegreen4","darkorange","darkorange1","darkorange2","darkorange3","darkorange4","darkorchid","darkorchid1","darkorchid2","darkorchid3","darkorchid4","darksalmon","darkseagreen","darkseagreen1","darkseagreen2","darkseagreen3","darkseagreen4","darkslateblue","darkslategray","darkslategray1","darkslategray2","darkslategray3","darkslategray4","darkturquoise","darkviolet","deeppink1","deeppink2","deeppink3","deeppink4","deepskyblue1","deepskyblue2","deepskyblue3","deepskyblue4","dimgray","dodgerblue1","dodgerblue2","dodgerblue3","dodgerblue4","eggshell","emeraldgreen","firebrick","firebrick1","firebrick2","firebrick3","firebrick4","flesh","floralwhite","forestgreen","gainsboro","ghostwhite","gold1","gold2","gold3","gold4","goldenrod","goldenrod1","goldenrod2","goldenrod3","goldenrod4","gray","gray1","gray10","gray11","gray12","gray13","gray14","gray15","gray16","gray17","gray18","gray19","gray2","gray20","gray21","gray22","gray23","gray24","gray25","gray26","gray27","gray28","gray29","gray3","gray30","gray31","gray32","gray33","gray34","gray35","gray36","gray37","gray38","gray39","gray4","gray40","gray42","gray43","gray44","gray45","gray46","gray47","gray48","gray49","gray5","gray50","gray51","gray52","gray53","gray54","gray55","gray56","gray57","gray58","gray59","gray6","gray60","gray61","gray62","gray63","gray64","gray65","gray66","gray67","gray68","gray69","gray7"]

chart_data_viz = [{"Label": "market_price_%d" % i, "Color": random.choice(colors)} for i in range(0, model_params["agent_count"])]
happy_chart = ChartModule(chart_data_viz)

server = ModularServer(Schelling,
                       [happy_element, happy_chart],
                       "Schelling", model_params)
server.launch()
