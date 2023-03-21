import time, requests, json, datetime, ctypes, random, sys
import util
from util import header


class Bot:
    def __init__(self):
        self.last_msg = 0

    @staticmethod
    def clean(s: str) -> str:
        """
        Removes all spaces, punctuation, and lowercases the string
        :param s: the string
        :return: the formatted string
        """
        s = [i for i in s.strip().lower()]
        for i, char in enumerate(s):
            if char in [j for j in "\"';:,<.>/?[{]}\\|=+-_)(*&^%$#@!~` "]:
                s[i] = ""
        return "".join(s)

    @staticmethod
    def check_chain() -> bool:
        """
        Checks if the last 21 or so messages are repeats of ['._.','so','hows life']
        :param messages: the messages
        :return: True if the last 21 messages are repeats of ['._.','so','hows life'], False otherwise
        """
        # r = requests.get(f'https://discord.com/api/v9/channels/{id}/messages?limit=21', headers=header)
        # if r.status_code != 200:
        #     print(f"ERROR AFOIESF ({time.time()},{datetime.datetime.now()})")
        #     print(r.text)
        #     '''msg = f"ERROR ({time.time()},{datetime.datetime.now()})"
        #     notification.notify(title="SHL error", message=msg, timeout=10)'''
        #     # notif.error(r.text)
        # result, js = [], json.loads(r.text)
        # for v in js:
        #     # timestamp in iso format
        #     result.append((v['content'], v["author"]['username'],
        #                    int(datetime.datetime.fromisoformat(v["timestamp"]).timestamp())))
        #
        # # check if the last 21 messages are repeats of ['._.','so','hows life']
        # if len(result) < 21:
        #     return False
        # for i in range(21):
        #     if result[i][0] not in ['._.', 'so', 'hows life']:
        #         return False
        # return True
        return False

    def interpret(self, messages: list) -> (list[str], any):
        self.last_msg = messages[0][2]
        # messages ex: [('hello', `user`), ('how are you', `user`), ...]
        # 0 index is the most recent message

        # howslife
        if Bot.clean(messages[0][0]) == "howslife" and messages[0][1] != "imapotatoes11":
            if Bot.check_chain():
                return ["._."], "shl.chain"
            if Bot.clean(messages[1][0]) == "so" and messages[0][1] != "imapotatoes11":
                if messages[2][0] == "._." and messages[0][1] != "imapotatoes11":
                    return ["._.", "so", "hows life"], "shl.standard"
            elif messages[0][1] != "imapotatoes11":
                if messages[1][1] == "No u" and messages[0][1] != "imapotatoes11":
                    return ["._."], "shl.fake_alex"
                elif messages[0][1] != "imapotatoes11":
                    return ["._."], "shl.fake_standard"

        # bot detection
        if "bot" in Bot.clean(messages[0][0]) and messages[0][1] != "imapotatoes11":
            return ["._."], "bot_detection.standard"

        # chain detection
        if messages[0][0] == messages[1][0] == messages[2][0] and messages[0][1] != "imapotatoes11":
            return [messages[0][0]], "chain.standard"
