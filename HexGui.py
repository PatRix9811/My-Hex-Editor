import tkinter,sys
import file

def wheel(event):
	offset.yview_scroll(int(-3*(event.delta/120)), "units")
	hexPart.yview_scroll(int(-1*(event.delta/120)), "units")
	asciDump.yview_scroll(int(-3*(event.delta/120)), "units")
	
def load():
	plik.fileOpen()
	ref()
	
def save():
	plik.fileSave()
	
def save1():
	plik.fileSave(flag=True)
	
def ref():
	offset.config(state="normal")
	asciDump.config(state="normal")
	
	offset.delete('0.0','end')
	hexPart.delete('0.0','end')
	asciDump.delete('0.0','end')
	
	offset.insert("0.0",plik.getOffset())
	hexPart.insert("0.0",plik.getHex())
	asciDump.insert("0.0",plik.getAscii())
	
	offset.config(state="disabled")
	asciDump.config(state="disabled")
	
def edit():
	content=hexPart.get('0.0','end')
	if len(content)>0:
		plik.fileEdit(content.split(' '))
	ref()


window=tkinter.Tk()
window.title("My Hex Editor")
window.bind("<MouseWheel>",wheel)

plik = file.File()

#kontrloki menu
menubar = tkinter.Menu(window)
menuItem = tkinter.Menu(menubar,tearoff=0)
menuItem.add_command(label="Open",command=load)
menuItem.add_command(label="Save",command=save)
menuItem.add_command(label="Save file as",command=save1)
menuItem.add_command(label="Exit",command=sys.exit)
menubar.add_cascade(label="File",menu=menuItem)
menubar.add_command(label="Change",command=edit)

hexPart=tkinter.Text(window,width=70,height=30)
offset=tkinter.Text(window,width=5,height=30,bg="#cccccc")
asciDump=tkinter.Text(window,width=30,height=30,bg="#cccccc")

offset.grid(row=0,column=0,sticky="ns")
hexPart.grid(row=0,column=1,sticky="nwse")
asciDump.grid(row=0,column=2,sticky="nwse")
window.config(menu=menubar)

window.mainloop()
