# -*- coding: utf-8 -*-

import sys
import time

from naoqi import ALProxy


class Pepper(object):
    subscribers = {}

    def __init__(self, app, app_name, pepper_ip, pepper_port):
        # 初期化
        super(Pepper, self).__init__()
        self.app_name = app_name
        self.pepper_ip = pepper_ip
        self.pepper_port = pepper_port

        app.start()
        session = app.session
        # ALMemoryサービスを起動
        self.memory = session.service("ALMemory")

        # 音声設定
        self.tts = ALProxy("ALTextToSpeech", self.pepper_ip, self.pepper_port)
        # 音量設定
        self.audio = ALProxy("ALAudioDevice", self.pepper_ip, self.pepper_port)

        self.Speak(app_name + "を起動します")

    def run(self):
        # 終了条件とループ処理
        print "Starting " + self.app_name
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.Speak(self.app_name + "を停止します")
            print "停止"
            # stop
            sys.exit(0)

    def Speak(self, script, speed=100, voice_sharping=100, volume=40):

        self.audio.setOutputVolume(volume)
        sentence = "\\RSPD={}\\\\VCT={}\\{}\\RST\\"
        speak_id = self.tts.post.say(sentence.format(speed, voice_sharping, script))
        try:
            self.tts.wait(speak_id, 0)
        finally:
            self.Quietly()

    def Quietly(self):
        self.tts.stopAll()
