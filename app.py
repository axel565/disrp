import rpc
import time
import os

print("Demo for python-discord-rpc")

client_id = os.getenv('CID')
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) 

print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Playing",
            "details": "Skyblock Green S2",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Text for small_image",
                "small_image": "img_small",
                "large_text": "Text for large_image",
                "large_image": "img_large"
            }
        }
    rpc_obj.set_activity(activity)
    
