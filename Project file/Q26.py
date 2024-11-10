import time

def print_time_functions():
    print("time():", time.time())
    utc_time = time.gmtime()
    print("gmtime():", utc_time)
    local_time = time.localtime()
    print("localtime():", local_time)
    epoch_time = time.mktime(local_time)
    print("mktime(localtime()):", epoch_time)
    print("ctime():", time.ctime())
    print("asctime(gmtime()):", time.asctime(utc_time))

print_time_functions()
