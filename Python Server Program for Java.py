#Server prg
import socket
import math
import datetime
import random
import numpy as np
import pandas as pd
from scipy import constants
import sys, os
def is_float(a_string):
    try:
        float(a_string)
        return True
    except ValueError:
        return False
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname() ,1234))  
    print(socket.gethostname())
    s.listen(5)
    while True:
        clt,adr=s.accept()
        msg=clt.recv(4096)
        code=msg.decode("utf-8")
        
        if(code=="exit()" or code=="quit()"):
            print("output-0: ",code)
            sys.exit("You have stoped") 
            clt.close()
        elif(code.endswith(".csv")):
            df = pd.read_csv(code)
            clt.send("pandas dataframe object with 'df' loaded.".encode())
        else:
            exec(f"out= "+code) #, globlsparam,  localsparam)
            output=str(out)
            
            if(output.isnumeric()):
                clt.send(bytes(out))
                print("output-1: ",out)
            elif (is_float(output)):
                clt.send(output.encode())
                print("output-1: ",output)
            else:
                clt.send(output.encode())
                print("output-2: ",output)
except Exception as err:
    print(f"Unexpected {err=}")
    error=str('Runtime Error: ') + str(err)
    clt.send(error.encode())
    clt.close()
    raise    


