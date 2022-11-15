def clickBtnFn(wn, args):
	btn = wn.getItem(args[0])
	btn.btnClickFn(btn.name)
	print('click: [{}]'.format(args[0]))

def getTextFn(wn, args):
	text = wn.getItem(args[0]).getValue()
	if text == '':
		text = '<empty string>'
	print('"{}" -> {}'.format(args[0], text))

def setTextFn(wn, args):
	wn.getItem(args[0]).setValue(args[1])
	print('"{}" <- {}'.format(args[0], args[1]))

def openWnFn(wn, args):
	global openWn
	openWn = True
	print('<window will open>')

cmds = {
	'clickBtn':		clickBtnFn,
	'getText':		getTextFn,
	'openWindow':	openWnFn,
	'setText':		setTextFn
}

def automate(wn, automateFilePath):
	global openWn

	openWn = False
	file = open(automateFilePath, 'r')
	lines = file.readlines()
	for line in lines:
		words = line.split()
		words = [w.replace('_', ' ') for w in words]
		if len(words) == 0 or words[0] == '#':
			continue
		lineFn = cmds[words[0]]
		lineFn(wn, words[1:])
	file.close()
	return openWn