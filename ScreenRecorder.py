import cv2
import d3dshot
import numpy as np
from ScreenRecording_Dimensions import ScreenRegionSelect

class Recorder():
    def __init__(self):
        self.screenshot = d3dshot.create(capture_output='pil')
        self.videolocal = "Captures/Video/"
        self.ext = '.mp4'

    def SelfController(self):
        opts = {'1': self.Capture_Region, '2': self.SceenCaptureDisplay}
        while True:
            print('1- Capture Screen Region 2- Capture Display -9 End')
            answer = input("Enter Option\n")
            if answer in opts:
                self.filename = input("\n Enter File Name")
                self.savestring = self.videolocal + self.filename + self.ext
                print('Hit 0 on screen to end')
                opts[answer]()
            if answer is '9':
                print("End")
                break

    def CaptureLoop(self,frame,region):
        size = frame.size
        vid = cv2.VideoWriter(self.savestring,cv2.VideoWriter_fourcc('M','P','4','V'),26,size)
        while True:
            frame = self.screenshot.screenshot(region)
            key, frame = self.ShowFrame(frame, self.filename)
            vid.write(frame)
            if key == 48:
                vid.release()
                cv2.destroyAllWindows()
                break

    def Capture_Region(self):
        region = ScreenRegionSelect()
        frame = self.screenshot.screenshot(region=(region))
        self.CaptureLoop(frame,region)

    def SceenCaptureDisplay(self):
        displays = self.screenshot.displays.__len__()
        choice = 0
        if displays > 1:
            choice = input("Select display | number of Displays: "+str(displays)+" \n")
        self.screenshot.display = self.screenshot.displays[int(choice)]
        frame = self.screenshot.screenshot()
        region = (0,0,1980,1080)
        self.CaptureLoop(frame,region)

    def ShowFrame(self,frame,name):
        frame = np.array(frame)
        name = str(name)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow(name, frame)
        key = cv2.waitKey(1)
        return key, frame

