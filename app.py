import rpc
import time

print("Demo for python-discord-rpc")
client_id = os.getenv('CID') #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
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
    time.sleep(30000)
