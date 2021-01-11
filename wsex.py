#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import os
import glob

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

async def layers(websocket, path):
    while True:
        lst = glob.glob("./layers/*.html")
        msg = "\n"
        for a in lst:
            nm = os.path.abspath(a)
            with open(nm, encoding='utf-8') as f:
                msg += f.read()
        await websocket.send(msg)
        await asyncio.sleep(3000)
async def wsjs(websocket, path):
    while True:
        lst = glob.glob("./wsjs/*.js")
        msg = "\n"
        for a in lst:
            nm = os.path.abspath(a)
            with open(nm, encoding='utf-8') as f:
                msg += f.read()
        await websocket.send(msg)
        await asyncio.sleep(3000)

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)

# start_server = websockets.serve(time, "127.0.0.1", 5678)
start_server = websockets.serve(layers, "127.0.0.1", 5678)
start_server2 = websockets.serve(wsjs, "127.0.0.1", 5679)
# start_server = websockets.serve(layers, "127.0.0.1", 5678,ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(start_server2)
asyncio.get_event_loop().run_forever()