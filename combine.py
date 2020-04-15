import os
import json
import pandas



dirs = os.listdir('./')

WholeJson = []

for i in dirs:
    if 'WholeJson' in i:
        WholeJson.append(i)

data = {}
data['prod_id'] = [ json.load(open('./'+ i ))['data']['prod_id'] for i in WholeJson]
data['prod_sku'] = [ json.load(open('./'+ i ))['data']['prod_sku'] for i in WholeJson]
data['prod_name'] = [ json.load(open('./'+ i ))['data']['prod_name'] for i in WholeJson]
data['prod_cat'] = [ json.load(open('./'+ i ))['data']['prod_cat'] for i in WholeJson]

frame = pandas.DataFrame(data)
frame.to_csv('./result.csv', index=True,encoding='utf_8_sig')