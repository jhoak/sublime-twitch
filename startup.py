# Ideas list
# - be able to change streams at any time w/ hotkey/button/whatever
# - toggle webcam (prompt though)
# - handle stream ending / re-prompt
# - handle internet ending / re-prompt
# - toggle chat
# - chat fcn'ality
# - chat/video size
# - reposition minimap?
# - handle text getting under chat sidebar
# - decide on sidebar vs overlay (if that's even a choice)
# - window spawn @ center of screen

from tkinter import *

def connect(streamer_name, login_name, passwd):
	"""Connects user to a Twitch stream."""
	#if stream:
		# ... Try to get the stream view/chat, show if ok(?) and return
		# ... also incorporate login
	# ... if we messed up then show a dialog saying we couldn't connect.
	pass

# Main window initialization
basewindow = Tk()
basewindow.title("Twitch Plugin Options")
basewindow.geometry('360x210')
basewindow.resizable(width=False, height=False)

# Now for frames
topf, checkf, botf = (Frame(basewindow) for i in range(3))

# Build top frame (stream name, username, password (latter 2 optional))
Label(topf, text='Streamer to watch (required):', anchor=E).grid(row=0, column=0, pady=10)
Label(topf, text='Login name (optional):', anchor=E).grid(row=1, column=0, pady=10)
Label(topf, text='Password (if logging in):', anchor=E).grid(row=2, column=0, pady=10)

entries = (Entry(topf) if i != 2 else Entry(topf, show='*') for i in range(3))
stream_name_field, username_field, passwd_field = entries
stream_name_field.grid(row=0, column=1)
username_field.grid(row=1, column=1)
passwd_field.grid(row=2, column=1)
topf.pack(side=TOP)

# Build checkbox frame
webcam_check, box_text = IntVar(), '(If streaming) Show webcam view'
Checkbutton(checkf, text=box_text, variable=webcam_check).pack()
checkf.pack(pady=10)

# Build bottom
def try_ok():
	"""Tries to connect w/ given info (passes it to connect())"""
	pass
	
botf_left, botf_right = (Frame(botf) for i in range(2))
Button(botf_left, text='OK', width=10, command=try_ok).pack()
botf_left.grid(row=0, column=0, pady=0, padx=10)
Button(botf_right, text='Cancel', width=10, command=quit).pack()
botf_right.grid(row=0, column=1, pady=0, padx=10)
botf.pack()

# Run!
basewindow.mainloop()