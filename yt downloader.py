#yt-video-downloader is a GUI based Video downloader dor YouTube

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program. If not, see {http://www.gnu.org/licenses/}.

import tkinter as tk
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox, filedialog


def Widgets():

	head_label = Label(root, text="YouTube Video Downloader",
					padx=12,
					pady=12,
					font="SegoeUI 14",
					bg="black",
					fg="white")
	head_label.grid(row=1,
					column=1,
					pady=1,
					padx=1,
					columnspan=2)

	link_label = Label(root,
					text="YouTube link :",
					bg="white",
					pady=5,
					padx=8)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=36,
						textvariable=video_Link,
						font="Arial 15")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


	destination_label = Label(root,
							text="Location :",
							bg="white",
							pady=5,
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="Arial 15")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="white",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_V = Button(root,
						text="Download Video",
						command=Download,
						width=20,
						bg="WHITE",
						font="Georgia, 13")
	Download_V.grid(row=4,
					column=1,
					pady=20,
					padx=20)


def Browse():
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")

	download_Path.set(download_Directory)

def Download():
    
	Youtube_link = video_Link.get()
	download_Folder = download_Path.get()
	getVideo = YouTube(Youtube_link)
	videoStream = getVideo.streams.get_highest_resolution()
	videoStream.download(download_Folder)

	messagebox.showinfo("SUCCESSFULLY",
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder)

root = tk.Tk()

root.geometry("520x220")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="black")

video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()