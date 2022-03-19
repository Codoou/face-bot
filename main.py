from tabnanny import check
from app.andrew_based import AndrewBased
from app.twitter import Twitter
import requests
import json
import sys

FILESTORAGE = "replied_mentions.txt"
ME = "codyzdotorg".lower()

def add_id(id):
    with open(FILESTORAGE, "a") as e:
        e.write(id+'\n')

def check_if_id_exists(id):
    # logic for not repeating mentions
    # Exits if it does to prevent multiple runs per id
    with open(FILESTORAGE, "r") as f:
        """"""
        for x in f:
            if x.strip() == str(id).strip():
                print("we done did it")
                sys.exit(0)

def check_if_self(screen_name):
    if screen_name.lower() == ME:
        print("Hey I did the last mention, I will stop now")
        sys.exit(0)

t = Twitter()
a = AndrewBased()

response = t.get_most_recent_mention()

tweet_json = json.loads(json.dumps(response[0]._json))

screen_name = tweet_json['user']['screen_name']
id = tweet_json["id_str"]

try:
    image_url = tweet_json['entities']['media'][0]['media_url']
except Exception as ex:
    print("Unable to get media. Probably no media")
    add_id(id)
    raise ex

check_if_id_exists(id)
add_id(id)
check_if_self(screen_name=screen_name)


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