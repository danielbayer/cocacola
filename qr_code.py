import qrcode
from PIL import Image
import PIL
import smtplib
from email.message import EmailMessage
import mysql.connector


data = "https://www.google.com/search?q=python+flask+template+download&client=ubuntu&hs=rWQ&sxsrf=ALeKk03T1JcQPKQ-QrEB2v2VhvwvlqnpCw:1604671470586&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiIwvCHi-7sAhXBzKQKHfdABvcQ_AUoAnoECAYQBA&biw=1920&bih=939#imgrc=YHDQbbtXD3oFMM"
img = qrcode.make(data)
img1 = img.save('a.png')

Link = gsutil

mydb = mysql.connector.connect(
  host="localhost",
  user="idan",
  password="Aa123456!",
  database="test"
)
mycursor = mydb.cursor()
sql = "INSERT INTO Names (ID, Name, personID, IDbarCode, link) VALUES (%s, %s, %s, %s, %s)"
val = (12,"Daniel","12",24,"http://test.test.com")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

# msg = EmailMessage()
# msg.set_content(img)

# msg['Subject'] = 'subject'
# msg['From'] = cocacola@gmail.com
# msg['To'] = idan.l@gmail.com

#s = smtplib.SMTP('maskte.com:25')
#s.send_message(msg)
#s.quit()