from __future__ import print_function

import socket
import time

retry = 5
delay = 10
timeout = 3

def isOpen(ip, port, timeouts=timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeouts)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

def checkHost(ip, port, retries=retry, delays=delay):
    ipup = False
    for i in range(retries):
        if isOpen(ip, port):
            ipup = True
            break
        else:
            time.sleep(delays)
    return ipup

if (__name__ == '__main__'):
    ip = "google.com"
    port = 443

    if checkHost(ip, port):
        print_function(ip + " is UP")