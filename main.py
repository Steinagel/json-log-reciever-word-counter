from utils import ListLines
from lib.log_json import readJSONlog
from time import sleep
import json
import random

# LOG_PATH = 'PATH/TO/log_exporter_word_counter/logs/file.log'
############ FOR ME: '/Users/williansteinagel/Pocs/log_exporter_word_counter/logs/file.log'

LOG_PATH = '/Users/williansteinagel/Pocs/log_exporter_word_counter/logs/file.log'
LINE_COUNTER_PATH = 'data/read.json'
RESOULT_JSON = 'data/log_json.json'

def main():
    (update, new_infos) = ListLines(LOG_PATH, LINE_COUNTER_PATH)
    
    if update:
        current_data = json.load(open(RESOULT_JSON))
        value = readJSONlog(new_infos, current_data,(lambda x: x['count'] != None))
        with open('data/log_json.json', 'w') as outfile:
            json.dump(value, outfile)

        sleep(1)

if __name__=='__main__':
    while(True):
        main()
