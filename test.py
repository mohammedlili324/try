from pywebio.output  import *
from pywebio.input import *
import time
from pywebio.pin import *
from pywebio.platform import *
import argparse
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio_battery import *
from pywebio.session import info
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)





                


def startw():
 
    a = webdriver.Chrome(ChromeDriverManager().install())
   

   







app.add_url_rule('/tool','webio.view',webio_view(startw)
                 ,methods=['GET','POST','OPTIONS'])




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(startw, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)

