from pywebio.output  import *
from pywebio.input import *
import time
from pywebio.pin import *
from pywebio.platform import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import argparse
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio_battery import *
from pywebio.session import info
from webdriver_manager.chrome import ChromeDriverManager


app = Flask(__name__)





                

def r():
    with use_scope(name='comm', clear=True):
        s=run_shell(pin.a)
        put_grid([[None,None,None,None,put_text(s,inline=True),None,None,None,None]])



def startw():
    with use_scope(name='comm',clear=True):
        pass

    put_grid([[None,None,None,None,put_input('a',type=TEXT,label='TErmnal'),None,None,None,None]])
    put_grid([[None, None, None, None, put_button('run',onclick=r), None, None, None, None]])


    








app.add_url_rule('/tool','webio.view',webio_view(startw)
                 ,methods=['GET','POST','OPTIONS'])




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(startw, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

