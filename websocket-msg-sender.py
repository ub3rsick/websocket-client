#!/usr/bin/env python

__author__ = 'Rizal'
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Separator
try:
	from websocket import create_connection, WebSocketTimeoutException, WebSocketException
except:
	print "[-] Module websocket missing!"
	print "[*] pip install websocket-client"

class WebSocketClass:
    def __init__(self, master):
	
        self.label = Label(master, text="WEBSOCKET:", fg="#ED3276")
        self.label.grid(row=2, sticky=W, padx=5)
        
		self.label = Label(master, text="DATA-TO-WS:", fg="#ED3276")
        self.label.grid(row=3, sticky=W, padx=5)

        self.ws_addr = Entry(master, width="128")
        self.ws_addr.grid(row=2, column=1, padx=5)
        # add mouse click event to the Websocket entry field
        #self.ws_addr.bind('<Button-1>', lambda event: self.ws_addr.delete(0, END))

		self.ws_data = Entry(master, width="128")
        self.ws_data.grid(row=3, column=1, padx=5)
        # add mouse click event to the Websocket data entry field
        #self.ws_data.bind('<Button-1>', lambda event: self.ws_data.delete(0, END))

        self.button = Button(master, text="SendData", command=self.send_to_ws)
        self.button.grid(row=6, column=1, padx=5, pady=3)
        
		self.abtbutton = Button(master, text="About", command= lambda: messagebox.showinfo('ABOUT', 'SIMPLE WEBSOCKET CLIENT\nDEV:RIZAL~AKA~UB3RSiCK'))
        self.abtbutton.grid(row=6, padx=5, pady=3)

		self.button_wsad_cl = Button(master, text="X", command= lambda: self.ws_addr.delete(0, END))
		self.button_wsad_cl.grid(row=2, column=2, padx=2, pady=3)

		self.button_wsdat_cl = Button(master, text="X", command= lambda: self.ws_data.delete(0, END))
		self.button_wsdat_cl.grid(row=3, column=2, padx=2)	

        self.sep = Separator(master, orient=HORIZONTAL)
        self.sep.grid(row=4, sticky='we', columnspan=2, pady=5, padx=5)

        self.l_ws_resp = Label(master, text="RESPONSE\nFROM\nWEBSOCKET:", fg="#ED3276")
		self.ws_resp = Text(master, height=15, width="146")

        self.l_ws_resp.grid(row=5, sticky=W, padx=5)
        self.ws_resp.grid(row=5, column=1)


    def clear_resp_feild(self):
        self.ws_resp.delete(1.0, END)

    def send_to_ws(self):
	
		# Clear response feild
		self.clear_resp_feild()
		
		ws_address = self.ws_addr.get()
		if not len(ws_address) == 0:
			
			# Websocket address is present
			
			# is there any data?
			
			data_to_ws = self.ws_data.get()
			if not len(data_to_ws) == 0:
				# data to websocket is present.
				# is the websocket valid?
				try:
					wsock = create_connection(ws_address)
			
				# TODO: Handle different exceptions
				except WebSocketTimeoutException:
					messagebox.showinfo('EXCEPTION', WebSocketTimeoutException)
					#print "[-] Not a valid WEBSOCKET address"
					return
				except WebSocketException:
					messagebox.showinfo('EXCEPTION', WebSocketException)
					#print "[-] Not a valid WEBSOCKET address"
					return	
				except:
					messagebox.showinfo('EXCEPTION', '[-] Invalid WEBSOCKET address!')
					return	

				# We Have a valid Websocket in hand.
				# Send data to ws.

				print data_to_ws
				wsock.send(data_to_ws)
				res = wsock.recv()
				print "[+] Received {} bytes.".format(len(res))
				self.ws_resp.insert(END, res)
				
			else:
				print "[-] Provide data to websocket"
				messagebox.showinfo('WARNING', '[-] Provide data to websocket')	
			
		else:
			print "[-] No WebSocket address specified"
			messagebox.showinfo('WARNING', '[-] No WebSocket address specified')
		

if __name__ == "__main__":
    mainWindow = Tk()
    ws_obj = WebSocketClass(mainWindow)
    mainWindow.resizable(width=FALSE, height=FALSE)

    #img = PhotoImage(file='icon.png')
    #mainWindow.tk.call('wm', 'iconphoto', mainWindow._w, img)
    mainWindow.title("WebSocket Client")
    mainWindow.mainloop()



