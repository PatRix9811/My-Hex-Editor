from tkinter import filedialog as fd

class File:
	filename =""
	file=""
	asciDump=""
	hexPart=""
	offset=""
	saveFile=""
	
	def reset(self):
		self.asciDump=""
		self.hexPart=""
		self.offset=""
		
		
	def set_offset(self,o):
		self.offset+=str(o*14)


	def toHex(self,file):
		i=0
		o=0
		for x in file:
			if x >=0x20 and x <=0x7e:
				self.asciDump+=chr(x)
				self.hexPart+=hex(x)
				self.hexPart+=" "
			else:
				self.asciDump+="."
				self.hexPart+=hex(x)
				self.hexPart+=" "
			i+=1
			
			if i==14:
				self.hexPart+="\n"
				self.asciDump+="\n"
				self.set_offset(o)
				self.offset+="\n"
				o+=1
				i=0
				
		self.set_offset(o)

	def fileOpen(self):
		self.reset()
		self.filename = fd.askopenfilename(filetypes=[("Wszystkie pliki","*.*"),("Plik tekstowy","*.txt"),("Plik Pythona","*.py")])
		if self.filename:
			try:
				self.file = bytearray(open(self.filename,"rb").read())
			except:
				print("[!] File not found")
				
			self.toHex(self.file)
			
	def getAscii(self):
		return self.asciDump
	
	def getOffset(self):
		return self.offset
		
	def getHex(self):
		return self.hexPart
		
	def fileSave(self,flag=False):
		if flag == True:
			self.filename = fd.asksaveasfilename(filetypes=[("Wszystkie pliki","*.*")])
		try:
			self.saveFile = open(self.filename,"wb")
			self.saveFile.write(self.file)
			self.saveFile.close()
		except:
			print("[!] Save Error")
			
	def fileEdit(self,content):
		content = content[:-1]
		i=0
		for x in content:
			content[i]=x.strip("\n")
			i+=1
							
		self.reset()
		i=0
		l=len(content)
		while i <l:
			content[i]=int(content[i],16)
			i+=1
			
		content = bytearray(content)
		i=0
		while i<l:
			self.file[i] = content[i]
			i+=1
				
		self.toHex(self.file)