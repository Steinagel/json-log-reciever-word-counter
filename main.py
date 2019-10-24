from utils import ListLines
from lib.log_json import readJSONlog
from time import sleep
import json
import random
import asyncio
from lib.jsonpath_exporter.exporter import start_exporter

# LOG_PATH = 'PATH/TO/log_exporter_word_counter/logs/file.log'
############ FOR ME: '/Users/williansteinagel/Pocs/log_exporter_word_counter/logs/file.log'

LOG_PATH = '/Users/williansteinagel/Pocs/log_exporter_word_counter/logs/file.log'
LINE_COUNTER_PATH = 'data/read.json'
RESOULT_JSON = 'data/log_json.json'

async def update_json():
    while(True):
        (update, new_infos) = ListLines(LOG_PATH, LINE_COUNTER_PATH)
        if update:
            current_data = json.load(open(RESOULT_JSON))
            value = readJSONlog(new_infos, current_data,(lambda x: x['count'] != None))
            with open('data/log_json.json', 'w') as outfile:
                json.dump(value, outfile)

            await asyncio.sleep(0.1)
    

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(start_exporter('lib/jsonpath_exporter/config.yml'), update_json()))
    loop.close()