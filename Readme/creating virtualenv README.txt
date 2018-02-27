root@kali:~# cd Desktop
root@kali:~/Desktop# mkdir flasksite
root@kali:~/Desktop# cd flasksite
root@kali:~/Desktop/flasksite# virtualenv env
Using base prefix '/usr'
New python executable in /root/Desktop/flasksite/env/bin/python3
Also creating executable in /root/Desktop/flasksite/env/bin/python
Installing setuptools, pip, wheel...done.
root@kali:~/Desktop/flasksite# dir
env
root@kali:~/Desktop/flasksite# cd env
root@kali:~/Desktop/flasksite/env# dir
bin  include  lib  pip-selfcheck.json
root@kali:~/Desktop/flasksite/env# cd bin
root@kali:~/Desktop/flasksite/env/bin# dir
activate       activate_this.py  pip	 python     python-config
activate.csh   easy_install	 pip3	 python3    wheel
activate.fish  easy_install-3.6  pip3.6  python3.6
root@kali:~/Desktop/flasksite/env/bin# activate
bash: activate: command not found
root@kali:~/Desktop/flasksite/env/bin# ./activate
bash: ./activate: Permission denied
root@kali:~/Desktop/flasksite/env/bin# source ./activate
(env) root@kali:~/Desktop/flasksite/env/bin# cd..
bash: cd..: command not found
(env) root@kali:~/Desktop/flasksite/env/bin# cd ..
(env) root@kali:~/Desktop/flasksite/env# cd ..
(env) root@kali:~/Desktop/flasksite# pip3 install flask
Collecting flask
  Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 128kB/s 
Collecting click>=2.0 (from flask)
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 257kB/s 
Collecting itsdangerous>=0.21 (from flask)
  Downloading itsdangerous-0.24.tar.gz (46kB)
    100% |████████████████████████████████| 51kB 371kB/s 
Collecting Werkzeug>=0.7 (from flask)
  Downloading Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
    100% |████████████████████████████████| 327kB 283kB/s 
Collecting Jinja2>=2.4 (from flask)
  Downloading Jinja2-2.10-py2.py3-none-any.whl (126kB)
    100% |████████████████████████████████| 133kB 281kB/s 
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
  Downloading MarkupSafe-1.0.tar.gz
Building wheels for collected packages: itsdangerous, MarkupSafe
  Running setup.py bdist_wheel for itsdangerous ... done
  Stored in directory: /root/.cache/pip/wheels/fc/a8/66/24d655233c757e178d45dea2de22a04c6d92766abfb741129a
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: /root/.cache/pip/wheels/88/a7/30/e39a54a87bcbe25308fa3ca64e8ddc75d9b3e5afa21ee32d57
Successfully built itsdangerous MarkupSafe
Installing collected packages: click, itsdangerous, Werkzeug, MarkupSafe, Jinja2, flask
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-0.12.2 itsdangerous-0.24
(env) root@kali:~/Desktop/flasksite# python from flask import Flask
python: can't open file 'from': [Errno 2] No such file or directory
(env) root@kali:~/Desktop/flasksite# python3
Python 3.6.3 (default, Oct  3 2017, 21:16:13) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask import Flask
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
[1]+  Stopped                 python3
(env) root@kali:~/Desktop/flasksite# mkdir static
(env) root@kali:~/Desktop/flasksite# mkdir templates
(env) root@kali:~/Desktop/flasksite# cd static
(env) root@kali:~/Desktop/flasksite/static# mkdir css
(env) root@kali:~/Desktop/flasksite/static# mkdir js
(env) root@kali:~/Desktop/flasksite/static# mkdir images
(env) root@kali:~/Desktop/flasksite/static# cd ..
(env) root@kali:~/Desktop/flasksite# 

