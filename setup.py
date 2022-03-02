#In the name of GOD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import update

main_direct = ['AI', 'Config', 'Database', 'DCC1', 'GUI', 'GUI\\Temp', 'GUI\\API', 'GUI\\AuiPanel', 'GUI\\Main',
               #'Locale', 'Locale\\en', 'Locale\\fa', 'Locale\\fr', 'Locale\\gr', 'Locale\\sp', 'Locale\\tr',
               'Logs', 'Res', 'Res\\Fonts', 'Res\\Icons', 'Res\\Icons\\Menu', 'Res\\Icons\\Toolbar',
               'Res\\Icons\\16x16', 'Res\\Icons\\32x32', 'Res\\Images', 'Res\\Pics', 'Res\\Splash',
               'Src', 'Src\\API', 'Src\\AUI', 'Src\\DBF', 'Src\\DBF\\sqls', 'Src\\GUI', 'Src\\MLA', 'Src\\MLP', 'Src\\PRG',
               'Temps', 'Utility', 'Utility\\ML', 'Utility\\Pans', 'Utility\\Programs', 'Utility\\Tools', 'Utility\\UpdateApp'
               ]

main_file = {
	'AI': ['OpnSrc.py', 'Generats.py', 'DBgen.py', 'Analiz.py'],
    'Config': ['Init.py'],
    'Database': ['wxsq.py', 'PostGet2.py', 'PostGet.py', 'MenuSet2.py'],
	'DCC1': ['Proper2.py', 'MenuDev2.py', 'DBDev2.py', 'ToolBar2.py', 'ProgDev2.py', 'MLDev2.py', 'ListPro2.py', 'AuiPan2.py'],
	'GUI': ['window2.py', 'Start.py', 'proman.py', 'MainTool.py', 'MainMenu2.py', 'BG2.py'],
	'GUI\\Temp': ['untitle.py', 'Demo.py', 'Muntitle.py'],
	'GUI\\API': ['SamPnl.py'],
	'GUI\\AuiPanel': ['tempane.py', 'PAui.py'],
	'GUI\\Main': ['TPv1.py', 'TBv1.py', 'PPv1.py', 'PGv1.py', 'PAv1.py', 'MLv1.py', 'MDv1.py', 'DBv1.py'],
	'Res': ['Allicons.py'],
}

creat_file = {
	'Config': ['MLmethod.ini', 'option.ini', 'system1.ini'],
	'Database': ['Menu2.db'],
	'..': ['Mainpro.py','update.py','requirements.txt','Allimp.py']
}

def create_this(file):
	if file == 'Mainpro.py':
		pass
	if file == 'requirements.txt':
		pass
	if file == 'Allimp.py':
		pass
	if file == 'MLmethod.ini':
		pass
	if file == 'option.ini':
		pass
	if file == 'system1.ini':
		pass
	if file == 'Menu2.db':
		pass


def main():
	mydir = input("Please write directory to like install program:[sample: c:\Temp5\] >>")
	print(mydir)
	print(os.path.isdir(mydir))
	if not os.path.isdir(mydir):
		os.mkdir(mydir)

	os.chdir(mydir)
	for dir in main_direct:
		if not os.path.isdir(dir):
			os.mkdir(dir)
			if not os.path.isfile(dir+'\\'+'__init__.py'):
				with open(dir+'\\'+'__init__.py','w') as f:
					f.write('')


	for dir in main_file:
		for fil in main_file[dir]:
			if not os.path.isfile(fil):
				with open(dir+'\\'+fil,'w') as f:
					f.write('')


	update.main()


if __name__ == '__main__':
	main()