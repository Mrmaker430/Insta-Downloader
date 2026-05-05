#https://t.me/Masterolic
from pyrogram import filters, Client 
import bs4, requests, logging 
from os import environ,cpu_count
from dotenv import load_dotenv
import multiprocessing 
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
load_dotenv("config.env")
API_ID=int(environ['API_ID'])
API_HASH=environ['API_HASH']
BOT_TOKEN=environ['BOT_TOKEN']
LOG_GROUP=environ.get('LOG_GROUP',"")
DUMP_GROUP=environ.get('DUMP_GROUP',"")
OWNER_ID=int(environ['OWNER_ID'])
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
if LOG_GROUP:
   LOG_GROUP=int(LOG_GROUP)
if DUMP_GROUP:
   DUMP_GROUP=int(DUMP_GROUP)
Mbot=Client(name="instabot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=64,
            sleep_threshold=22)

def run_healthcheck_server():
    port = environ.get("PORT")
    if not port:
        return
    class HealthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Insta-DL bot is running")
        def log_message(self, format, *args):
            return
    server = HTTPServer(("0.0.0.0", int(port)), HealthHandler)
    Thread(target=server.serve_forever, daemon=True).start()
if __name__ == '__main__':
    print (" Insta-DL Bot started  running...")
    run_healthcheck_server()
    num_workers = cpu_count()
    pool = multiprocessing.Pool(processes=num_workers)
    Mbot.run()
    pool.close()
    pool.join()
