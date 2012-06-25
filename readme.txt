ftpup.py

[概要]
・指定されたディレクトリ以下を7zip圧縮してFTPで転送するスクリプトです。

[動作環境]
・pythonがインストールされているマシンで動作します。

[使用方法]
1.Copy_usenetworkdrive.batを任意のディレクトリにコピーしてください。
2.定義部分を修正して実行してください。
2.1._FROMPATH = '/xxxx/xxxx/Share/from/'
　転送したいファイルのあるディレクトリを指定してください。
2.2._TOPATH = '/xxxx/xxxx/Share/to/'
　圧縮したファイルを置く一時ディレクトリを指定してください。
2.3._ZIPFILENAME = 'AutoFTP' + time.strftime('%Y.%m.%d.%H.%M.%S') + '.7z'
　圧縮ファイル名を指定してください。
2.4._7ZaPATH = '/usr/local/bin/7za'
　7zaのPATHを指定してください。
2.5._FTP_SERVER = '******'
　FTPサーバを指定してください。
2.6._FTP_ID = '******'
　FTPサーバのログインIDを指定してください。
2.7._FTP_PW = '******'
　FTPサーバのログインパスワードを指定してください。
2.8._FTP_DEFAULT_DIR = '/xxxx/xxxx/'
　FTPサーバ上のファイルを置きたいPATHを指定してください。
