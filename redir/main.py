import requests, json, time, datetime, ctypes, random,sys
import logic
# import notif

header = {'authorization': '--redacted--'}

notif_cooldown = time.time()

vary=lambda bound: random.randint(0,bound)


def retrieve_msg(id):
    """
    Retrieve messages from a channel with id {id}.\n
    :param id: id of channel (int)
    :return: the first 5 messages in format [(message,author),(message,author),...]
    """
    # TODO: make the limit like 10 or smth
    r = requests.get(f'https://discord.com/api/v9/channels/{id}/messages?limit=5', headers=header)
    if r.status_code != 200:
        print(f"ERROR AFOIESF ({time.time()},{datetime.datetime.now()})")
        print(r.text)
        '''msg = f"ERROR ({time.time()},{datetime.datetime.now()})"
        notification.notify(title="SHL error", message=msg, timeout=10)'''
        # notif.error(r.text)
    js = json.loads(r.text)
    result = []
    for v in js:
        # timestamp "2023-03-21T00:42:09.257000+00:00"
        result.append((v['content'], v["author"]['username'], int(datetime.datetime.fromisoformat(v["timestamp"]).timestamp())))
    return result


def post_msg(msg,id=921607732384108575):
    """
    Post a message to a channel with id {id}.\n
    :param msg: list of messages to post in format [message,message,...]
    :return: [sent messages, status code]
    """
    r = [requests.post(f'https://discord.com/api/v9/channels/{id}/messages', data={'content': i}, headers=header) for i
         in msg]
    return [msg, r[0].status_code]


def format(retrieve, response, code):
    """
    Format data to be printed to console.\n
    :param retrieve: Sent messages
    :param response: Bot Response
    :param code: Status code
    :return: None
    """
    # notif.notify("SHL Response!", f"{retrieve[:3]}\n{response}")
    print(f'retrieved {retrieve}\nbot response: {response}\npost with status code: {code}')
    print()

def cycle():
    """
    A Single cycle of the main loop.\n
    :return: None
    """
    r = retrieve_msg(id)
    response = bot.interpret(r)
    if response is not None:
        stat = post_msg(response[0])
    else:
        stat = [None, None]

    if response is not None:
        format(r, response, stat[-1])
    if response == 'restarting...':
        print(f"Restarting... (", datetime.datetime.strftime(time.time()), f", {sys.executable,sys.argv})")
        import os
        os.execl(sys.executable, sys.executable, *sys.argv)

    if time.time()-bot.last_msg>(10*60+vary(10)):
        print('we posta da so hows life')
        post_msg(['._.','so','hows life'])
        bot.last_msg=time.time()
    time.sleep(5)






id = 921607732384108575  # four cheese toast
# id=911440520277033031#alt

bot = logic.Bot()

#Main loop
while True:
    cycle()
