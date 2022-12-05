from tkinter import *
import speedtest

janela = Tk()
janela.title("Internet Speed Test")
janela.geometry("360x600")
janela.resizable(False, False)
janela.config(bg="#1a212d")

def Check():

    test = speedtest.Speedtest()

    Uploading = round(test.upload()/(1024*1024), 2)
    upload.config(text=Uploading)

    downloading = round(test.download()/(1024*1024), 2)
    download.config(text=downloading)
    Download.config(text=downloading)

    servernames = []
    test.get_servers(servernames)
    ping.config(text=test.results.ping)

    
# icon
img_icon = PhotoImage(file="logo.png")
janela.iconphoto(False, img_icon)

# imagens
top = PhotoImage(file='top.png')
Label(janela, image=top, bg="#1a212d").pack()

main = PhotoImage(file='main.png')
Label(janela, image=main, bg="#1a212d").pack(pady=(40, 0))

button = PhotoImage(file='button.png')
Button = Button(janela, image=button, bg="#1a212d", bd=0, activebackground="#1a212d", cursor='hand2', command=Check)
Button.pack(pady=10)

# Label
Label(janela, text="PING", font="arial 10 bold", bg="#384056").place(x=50, y=0)
Label(janela, text="DOWNLOAD", font="arial 10 bold", bg="#384056").place(x=140, y=0)
Label(janela, text="UPLOAD", font="arial 10 bold", bg="#384056").place(x=260, y=0)

Label(janela, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=60, y=80)
Label(janela, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=165, y=80)
Label(janela, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=275, y=80)

Label(janela, text="Download", font="arial 15 bold", bg='#384056', fg="white").place(x=140, y=280)
Label(janela, text="MBPS", font="arial 15 bold", bg='#384056', fg="white").place(x=155, y=380)

ping = Label(janela, text='00', font="arial 13 bold", bg="#384056", fg="white")
ping.place(x=70, y=60, anchor="center")

download = Label(janela, text='00', font="arial 13 bold", bg="#384056", fg="white")
download.place(x=180, y=60, anchor="center")

upload = Label(janela, text='00', font="arial 13 bold", bg="#384056", fg="white")
upload.place(x=290, y=60, anchor="center")

Download = Label(janela, text='00', font="arial 40 bold", bg="#384056")
Download.place(x=185, y=350, anchor="center")




janela.mainloop()


