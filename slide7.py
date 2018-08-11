#!C:/Python34/python.exe
import cgi, cgitb
import sys
#from iterable import chain
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()
qrytable = form.getvalue('hotels')
stat = form.getvalue('choice')

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
    db = mysql.connector.Connect(**config)
    cursor = db.cursor()
    if qrytable == "four seasons" :
        print("""<form action="slide7.py"
                    <div><select name="choice">
                    <option value="201">Royal</option>
                    <option value="202">Family</option>
                    <option value="203">Presidential</option>
                    </select></div><br/><br/>
                    <input type ="submit" value ="Check In"/>
                        </form>""")


    elif qrytable == "fat duck" :
        print("""<form action="slide7.py"
                    <div><select name="choice">
                    <option value="204">Royal</option>
                    <option value="205">Penthouse</option>
                    <option value="206">Sky villa</option>
                    </select></div><br/><br/>
                    <input type ="submit" value ="Check In"/>
                        </form>""")



    elif qrytable == "lime wood" :
        print("""<form action="slide7.py"
                    <div><select name="choice">
                    <option value="207">Family</option>
                    <option value="208">Skyvilla</option>
                    </select></div><br/><br/>
                    <input type ="submit" value ="Check In"/>
                        </form>""")


    elif qrytable == "oasis" :
        print("""<form action="slide7.py"
                    <div><select name="choice">
                    <option value="209">Royal</option>
                    <option value="210">Pent House</option>
                    <option value="211">Family</option>
                    </select></div><br/><br/>
                    <input type ="submit" value ="Check In"/>
                        </form>""")



    elif qrytable == "tipton" :
        print("""<form action="slide7.py"
                    <div><select name="choice">
                    <option value="212">Presidential</option>
                    <option value="213">Sky villa</option>
                    </select><br/></div><br/><br/>
                    <input type ="submit" value ="Check In"/>
                        </form>""")
    if stat != None :
        cursor.execute(("update rooms set status = 'no' where roomid = '%s' ; ") %stat)
        db.commit()
        cursor.execute(("select message from messages") )
        res=cursor.fetchall()
        for i in range(0,len(res)):
            print(res[i][0])




def home():
    print("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Check In</title>
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <link href="style/main.css" rel="stylesheet" type="text/css" media="screen" />
    <link href="style/animate.css" rel="stylesheet" >
    </head>
    <body background="hotel12.jpg">

        <div class ="supreme">
          <div class ="animated slideInDown">

        </div>
        <div class = "animated fadeIn">
            <h1 name ="heading" class="hd" id="tre"> Check In </h1>
            <a href = "slide1.py" style="float:left"><button><-- Back</button></a>
        <br/><br/></div>
        <form action ="slide7.py" method="get">
        <div class ="animated fadeIn">
            <select name="hotels">
            <option value="four seasons">Four Seasons</option>
            <option value="fat duck">Fat Duck</option>
            <option value="lime wood">Lime Wood</option>
            <option value="oasis">Oasis</option>
            <option value="tipton">Tipton</option>
            </select>
        </div>

        <div class ="animated fadeIn">
            <input type ="submit" value ="QUERY"/>
        </div>
        </div>
        </form>""")
    hotels(config)
    print ("""</body>
            </html>""")

home()
