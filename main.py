# -*- coding: utf-8 -*-

import sys
import time

import qi


class Pepper(object):
    subscribers = {}

    def __init__(self, app, pepper_ip, pepper_port):
        from naoqi import ALProxy
        # 初期化
        super(Pepper, self).__init__()
        self.pepper_ip = pepper_ip
        self.pepper_port = pepper_port

        app.start()
        session = app.session
        # ALMemoryサービスを起動
        self.memory = session.service("ALMemory")
        # コールバックを修正

        self.subscribers["TouchChanged"] = self.memory.subscriber("TouchChanged")
        self.subscribers['TouchChanged'].signal.connect(self.TouchChanged)

        # 音声設定
        self.tts = ALProxy("ALTextToSpeech", self.pepper_ip, self.pepper_port)
        # 音量設定
        self.audio = ALProxy("ALAudioDevice", self.pepper_ip, self.pepper_port)

        self.Speak("ロボアプリを起動します")

    def TouchChanged(self, event_name):
        if event_name[0][1]:
            self.Speak(event_name[0][0])
            print event_name[0]

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

    def Speak(self, script, speed=100, voice_sharping=100, volume=20):

        self.audio.setOutputVolume(volume)
        sentence = "\\RSPD={}\\\\VCT={}\\{}\\RST\\"
        speak_id = self.tts.post.say(sentence.format(speed, voice_sharping, script))
        try:
            self.tts.wait(speak_id, 0)
        finally:
            self.Quietly()

    def Quietly(self):
        self.tts.stopAll()


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

What_is_do = Pepper(app, pepper_ip, pepper_port)
What_is_do
What_is_do.run()
