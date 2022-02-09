import os


files = os.listdir()
files.remove("clearClutter.py")


#making folders
def make (folders):
    if not os.path.exists(folders):
        os.makedirs(folders)

#moving files to folders
def move (files,foldername):
    for file in files:
        os.replace(file, f"{foldername}/{file}")
        

make("Images")

make("Documents")

make("Videos")

make("Music")

make("Others")


#extracting extension from file name
img_ext = [".jpg",".png",".jpeg",".gif"]
images = [file for file in files if os.path.splitext(file)[1].lower() in img_ext]

doc_ext = [".txt",".docx",".pdf",".pptx",".doc"]
documents = [file for file in files if os.path.splitext(file)[1].lower() in doc_ext]

vid_ext = [".avi",".mp4"]
videos = [file for file in files if os.path.splitext(file)[1].lower() in vid_ext]

msc_ext = [".mp3"]
music = [file for file in files if os.path.splitext(file)[1].lower() in msc_ext]


others = []
for file in files:
    ext = os.path.splitext(file)[1].lower() 
    if (ext not in img_ext) and (ext not in doc_ext) and (ext not in vid_ext) and (ext not in msc_ext) and os.path.isfile(file):
        others.append(file)



move(images,"Images")

move(documents,"Documents")

move(videos,"Videos")

move(music,"Music")

move(others,"Others")
   