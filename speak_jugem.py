# -*- coding: utf-8 -*-

import pepper_core


class Pepper(pepper_core.Pepper):
    subscribers = {}

    def __init__(self, app, pepper_ip, pepper_port):
        # 初期化
        super(Pepper, self).__init__(app, "スピークじゅげむ", pepper_ip, pepper_port)

        # 購読を追加
        self.subscribers["TouchChanged"] = self.memory.subscriber("TouchChanged")
        self.subscribers['TouchChanged'].signal.connect(self.Jugem)

    def Jugem(self, events):
        event = events[0]
        on_touched = event[1]
        where_is_touched = event[0]
        if on_touched and where_is_touched == "LArm":
            self.Speak(
                "じゅげむじゅげむごこうのすりきれかいじゃりすいぎょのすいぎょうまつくうねるところにすむところやぶらこうじのやぶこうじぱいぽぱいぽぱいぽのしゅーりんがんしゅーりんがんのぐーりんだいぐーりんだいのぽんぽこぴーのぽんぽこなーのちょうくめいのちょうすけ")
            print "寿限無寿限無五劫の擦り切れ海砂利水魚の水行末雲来末風来末食う寝る処に住む処やぶら小路の藪柑子\n" + \
                  "パイポパイポパイポのシューリンガンシューリンガンのグーリンダイグーリンダイのポンポコピーの\n" + \
                  "ポンポコナーの長久命の長助\n"
        elif on_touched and where_is_touched == "RArm":
            self.Quietly()
            print "音声を停止しました"
