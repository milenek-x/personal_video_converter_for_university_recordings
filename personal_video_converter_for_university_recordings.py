import tkinter as tk
from tkinter import filedialog
import os
import subprocess

# function to get WebM file for the audio of the merged video
def get_webm_files_audio():
    root.filename1 = filedialog.askopenfilename(initialdir="/", title="Select the webm file for the audio of the merged video", filetypes=(("WebM files", "*.webm"),))
    webm1_label.config(text=os.path.basename(root.filename1))

# function to convert WebM to MP3
def convert_to_mp3():
    subprocess.call([r'D:/ffmpeg-6.0-full_build/bin/ffmpeg.exe', '-i', root.filename1, '-vn', '-ar', '44100', '-ac', '2', '-ab', '192k', '-f', 'mp3', 'temp.mp3'])
    mp3_label.config(text="temp.mp3")

# function to get WebM files
def get_webm_files_video():
    root.filename2 = filedialog.askopenfilename(initialdir="/", title="Select the webm file for the video of the merged video", filetypes=(("WebM files", "*.webm"),))
    webm2_label.config(text=os.path.basename(root.filename2))

# function to merge files with 4K resolution and compatible codecs
def merge_files():
    output_path = filedialog.asksaveasfilename(defaultextension='.mp4', filetypes=[('MP4 files', '*.mp4')])
    output_filename = os.path.basename(output_path)
    output_dir = os.path.dirname(output_path)
    subprocess.call([r'D:/ffmpeg-6.0-full_build/bin/ffmpeg.exe', '-i', root.filename2, '-i', 'temp.mp3', '-c:v', 'copy', '-c:a', 'libmp3lame', '-map', '0:v:0', '-map', '1:a:0', '-shortest', '-s', '3840x2160', os.path.join(output_dir, output_filename)])
    os.remove('temp.mp3')


# create tkinter window
root = tk.Tk()
root.title("WebM to MP3 and Merge")

# create buttons and labels
get_webm_audio_button = tk.Button(root, text="Select the webm file for\nthe audio of the merged video", command=get_webm_files_audio)
get_webm_audio_button.pack(pady=10)

webm1_label = tk.Label(root, text="No file selected")
webm1_label.pack()

convert_button = tk.Button(root, text="Convert to MP3", command=convert_to_mp3)
convert_button.pack(pady=10)

mp3_label = tk.Label(root, text="No file selected")
mp3_label.pack()

get_webm_video_button = tk.Button(root, text="Select the webm file for\nthe video of the merged video", command=get_webm_files_video)
get_webm_video_button.pack(pady=10)

webm2_label = tk.Label(root, text="No file selected")
webm2_label.pack()

merge_button = tk.Button(root, text="Merge Files", command=merge_files)
merge_button.pack(pady=10)

root.mainloop()
