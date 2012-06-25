#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import glob
import string
import os
import time
import shutil
from ftplib import FTP
from urllib import urlopen

##こっちの情報
_FROMPATH = '/xxxx/xxxx/Share/from/'
_TOPATH = '/xxxx/xxxx/Share/to/'
_ZIPFILENAME = 'AutoFTP' + time.strftime('%Y.%m.%d.%H.%M.%S') + '.7z'
_7ZaPATH = '/usr/local/bin/7za'

##あっちの情報
_FTP_SERVER = '******'
_FTP_ID = '******'
_FTP_PW = '******'
_FTP_DEFAULT_DIR = '/xxxx/xxxx/'

##古い圧縮ファイルを消す
cmd = "rm -rf " + _TOPATH + "*"
print cmd
#subprocess.call(cmd, shell=True)
os.system(cmd)

##圧縮
ignorelist = ['.7z', '.rar', '.zip', '.gz', '.z' '.tar']
for file in os.listdir(_FROMPATH):
	#cmd = _7ZaPATH + " a -t7z " + _TOPATH + _ZIPFILENAME + " " + _FROMPATH + "'" + file + "'"
	filename, ext = os.path.splitext(file)
	if (ext.lower() not in ignorelist):
		cmd = _7ZaPATH + " a -t7z " + _TOPATH + "'" + file + "'" + ".7z " + _FROMPATH + "'" + file + "'"
		print u'圧縮します'
		print cmd
		#subprocess.call(cmd, shell=True)
		os.system(cmd)
		print u'圧縮しました'
	else:
		shutil.move(_FROMPATH + file, _TOPATH)

##FTPする
path = _TOPATH

#filelist = glob.glob(_TOPATH + "*.7z")
filelist = glob.glob(_TOPATH + "*")
print filelist

if (len(filelist) > 0):
	ftp=FTP(_FTP_SERVER)
	ftp.login(_FTP_ID, _FTP_PW)
	ftp.cwd(_FTP_DEFAULT_DIR)
	for file in ftp.nlst():
		if(file == _ZIPFILENAME):
			ftp.delete(file)
			print file + ' is deleted'
	for file in filelist:
		filename=os.path.basename(file)
		f=open(os.path.join(path, filename),'r')
		cmd='STOR ' + filename
		print cmd
		ftp.storbinary(cmd, f)
		f.close()
	ftp.quit()

##送信したらローカルのファイルを消す
cmd = "rm -rf " + _FROMPATH + "*"
print cmd
#subprocess.call(cmd, shell=True)
os.system(cmd)

print 'finish'
