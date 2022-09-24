from fastapi import FastAPI, WebSocket
import asyncio
import logging

logging.basicConfig(filename='server.log', level= logging.INFO)
app = FastAPI()


@app.websocket("/")
async def process_audio_stream(websocket: WebSocket):
    await websocket.accept()
    while True:
        audio_chunk = await websocket.receive()
        logging.info("received"+str(audio_chunk))
        await websocket.send({"type": "websocket.send", "text": "received: "+audio_chunk.get("text")})
        await asyncio.sleep(1)
