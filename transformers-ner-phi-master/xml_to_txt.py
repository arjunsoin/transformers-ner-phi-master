
import os
import xml.dom.minidom

TRAIN_PATH = 'i2b2/training-PHI-Gold-Set1/'
TEST_PATH = 'i2b2/testing-PHI-Gold-fixed/'
EVAL_PATH = 'i2b2/testing-PHI-Gold-fixed/'

def findAllFiles():
    data = []
    for root, dirs, files in os.walk(EVAL_PATH):
        for file in files:
            data.append(file)
    return data

train_data = findAllFiles()
train_data = sorted(train_data)[1:]

def parseXMLFile(filepath):
    print("-DOCSTART- O")
    print("")
    doc = xml.dom.minidom.parse(filepath)
    text = doc.getElementsByTagName('TEXT')
    tags = doc.getElementsByTagName('TAGS')
    map_idx_to_tags = {}
    tags_list = []
    for idx, nodes in enumerate(tags[0].childNodes):
        if idx % 2 == 1:
            start_idx = nodes.getAttribute('start')
            end_idx = nodes.getAttribute('end')
            type_idx = nodes.getAttribute('TYPE')
            for i in range(int(start_idx), int(end_idx)):
                map_idx_to_tags[i] = type_idx

            tags_list.append(type_idx)
            # if type_idx not in unique_tags:
            #     unique_tags[type_idx] = True
                
    string = text[0].firstChild.nodeValue
    cleaned = ""
    # for e in string:
    #     if e.isalnum():
    #         cleaned += e
    #     else:
    #         cleaned += ' '
    # currIdx = 0
    # for word in cleaned.split(" "):
    #     if len(word) == 0:
    #         # print(word)
    #     else:
    #         if currIdx in map_idx_to_tags:
    #             # print(word, map_idx_to_tags[currIdx])
    #         else:
    #             # print(word, 'O')
    #             continue
    #         currIdx += len(word)
    #     currIdx += 1
    # print(tags_list)
    return tags_list

all_tags = []
for file in train_data:
    all_tags.extend(parseXMLFile(EVAL_PATH + file))

print(set(all_tags))

set_all_tags = set(all_tags)

for elem in set_all_tags:
    print("\"" +  + "\"")