import json

class Movefiles:

    base_video_path = ""    
    base_music_path = ""

    def __init__(self):

        try:
            if not self.base_music_path:
                path_music = input("Enter music path: ")

                with open('details.json', "r") as file:
                    loaded_data = json.load(file) 
                loaded_data['music_path'] = path_music

            if not self.base_video_path: 
                path_video = input("Enter video path: ")
                with open('details.json', "r") as file:
                    loaded_data['video_path'] = path_video
        except KeyError:
            self.base_music_path = ""
            self.base_music_path = ""
    
    def move_files(self):
        print(self.base_music_path)
        print(self.base_video_path)


