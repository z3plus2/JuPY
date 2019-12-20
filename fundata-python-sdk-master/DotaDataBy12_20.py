import json
import os
import sys
import time
from pprint import pprint
from fundata.request import ApiClient
from fundata.client import init_api_client
from fundata.dota2.match import get_batch_basic_info

print(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

public_key = '7f78fb5fe20074f4aeabae0b233845d3'
secret_key = 'c56e24ea4c92bb392b20ab1fe1025326'

client = ApiClient(public_key, secret_key)

# 准备 API 需要的参数
uri = '/fundata-dota2-free/v2/match/general-info'
StartId = 5157360000  #16日晚上

SUM: int=100000


with open('list12-20.csv', 'w', encoding='utf-8') as fout:
    a: int=1
    while a<SUM:
        StartId+=1
        time.sleep(0.1)

        data = {"match_id": StartId}

        try:
            res = client.api(uri, data)
        except Exception:
            time.sleep(0.2)
        # pprint(res)
        if res['retcode']==200 and res['data']['human_players']==10 and res['data']['lobby_type']==7:
            strPlayer=''
            # pprint(res['data']['start_time'])
            for item in res['data']['players']:
                 strPlayer+=','+str(item['player_slot'])+','+str(item['hero_id'])+','+str(item['last_hits'])

            fout.write(str(res['data']['match_id'])+','+str(res['data']['game_mode'])+','+str(res['data']['duration'])+','+str(res['data']['human_players'])+','+str(res['data']['radiant_win'])+strPlayer+'\n')
        else:
            continue
        a+=1


