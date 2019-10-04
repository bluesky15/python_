import json

NODE_HOME_MESSAGES = "homemessages"
NODE_MESSAGE = "message"
BASE_PATH = '/Users/lalitkumar.behera/code/LM/Android_app_v2' \
            + '/android_uat_appconfig/android/landmark/config_en_september.json'
# ---------------------------------------
# territory = ["ae", "sa", "bh", "kw"]
# concept = ["homecentre", "centrepoint", "homebox", "babyshop", "lifestyle", "max", "shoemart", "splash"]
# ---------------------------------------
concept = ["splash", "lifestyle"]  # where you want to change the message.
tDict = {"ae": "<b>Free shipping </b>- on orders above AED 63700"}  # what is the message you want
# to change and which concept.

with open(BASE_PATH, 'r') as f:
    config = json.load(f)


def swap_concept():
    global c
    if t == "bh" and c == "babyshop":
        c = "mothercare"


for t in tDict:
    print(t + "------------------")
    for c in concept:
        swap_concept()
        y = config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE]
        print(y)
        config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE] = tDict[t]

        jsonFile = open(BASE_PATH, "w+")
        jsonFile.write(json.dumps(config))
        jsonFile.close()

    print("------------------")
