import json

NODE_HOME_MESSAGES = "homemessages"
IMG_NODE = "image"
NODE_MESSAGE = "message"
BASE_PATH = "/Users/lalitkumar.behera/code/LM/android_config/android/landmark/config_{}_6.{}.json"
# ---------------------------------------
# territory = ["ae", "sa", "bh", "kw"]
# concept = ["homecentre", "centrepoint", "homebox", "babyshop", "lifestyle", "max", "shoemart", "splash"]
# ---------------------------------------
types = ["ar", "en"]
allPaths = []


def gen_file_path(lang):
    global i
    initial_index = 14
    for i in range(8):
        allPaths.append(BASE_PATH.format(lang, initial_index + i), )


concept = ["babyshop"]  # where you want to change the message.
dict_ar = {"ae": "خصم إضافي 10% لحاملي بطاقات بنك دبي الإمارات الوطني",
           "bh": " 9خصم إضافي 10% لحاملي بطاقات بنك دبي الإمارات الوطني"}  # what is the message you want

dict_en = {"ae": "english",
           "bh": " english 77"}  # what is the message you want


# to change and which concept.


def swap_concept():
    global c
    if t == "bh" and c == "babyshop":
        c = "mothercare"


for lang in types:
    gen_file_path(lang)
    if lang == "ar":
        dict_l = dict_ar
    else:
        dict_l = dict_en

    for i in range(len(allPaths)):
        with open(allPaths[i], 'r') as f:
            config = json.load(f)

        for t in dict_l:
            print(t + "------------------" + allPaths[i])
            for c in concept:
                swap_concept()
                print(t + " " + c + " Old: " + config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE])
                config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE] = dict_l[t]
                config[NODE_HOME_MESSAGES][t][c][0][IMG_NODE] = ""  # in case of removing icon - shipping
                print(t + " " + c + " New: " + config[NODE_HOME_MESSAGES][t][c][0][NODE_MESSAGE])
                jsonFile = open(allPaths[i], "wb+")
                jsonFile.write(json.dumps(config, ensure_ascii=False, indent=2).encode())
                jsonFile.close()
            print("------------------")
