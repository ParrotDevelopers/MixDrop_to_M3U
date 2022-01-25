### Legal
- I am not associated with mixdrop.co/.bz/... in any way. I just make grabber from source code of page which is directly avalible by just pressing ```CTRL + U```.

### About
- This grabber takes links from mixdrop and puts them into m3u.
- I will make server version soon.
- MixDrop links are IP-Locked.

### Installation / Running
##### Run these commands to clone repository:
```bash
https://github.com/ParrotDevelopers/MixDrop_to_M3U.git
```
and 
``` bash
cd MixDrop_to_M3U
```
##### To install required  dependencies:
```bash
python3 -m pip install -r requirements.txt
```
or 
```bash
pip3 install -r requirements.txt
```
##### Running script:
To run in normal mode:
```bash
python3 main.py
```
To run in cron mode:
```bash
python3 main.py --cron
```
### Editing:
- To set custom output file name open main.py and edit MixDrop.m3u to any filename.
- To set your own delay between cron jobs open main.py and edit time.sleep(28800) to any time you want.
