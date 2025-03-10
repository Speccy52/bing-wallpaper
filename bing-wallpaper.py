#!/usr/bin/python
import os
import requests
import subprocess
from pathlib import Path

def get_bing_wallpaper():
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    image_url = "https://www.bing.com" + data["images"][0]["url"]
    image_url = image_url.replace("1920x1080", "1366x768")  # Replace image resolution
    return image_url

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

def set_wallpaper(image_path):
    subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri", f"file://{image_path}"], check=True)

def main():
    wallpaper_dir = Path.home() / "Pictures" / "Wallpapers"
    wallpaper_dir.mkdir(parents=True, exist_ok=True)
    
    image_url = get_bing_wallpaper()
    image_path = wallpaper_dir / "bing_wallpaper.jpg"
    
    download_image(image_url, image_path)
    set_wallpaper(image_path)
    print("Обои обновлены!")

if __name__ == "__main__":
    main()
