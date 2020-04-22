import requests
import attr
import datetime
from config import CONFIG


@attr.s
class UserMessage(object):
    text: str = attr.ib()
    peer_id: str = attr.ib()
    out: bool = attr.ib()

    @classmethod
    def from_request(cls, req):
        message = req["last_message"]
        return cls(
            text=message["text"],
            peer_id=str(message["peer_id"]),
            out=bool(message["out"]),
        )

    @property
    def is_from_user(self):
        return self.out is False

    @property
    def is_admin(self):
        return self.peer_id in CONFIG.admin_peers


def main():
    values = {
        'access_token': CONFIG.access_token,
        'chatId': '194558422',
        'v': '5.50',
        'filter': 'all',
    }
    r = requests.post(
        'https://api.vk.com/method/messages.getConversations',
        values
    )
    print(r.json())
    items = r.json()["response"]["items"]
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    for item in items:
        user_message = UserMessage.from_request(item)
        print(user_message)
        if user_message.is_from_user:
            reply(user_message, today)
        elif user_message.is_admin:
            pass


def reply(user_message: UserMessage, today: str):
    values = {
        'access_token': CONFIG.access_token,
        'peer_id': user_message.peer_id,
        'message': f'{today}: принято "{user_message.text}"',
        'v': '5.50',
    }
    r = requests.post(
        'https://api.vk.com/method/messages.send',
        values
    )
    print(r.json())


main()