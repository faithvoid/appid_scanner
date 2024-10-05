import os
import requests

def get_steam_game_name(app_id):
    try:
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
        response = requests.get(url)
        data = response.json()
        
        if data[str(app_id)]['success']:
            return data[str(app_id)]['data']['name']
        else:
            return None
    except Exception as e:
        print(f"Error retrieving game name for app ID {app_id}: {e}")
        return None

def scan_directory_for_app_ids(directory):
    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    # List all subfolders in the directory
    subfolders = [f.name for f in os.scandir(directory) if f.is_dir()]

    print(f"Scanning directory: {directory}")
    
    for folder in subfolders:
        if folder.isdigit():
            app_id = int(folder)
            game_name = get_steam_game_name(app_id)
            if game_name:
                print(f"{app_id} - {game_name}")
            else:
                print(f"{app_id} - N/A")

if __name__ == "__main__":
    directory = input("Please enter the directory to scan: ")
    scan_directory_for_app_ids(directory)
