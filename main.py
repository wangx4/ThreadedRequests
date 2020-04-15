import threading
import requests
import time
import json

def thread_print(i):
    url = r'https://clarksonmsda.org/api/get_product.php?pid='+str(i)
#    print(url)
    r = requests.get(url)
    try:
        if 'q' in r.json():
            if r.json()['data'] != None and r.json()['data']['prod_id']!=None and r.json()['data']['prod_sku']!=None and r.json()['data']['prod_cat']!=None and r.json()['data']['prod_name']!=None:
                with open('./WholeJson'+str(i)+'.json', "w") as f:
                    f.write(json.dumps(r.json()))
                    f.close()
            else:
                with open('./NoDataJson'+str(i)+'.json', "w") as f:
                    f.write(json.dumps(r.json()))
                    f.close()
    except:
        with open('./NoneJson'+str(i)+'.json', "w") as f:
            f.write(json.dumps(r.json()))
            f.close()


threads = []




for i in range(201):
    threads.append(threading.Thread(target=thread_print,args=(i,)))




for th in threads:th.start()




for th in threads:th.join()


print("finished")
