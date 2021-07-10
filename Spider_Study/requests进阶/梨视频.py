# 拿到contId
# 拿到videoStatus接口返回的json拿到src
# 修改src内容
# 下载视频
import requests

url = "https://www.pearvideo.com/video_1734701"

contId = url.split("_")[1]

video_data_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.376240983804798"
headers = {
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    # 防盗链
    "Referer": url
}
resp = requests.get(video_data_url, headers=headers)

dict = resp.json()
srcUrl = dict['videoInfo']['videos']['srcUrl']
systemTime = dict['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# 下载视频

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

print("over!")
