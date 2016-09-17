import time

while True:
    if int(round(time.time() * 1000)) % 500 == 0:
        print(int(round(time.time() * 1000)))
    # millis = int(round(time.time() * 1000))
    # print(millis)
