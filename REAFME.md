## Bing Wallpaper
Python script for downloading from Bing and update wallpaper on Cinnamon desktop (and maybe on other).
Recommends **systemd** as timer to run.

### Install Notes
```bash
cp bing-wallpaper.service $(HOME)/.config/systemd/user/
cp bing-wallpaper.timer $(HOME)/.config/systemd/user/
cp bing-wallpapper.py $(HOME)/.local/bin/

systemctl --user daemon-reload
systemctl --user enable --now bing-wallpaper.timer
```
