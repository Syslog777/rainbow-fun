def bluegreen():
	print " - Just Copy & Paste The Generated Messages - \n"
	colors = ["#0d38c0","#460eea","#a60ee9","#e80ecb",'#e70e6a','#e6110e','#e5700e','#e4ce0e','#9ae30e','#3ce20e','#0de13c']
	s = 0
	new = ""
	msgb = ""
	while 1:
		msg = raw_input("Message: ").decode('utf8')
		if len(msg) >= 48:
			msgb = msg[48:]
			msg = msg[:48]
		msg = list(msg)
		for _ in msg:
			if s == len(colors):
				s = 0
			if _ == "":
				new = new + ""
				s = s - 1
			else:
				new = new + colors[s].replace("#","[") + "]" + _
			s = s + 1
		print "[c][b][i]" + new + msgb + "\n"
		new = ""
		msgb = ""
		s = 0
bluegreen()