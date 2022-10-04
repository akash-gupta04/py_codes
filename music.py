import random
import os
music_files = os.listdir('C:\\Users\\lenovo\\Desktop\\AP DHILLON')
selected_file = random.choice(music_files)
os.startfile(os.path.join('C:\\Users\\lenovo\\Desktop\\AP DHILLON'))
