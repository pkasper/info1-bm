import machine, neopixel, network
import time, json, os
import urequests as requests
from settings import DIMM, SLEEP_INTERVAL, READ_INTERVAL, LEDPIN

from random import randrange
np = neopixel.NeoPixel(machine.Pin(LEDPIN),10)
np.fill((0,0,0))
np.write()
##############################################################################
#wlan = network.WLAN(network.STA_IF)
#wlan.active(False)

myfile= "last10.json"
index = 0
try:
    with open(myfile,"r") as f:
        raw_data = f.read()
        data = json.loads(raw_data)
        last10 = data['last10']
        index = data['index']
        del raw_data
        del data
except (OSError, TypeError):
    last10 = ["000000000000000000af11ed56cddd78793d9d7cb42ad4b6f0986634c7690518",
                "000000000000000000786daed0aef5332fc3ac44ee1127525eeb16b1a3b6e0be",
                "00000000000000000014515fffe0f07eb8f1fe89d4d184263cbb5983dc5bfbbc",
                "0000000000000000004961f628037d20ad76dec96d46d0c8dfc90bee3481ef60",
                "00000000000000000005dfa9e6053bec0df032c91c63e4ccb635b5ba0fe9dd26", ]
    last10.extend([None]*5)
    pass

display_index = 0

def get_last_hash():
    r = requests.get("https://blockchain.info/q/latesthash")
    block_hash = r.content.decode()
    r.close()
    print(block_hash)
    return block_hash

def change_hash_on_leds():
    global display_index
    oldindex = display_index
    display_index += 1
    display_index %= 10
    while last10[display_index] == None:
        print(display_index)
        display_index += 1
        display_index %= 10
    show_hash_on_leds(last10[display_index])


def get_color_tuples(block_hash):
    colors = [block_hash[i*6+4:i*6+(4+6)] for i in range(10)]
    return [(int(int(c[:2],16)*DIMM),int(int(c[2:4],16)*DIMM),int(int(c[4:6],16)*DIMM)) for c in colors]
    # (230,50,4)
def show_hash_on_leds(block_hash):
    enc_cs = get_color_tuples(block_hash)
    for i in range(10):
        np[i] = enc_cs[i]
    np.write()


def save_file():
    with open(myfile,"w") as f:
        data = {"last10": last10, "index": index}
        f.write(json.dumps(data))

def save_new_hash(block_hash):
    global last10, index
    if block_hash in last10:
        return
    last10[index] = block_hash
    save_file()
    index += 1
    index %= 10

def fade_to_black(step=0.5):
    for index in range(10):
        ledr = int(np[index][0]*step) if np[index][0]*step >= 1 else 0
        ledg = int(np[index][1]*step) if np[index][1]*step >= 1 else 0
        ledb = int(np[index][2]*step) if np[index][2]*step >= 1 else 0
        np[index] = (ledr,ledg,ledb)
    np.write()

def sparcle():
    while True:
        # np[randrange(0,10)] = (55,25,0)
        np[randrange(0,10)] = (55,55,55)
        np.write()
        fade_to_black(0.65)
        time.sleep_ms(55)


def sparcle_rg():
    while True:
        nums = [(randrange(0,100),randrange(0,100),0) for x in range(0,10)]
        np.fill((0,0,0))
        for led in range(0,10):
            np[led] = nums[led]
        np.write()
        #fade_to_black(np)
        time.sleep_ms(100)

sparcle_rg()


# update_time = 0
# while True:
#     if update_time == 0 or update_time + READ_INTERVAL*1000 < time.ticks_ms():
#         update_time = time.ticks_ms()
#         # get_and_write_hash_to_pixels()
#         #bh = get_last_hash()
#         #save_new_hash(bh)
#     change_hash_on_leds()
#     time.sleep_ms(int(SLEEP_INTERVAL*1000))
