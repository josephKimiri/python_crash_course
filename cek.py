import sys
import base64

str_base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789+/'

for a in str_base64:
    for b in str_base64:
        try:
            str_flag = base64.b64decode("R"+a+b+"BR3tCNDUzXzYxWDdZXzRSfQ==")
            if("flag" in str_flag) or ("FLAG" in str_flag):
                print("Found : {}".format(str_flag))
                sys.exit(0)
        except:
            continue        