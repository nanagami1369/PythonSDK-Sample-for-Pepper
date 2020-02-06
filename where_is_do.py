# -*- coding: utf-8 -*-

import pepper_core


class Pepper(pepper_core.Pepper):
    subscribers = {}

    def __init__(self, app, pepper_ip, pepper_port):
        # 初期化
        super(Pepper, self).__init__(app, "どこタッチ", pepper_ip, pepper_port)

        # 購読を追加
        self.subscribers["TouchChanged"] = self.memory.subscriber("TouchChanged")
        self.subscribers['TouchChanged'].signal.connect(self.TouchChanged)

    def TouchChanged(self, events):
        event = events[0]
        on_touched = event[1]
        where_is_touched = event[0]
        if on_touched:
            self.Speak(where_is_touched)
            print event
