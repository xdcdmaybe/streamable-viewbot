import json
import time
import websocket
from concurrent.futures import ThreadPoolExecutor
import uuid
import re
import sys
views = 0
print('by https://github.com/xdcdmaybe')
link = input('link: ')
id = re.search(r'https://streamable.com/(\w+)', link)
threads = input('enter threads: ')
def send_message(): 
    ws = websocket.create_connection("wss://socket.streamable.com/")
    global views
    while True:
        message = {
            "type": "play",
            "progress": "1.00",
            "shortcode": id.group(1),
            "loops": 1,
            "timestamp": int(time.time()),
            "id": str(uuid.uuid4()).upper().replace("-", "")[:24],
            "referrer": ""
        }
        ws.send(json.dumps(message))
        views = views + 1
        sys.stdout.write(f"\rbotted {views:,} views")
        sys.stdout.flush()

    ws.close()

with ThreadPoolExecutor(max_workers=int(threads)) as executor:
    for _ in range(int(threads)):
        executor.submit(send_message)
