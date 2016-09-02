from tkinter import *
basewindow = Tk()
basewindow.title("Twitch Plugin Options")
basewindow.geometry('360x200')
basewindow.resizable(width=False, height=False)
topf, namef, passf, checkf, botf = (Frame(basewindow) for i in range(5))
# Build top
Label(topf, text='Name of streamer to watch (required):', anchor=E).grid(row=0, column=0, pady=10)
Label(topf, text='Login name (optional):', anchor=E).grid(row=1, column=0, pady=10)
Label(topf, text='Password (if logging in):', anchor=E).grid(row=2, column=0, pady=10)
stream_name_field = Entry(topf)
stream_name_field.grid(row=0, column=1)
username_field = Entry(topf)
username_field.grid(row=1, column=1)
passwd_field = Entry(topf)
passwd_field.grid(row=2, column=1)
topf.pack(side=TOP)
# Build name, password frames
#username_field = make_textframe(namef, 'Login name (optional): ')
#passwd_field = make_textframe(passf, 'Password (only if logging in): ')
# Build checkbox frame
webcam_check, box_text = IntVar(), '(If streaming) Show webcam view'
Checkbutton(checkf, text=box_text, variable=webcam_check).pack()
checkf.pack(pady=10)
# Build bottom
def try_ok():
	stream = stream_name_field.get()
	#if stream:
		# ... Try to get the stream view/chat, show if ok(?) and return
	# ... if we messed up then show a dialog saying we couldn't connect.
botf_left, botf_right = (Frame(botf) for i in range(2))
Button(botf_left, text='OK', width=10, command=try_ok).pack()
Button(botf_right, text='Cancel', width=10, command=quit).pack()
botf_left.grid(row=0, column=0, pady=0, padx=10)
botf_right.grid(row=0, column=1, pady=0, padx=10)
botf.pack()
basewindow.mainloop()