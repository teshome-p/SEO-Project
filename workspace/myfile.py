the_api_key = "AIzaSyBmiAPKcX6M0KrzQkQ8ak0RtzV2Uu87rck"
from pyyoutube import Api
api = Api(api_key=the_api_key)
channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items)