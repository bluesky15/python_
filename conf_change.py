import json

NODE_HOME_MESSAGES = "homemessages"
NODE_MESSAGE = "message"
BASE_PATH = '/Users/lalitkumar.behera/code/LM/android_config/android/landmark/config_en_6.21.json'
# ---------------------------------------
# territory = ["ae", "sa", "bh", "kw"]
# concept = ["homecentre", "centrepoint", "homebox", "babyshop", "lifestyle", "max", "shoemart", "splash"]
# ---------------------------------------
concept = ["babyshop"]  # where you want to change the message.
tDict = {"sa": "<b>Free shipping </b>- on orders above SAR 100"}  # what is the message you want
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
        print(t + " " + c + " Old: " + config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE])
        config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE] = tDict[t]
        print(t + " " + c + " New: " + config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE])
        jsonFile = open(BASE_PATH, "w+", encoding="utf-8")
        jsonFile.write(json.dumps(config, ensure_ascii=False))
        jsonFile.close()
    print("------------------")
