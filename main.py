# -*- coding: utf-8 -*-

import sys
import time

import qi


class Pepper(object):
    """
    A simple class to react to face detection events.
    """

    subscribers = {}

    def __init__(self, app):
        # 初期化
        super(Pepper, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.

        self.subscribers["FrontTactilTouched"] = self.memory.subscriber("FrontTactilTouched")
        self.subscribers['FrontTactilTouched'].signal.connect(self.FrontTactilTouched)
        self.subscribers["HandLeftBackTouched"] = self.memory.subscriber("HandLeftBackTouched")
        self.subscribers['HandLeftBackTouched'].signal.connect(self.HandLeftBackTouched)
        self.subscribers["HandLeftLeftTouched"] = self.memory.subscriber("HandLeftLeftTouched")
        self.subscribers['HandLeftLeftTouched'].signal.connect(self.HandLeftLeftTouched)
        self.subscribers["HandRightRightTouched"] = self.memory.subscriber("HandRightRightTouched")
        self.subscribers['HandRightRightTouched'].signal.connect(self.HandRightRightTouched)
        self.subscribers["HandRightRightTouched"] = self.memory.subscriber("HandRightRightTouched")
        self.subscribers['HandRightRightTouched'].signal.connect(self.HandRightRightTouched)
        self.subscribers["MiddleTactilTouched"] = self.memory.subscriber("MiddleTactilTouched")
        self.subscribers['MiddleTactilTouched'].signal.connect(self.MiddleTactilTouched)
        self.subscribers["RearTactilTouched"] = self.memory.subscriber("RearTactilTouched")
        self.subscribers['RearTactilTouched'].signal.connect(self.RearTactilTouched)

        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")
        # 音量設定
        self.audio = session.service("ALAudioDevice")

    def FrontTactilTouched(self, value):
        self.Speak("あたま")

    def HandLeftBackTouched(self, value):
        self.Speak("てのこう")

    def HandLeftLeftTouched(self, value):
        self.Speak("てのひら")

    def HandLeftLeftTouched(self, value):
        self.Speak("てのこう")

    def HandRightRightTouched(self, vale):
        self.Speak("てのひら")

    def MiddleTactilTouched(self, value):
        self.Speak("あたまのちゅうおう")

    def RearTactilTouched(self, value):
        self.Speak("ゆっくりでね")

    def run(self):
        # 終了条件とループ処理
        print "Starting What_is_do"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.Speak("ロボアプリを停止します")
            print "停止"
            # stop
            sys.exit(0)

    def Speak(self, script, speed=100, voice_sharping=100, volume=40):
        self.audio.setOutputVolume(volume)
        sentence = "\\RSPD={}\\\\VCT={}\\{}\\RST\\"
        self.tts.say(sentence.format(speed, voice_sharping, script))


if __name__ == "__main__":
    import os

    pepper_ip = os.environ.get("PEPPER_IP")
    pepper_port_row = os.environ.get("PEPPER_PORT")
    pepper_port = int(pepper_port_row)
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + pepper_ip + ":" + str(pepper_port)
        app = qi.Application(["What_is_do", "--qi-url=" + connection_url])
    except RuntimeError:
        error_message = "Pepperに接続できませんでした\n ip={}\n port={}\n"
        error_message.format(pepper_ip, pepper_port)
        sys.exit(1)

What_is_do = Pepper(app)
What_is_do
What_is_do.run()
