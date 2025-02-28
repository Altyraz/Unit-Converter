import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
from tkinter.filedialog import *


#global variable to store the path of the folder to save file
Folder_Name = ""


class Converter():
    def __init__(self) -> None:
        #create main window
        self.root = Tk()
        self.root.configure(background='light gray')
        self.root.title('Youtube Converter')
        self.root.geometry("500x450")


        #variable to know what format you want to download the video later
        self.variable1 = StringVar(self.root)


        #create and place some labels on the window
        lblInfo = Label(self.root, text="Copy the URL in the field below \n and Choose the file type", fg=
                        'purple', font=('Helvetica', 18), bg='light gray')
        lblInfo.grid(row=1, column=1, pady=10, padx=50)

        lblSavePath = Label(self.root, text="Choose your Location to save the file", fg='purple', font=
                            ('Helvetica', 16), bg='light gray')
        lblSavePath.grid(row=2, column=1, pady=5, padx=60)

        self.lblPath = Label(self.root, text="No path selected yet!", fg='dark red', bg='light gray', font=('Helvetica', 16))
        self.lblPath.grid(row=4, column=1, pady=5, padx=35)


        #button to get the folder where file will be saved
        self.btnPath = Button(self.root, text="Path", bg='green', fg='black', font=('Helvetica', 16), command=self.file_location)
        self.btnPath.grid(row=3, column=1, pady=10, padx=60)


        #entry to copy the url of the video
        self.entUrl = Entry(self.root, font=('Arial', 14))
        self.entUrl.grid(row=5, column=1, padx=10, pady=10, ipadx=100)

        #button to convert the url to mp3 or mp4 format and save it
        btnConvert = Button(self.root, text="Convert", fg='white', bg='gray', font=('Helvetica', 16), command=self.invalid_inputs)
        btnConvert.grid(row=7, column=1, pady=10)

        #dropdown list of the formats you can convert the video to
        self.convert_list = ["MP3", "MP4"]
        self.convert_type = ttk.OptionMenu(self.root, self.variable1, self.convert_list[0], *self.convert_list)
        self.convert_type.configure(width=20)
        self.convert_type.grid(row=6, column=1, pady=5)


        #Error Msg
        self.lblMessages = Label(self.root,text="",fg="black",bg='red', font=("jost",18))


        #setting some keybinds to the script and call the mainloop
        self.root.bind('<Return>', self.converting)
        self.entUrl.focus_set()
        self.root.bind('<Escape>', exit)
        self.root.mainloop()


    def invalid_inputs(self):
        #making sure path and url are there, if not, there will be a warning to do it first
        if not Folder_Name:
            self.btnPath.configure(bg='red')
            self.lblMessages.configure(text="Enter path to save your file")
            self.lblMessages.grid(column=1, padx=15)
            return
        if "https://www.youtube.com/watch" not in self.entUrl.get():
            self.lblMessages.configure(text="Enter the correct URL to your video")
            self.entUrl.configure(bg='red')
            self.lblMessages.grid(column=1, padx=15)
            return
        #if an error ocurred and error message is displayed, when all required data is there
        #remove the message from window and change background of entry to white again
        self.clear_error_messages()
        self.convert_url()


    def clear_error_messages(self):
        self.lblMessages.grid_forget()
        self.entUrl.configure(bg='white')

    def converting(self, event):
        self.invalid_inputs()


    #function called from the button to call the corresponding function that matches the variable1
    def convert_url(self):
        #create youtube object and set quality to highest resolution
        youtubeObject = YouTube(self.entUrl.get())
        video = youtubeObject.streams.get_highest_resolution()
        #download video in mp4 format to selected folder
        video.download(Folder_Name)

        #if mp3 format is selected, mp4 file will be converted to mp3 file
        #and the mp4 file will be deleted
        if self.variable1.get() == "MP3":
            file_name = (Folder_Name + "/" + video.title)
            videoclip = VideoFileClip(file_name + ".mp4")
            audioclip = videoclip.audio
            audioclip.write_audiofile(file_name + ".mp3")

            audioclip.close()
            videoclip.close()

            os.remove(file_name + ".mp4")

        self.lblMessages.configure(bg='green', text='Success! \n You can download a new Video')
        self.lblMessages.grid(column=1, padx=15)
        self.entUrl.delete(0, END)

    #ask for the folder to save in the global variable Folder_Name
    #and if path is set a label will show on the screen with the path selected
    def file_location(self):
        global Folder_Name
        Folder_Name = filedialog.askdirectory()
        #if (len(Folder_Name) > 1):
        self.lblPath.configure(text=Folder_Name, fg='green')
        self.btnPath.configure(bg='green')


if __name__ == '__main__':
    Converter()

