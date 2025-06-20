def run(): import run
from threading import Thread
Thread(target=run).start()

from requests import get
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import subprocess, json, os

os.system('apt install ffmpeg -y')

def get_video_duration(url):
    cmd = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-show_format',
        url
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        metadata = json.loads(result.stdout)
        duration = float(metadata['format']['duration'])
        return duration
    except Exception as e:
        print("Lỗi khi lấy thời lượng video:", e)
        return None

app = FastAPI()
@app.get("/")
def home(): return 'Success'

@app.get("/video")
def check(link: str = Query(...)):
    try:
        return JSONResponse(content={'length': get_video_duration(link)}, status_code=200)
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)
