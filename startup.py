from tkinter import *
basewindow = Tk()
basewindow.resizable(width=False, height=False)
basewindow.geometry('360x180')
basewindow.title("Twitch Plugin Options")
topf, midf, botf = (Frame(basewindow) for i in range(3))
# Build top
Label(topf, text='Stream to view: ').grid(row=0,column=0,pady=35)
stream_name_field = Entry(topf)
stream_name_field.grid(row=0,column=1)
topf.pack(side=TOP)
# Build mid
webcam_check, box_text = IntVar(), '(If streaming) Show webcam view'
Checkbutton(midf, text=box_text, variable=webcam_check).pack()
midf.pack()
# Build bottom
def try_ok():
	stream = stream_name_field.get()
	#if stream:
		# ... Try to get the stream view/chat, show if ok(?) and return
	# ... if we messed up then show a dialog saying we couldn't connect.
botf_left, botf_right = (Frame(botf) for i in range(2))
Button(botf_left, text='OK', width=10, command=try_ok).pack()
Button(botf_right, text='Cancel', width=10, command=quit).pack()
botf_left.grid(row=0,column=0,pady=20, padx = 10)
botf_right.grid(row=0,column=1,pady=20, padx = 10)
botf.pack()
basewindow.mainloop()