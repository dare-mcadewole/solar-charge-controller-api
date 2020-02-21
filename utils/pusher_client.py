import import_env_file
import pusher
import os

class PusherClient:
    _pusher_client = None
    def get_client (self):
        if not self._pusher_client:
            self._pusher_client = pusher.Pusher(
                app_id=os.getenv('PUSHER_APP_ID'),
                key=os.getenv('PUSHER_APP_KEY'),
                secret=os.getenv('PUSHER_APP_SECRET'),
                cluster=os.getenv('PUSHER_APP_CLUSTER'),
                ssl=True
            )
        return self._pusher_client
