from app.andrew_based import AndrewBased
from app.twitter import Twitter
import requests
import json
import sys

FILESTORAGE = "replied_mentions.txt"

t = Twitter()
a = AndrewBased()

response = t.get_most_recent_mention()

tweet_json = json.loads(json.dumps(response[0]._json))

try:
    image_url = tweet_json['entities']['media'][0]['media_url']
    screen_name = tweet_json['user']['screen_name']
    id = tweet_json["id_str"]
except Exception as ex:
    print("Unable to get media. Probably no media")
    raise ex

# logic for not repeating mentions
with open(FILESTORAGE, "r") as f:
    """"""
    #f.read()
    for x in f:
        if x == id:
            print("we done did it")
            sys.exit(0)

with open(FILESTORAGE, "a") as e:
    e.write(id)

img_data = requests.get(image_url).content

incoming_file_name = a._random_file_name(8)
with open(incoming_file_name, 'wb') as handler:
    handler.write(img_data)

generated_file_name = a.builder(incoming_file_name)

media_id = t.upload_image(generated_file_name)
t.tweet(
    f"Hey @{screen_name}, here is your image.",
    media_id=media_id
)

a.delete_file(overlay_image=incoming_file_name)