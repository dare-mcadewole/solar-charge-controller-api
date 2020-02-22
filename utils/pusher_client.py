import import_env_file
import pusher
import os

class PusherClient:
    _pusher_client = None

    @staticmethod
    def get_client ():
        if not PusherClient._pusher_client:
            PusherClient._pusher_client = pusher.Pusher(
                app_id=os.getenv('PUSHER_APP_ID'),
                key=os.getenv('PUSHER_APP_KEY'),
                secret=os.getenv('PUSHER_APP_SECRET'),
                cluster=os.getenv('PUSHER_APP_CLUSTER'),
                ssl=True
            )
        return PusherClient._pusher_client
