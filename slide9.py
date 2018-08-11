#!C:/Python34/python.exe
import cgi, cgitb
import sys
#from iterable import chain
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()

print("Content-type:text/html\r\n\r\n")
if __name__ == '__main__':

    config = {
               'host': '127.0.0.1',
               'port': 3306,
               'database': 'project',
               'user': 'root',
               'password': '',
               'charset': 'utf8',
               'use_unicode': True,
               'get_warnings': True,
               }

def hotels(config):
    print('<h1>')
    print('<a href="slide7.py">')
    print('Check In')
    print('</a></h1>')
    print('<h1><a href="slide8.py">')
    print('\tCheckout')
    print('</a></h1></div>')


def home():
    print("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Admin Access</title>
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <link href="style/main.css" rel="stylesheet" type="text/css" media="screen" />
    <link href="style/animate.css" rel="stylesheet" >
    <script src = "js/wow.min.js"></script>
    <script>
        new WOW().init();
    </script>

    </head>
    <body background = "hotel12.jpg">
    <div class ="supreme">
    <form action ="testing.py" method="get">
        <div class ="wow animated fadeInDown" data-wow-delay = "1s" >
            <img src="hotels-6.png" width= 1200 height= 500 border=0 alt="">
        </div>
        <div class = "col-2">
        <div>
         <div>

         </div>
       </form>
       <div class="wow fadeIn animated " data-wow-delay = "3s">
      """)
    hotels(config)
    print ("""
            </body>
            </html>""")

home()
