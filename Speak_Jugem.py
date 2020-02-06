# -*- coding: utf-8 -*-

import sys
import time

from naoqi import ALProxy


class Pepper(object):
    subscribers = {}

    def __init__(self, app, pepper_ip, pepper_port):
        # 初期化
        super(Pepper, self).__init__()
        self.pepper_ip = pepper_ip
        self.pepper_port = pepper_port

        app.start()
        session = app.session
        # ALMemoryサービスを起動
        self.memory = session.service("ALMemory")

        # 購読を追加
        self.subscribers["TouchChanged"] = self.memory.subscriber("TouchChanged")
        self.subscribers['TouchChanged'].signal.connect(self.Jugem)

        # 音声設定
        self.tts = ALProxy("ALTextToSpeech", self.pepper_ip, self.pepper_port)
        # 音量設定
        self.audio = ALProxy("ALAudioDevice", self.pepper_ip, self.pepper_port)

        self.Speak("スピークじゅげむを起動します")

    def Jugem(self, event):
        on_touched = event[0][1]
        where_is_touched = event[0][0]
        if on_touched and where_is_touched == "LArm":
            self.Speak(
                "じゅげむじゅげむごこうのすりきれかいじゃりすいぎょのすいぎょうまつくうねるところにすむところやぶらこうじのやぶこうじぱいぽぱいぽぱいぽのしゅーりんがんしゅーりんがんのぐーりんだいぐーりんだいのぽんぽこぴーのぽんぽこなーのちょうくめいのちょうすけ")
            print "寿限無寿限無五劫の擦り切れ海砂利水魚の水行末雲来末風来末食う寝る処に住む処やぶら小路の藪柑子" + \
                  "パイポパイポパイポのシューリンガンシューリンガンのグーリンダイグーリンダイのポンポコピーの" + \
                  "ポンポコナーの長久命の長助"
        elif on_touched and where_is_touched == "RArm":
            self.Quietly()

    def run(self):
        # 終了条件とループ処理
        print "Starting Speak_Jugem"
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.Speak("スピークじゅげむを停止します")
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
