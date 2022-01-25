import requests
import js2py
import sys
import time
import os

def main():
    output_file = "MixDrop.m3u" # Output file name
    if os.path.exists(output_file):
        os.remove(output_file)
    m3uarr = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    def grab(urlin):
        r = requests.get(urlin, headers=headers).text.replace('\n', '').split("return p}")[1].split("}))")[0] + "})"
        inputLink = "f" + r + ";"
        code = open('compiler.js', 'r').read() + inputLink
        print(inputLink)
        videoURL = "https://" + js2py.eval_js(code).split('MDCore.wurl="//')[1].split('";')[0]
        return videoURL
    m3uarr.append("#EXTM3U")
    for info in open('info.txt', 'r', encoding="utf-8"):
        info = info.split('\n')[0]
        if not info == "" or not info == None:
            name = info.split(' | ')[0]
            url = info.split(' | ')[1]
            group = info.split(' | ')[2]
            logo = info.split(' | ')[3]
            m3uarr.append(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}')
            m3uarr.append(grab("https://mixdrop.co/e/" + url))
    for i in m3uarr:
        with open(output_file, 'a') as f:
            f.write(i + '\n')

if __name__ == '__main__':
    if "--cron" in sys.argv:
        while True:
            main()
            print("[+] MixDrop.m3u updated!")
            print("[+] Next update in 8 hours")
            print("[+] Waiting...")
            time.sleep(28800)
    else:
        main()