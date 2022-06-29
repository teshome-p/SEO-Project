from pyyoutube import Api
import pprint
the_api_key = "AIzaSyBmiAPKcX6M0KrzQkQ8ak0RtzV2Uu87rck"
api = Api(api_key=the_api_key)
channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items[0].to_dict()["snippet"]["description"])
#ct_by_channel = api.get_comment_threads(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw", count=2)
#print(ct_by_channel)
r = api.get_activities_by_channel(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw", count=2)
print(r.items[0].to_dict()["snippet"]["description"])
