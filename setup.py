#! /usr/bin/python
from distutils.core import setup
from glob import glob
import py2exe

# to install type:
# python setup.py install --root=/

setup (name='SalamScout Softwares', version='0.5',
      description='SalamScout Softwares',
      author='Taha Zerrouki',
      author_email='taha_zerrouki@gawab.com',
      url='http://www.bouirascout.net/',
      license='GPL',
	 console = [
        {
            "script": "scoutgameconsole.py",
            "icon_resources": [(1, "images/sma.ico")]
        }
    ],
	 windows = [
        {
            "script": "main_gui.py",
            "icon_resources": [(1, "images/sma.ico")]
        }
    ],

      #scripts=['Qutrub'],
      classifiers=[
          'Development Status :: 5 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ],
      data_files=[
	  #('images',['f:\gui/qutrub/libqutrub/images/save.png']),
	  ('images',[
	  './images/logo.png','./images/sma.ico',]),
	  ('images/codepoint',
	  [
'./images/codepoint/cpicon.png',   './images/codepoint/heh.png',   './images/codepoint/noun.png',   './images/codepoint/teh.png',
'./images/codepoint/dad.png',   './images/codepoint/qaf.png',   './images/codepoint/theh.png',   './images/codepoint/ain.png',   './images/codepoint/del.png',   './images/codepoint/jim.png',   './images/codepoint/reh.png',   './images/codepoint/waw.png',   
'./images/codepoint/alif.png',   './images/codepoint/dhel.png',   './images/codepoint/kaf.png',   './images/codepoint/sad.png',   './images/codepoint/word.png',   './images/codepoint/beh.png',   './images/codepoint/feh.png',   './images/codepoint/khah.png',   './images/codepoint/shin.png',   './images/codepoint/yeh.png',  
'./images/codepoint/cp.png',   './images/codepoint/ghain.png',   './images/codepoint/lam.png',   './images/codepoint/sin.png',   './images/codepoint/zah.png',   './images/codepoint/cpanim.png',   './images/codepoint/hah.png',   './images/codepoint/meem.png',   './images/codepoint/tah.png',   './images/codepoint/zey.png',
]),
('images/codepoint/imagesquiz',[
# codepoint images quiz
   './images/codepoint/imagesquiz/heh.png',   './images/codepoint/imagesquiz/noun.png',   './images/codepoint/imagesquiz/teh.png',
'./images/codepoint/imagesquiz/dad.png',   './images/codepoint/imagesquiz/qaf.png',   './images/codepoint/imagesquiz/theh.png',   './images/codepoint/imagesquiz/ain.png',   './images/codepoint/imagesquiz/del.png',   './images/codepoint/imagesquiz/jim.png',   './images/codepoint/imagesquiz/reh.png',   './images/codepoint/imagesquiz/waw.png',   
'./images/codepoint/imagesquiz/alif.png',   './images/codepoint/imagesquiz/dhel.png',   './images/codepoint/imagesquiz/kaf.png',   './images/codepoint/imagesquiz/sad.png',   './images/codepoint/imagesquiz/word.png',   './images/codepoint/imagesquiz/beh.png',   './images/codepoint/imagesquiz/feh.png',   './images/codepoint/imagesquiz/khah.png',   './images/codepoint/imagesquiz/shin.png',   './images/codepoint/imagesquiz/yeh.png',  
   './images/codepoint/imagesquiz/ghain.png',   './images/codepoint/imagesquiz/lam.png',   './images/codepoint/imagesquiz/sin.png',   './images/codepoint/imagesquiz/zah.png',      './images/codepoint/imagesquiz/hah.png',   './images/codepoint/imagesquiz/meem.png',   './images/codepoint/imagesquiz/tah.png',   './images/codepoint/imagesquiz/zey.png',
]),
('images/semaphore',[
   #Semaphore images
	'./images/semaphore/FEH.png',	'./images/semaphore/LAM.png',	'./images/semaphore/semflag.png'	,'./images/semaphore/welcome.png',
	'./images/semaphore/GHAIN.png',	'./images/semaphore/learn.png',	'./images/semaphore/SHIN.png',	'./images/semaphore/word.png',
	'./images/semaphore/AIN.png',	'./images/semaphore/HAH.png',	'./images/semaphore/MEEM.png',	'./images/semaphore/SIN.png',	'./images/semaphore/write.png',
	'./images/semaphore/ALIF.png',	'./images/semaphore/HEH.png',	'./images/semaphore/NOUN.png',	'./images/semaphore/START.png',	'./images/semaphore/YEH.png',
	'./images/semaphore/BEH.png',	'./images/semaphore/play.png',	'./images/semaphore/TAH.png',	'./images/semaphore/ZAH.png',
	'./images/semaphore/DAD.png',	'./images/semaphore/JIM.png',	'./images/semaphore/QAF.png',	'./images/semaphore/TEH.png',	'./images/semaphore/ZEY.png',
	'./images/semaphore/DEL.png',	'./images/semaphore/KAF.png',	'./images/semaphore/REH.png',	'./images/semaphore/THEH.png',     
	'./images/semaphore/DHEL.png',	'./images/semaphore/KHAH.png',	'./images/semaphore/SAD.png',	'./images/semaphore/WAW.png',       
]),
('images/semaphore/imagesquiz',[
	#Semaphore images quiz
  	'./images/semaphore/imagesquiz/FEH.png',	'./images/semaphore/imagesquiz/LAM.png',	'./images/semaphore/imagesquiz/semflag.jpg',
	'./images/semaphore/imagesquiz/GHAIN.png',	'./images/semaphore/imagesquiz/SHIN.png',	'./images/semaphore/imagesquiz/word.png',
	'./images/semaphore/imagesquiz/AIN.png',	'./images/semaphore/imagesquiz/HAH.png',	'./images/semaphore/imagesquiz/MEEM.png',	'./images/semaphore/imagesquiz/SIN.png',
	'./images/semaphore/imagesquiz/ALIF.png',	'./images/semaphore/imagesquiz/HEH.png',	'./images/semaphore/imagesquiz/NOUN.png',	'./images/semaphore/imagesquiz/YEH.png',
	'./images/semaphore/imagesquiz/BEH.png',	'./images/semaphore/imagesquiz/TAH.png',	'./images/semaphore/imagesquiz/ZAH.png',
	'./images/semaphore/imagesquiz/DAD.png',	'./images/semaphore/imagesquiz/JIM.png',	'./images/semaphore/imagesquiz/QAF.png',	'./images/semaphore/imagesquiz/TEH.png',	'./images/semaphore/imagesquiz/ZEY.png',
	'./images/semaphore/imagesquiz/DEL.png',	'./images/semaphore/imagesquiz/KAF.png',	'./images/semaphore/imagesquiz/REH.png',	'./images/semaphore/imagesquiz/THEH.png',     
	'./images/semaphore/imagesquiz/DHEL.png',	'./images/semaphore/imagesquiz/KHAH.png',	'./images/semaphore/imagesquiz/SAD.png',	'./images/semaphore/imagesquiz/WAW.png',       

	  ]),
	  ('data',
	   [ 
	   ]
       ),
	  ('ar',
	   ['./ar/style.css',
	   './ar/scoutgame_body.html',
       './ar/about.html',
      './ar/morsehelp.html',
      './ar/semaphorehelp.html',
      './ar/codepointhelp.html',
       './ar/help_body.html']
       ),
	  ('ar/images',
	  [	  './ar/images/print.png',
	  './ar/images/save.png',
	  './ar/images/preview.png',
	  './ar/images/copy.png',
	  './ar/images/cut.png',
	  './ar/images/font.png',
	  './ar/images/help.jpg',
	  './ar/images/new.png',
	  './ar/images/exit.png',
	  './ar/images/zoomin.png',
	  './ar/images/zoomout.png',
	  './ar/images/logo.png' ])
	  ]);

