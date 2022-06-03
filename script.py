from urllib import response
import requests                        # http requests
from bs4 import BeautifulSoup          # web scrapping
import smtplib                         # Send Email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText   # System date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder 

content =  ''

# Extracting Hacker news Stories

def extract_news(url):
    print('Extracting Hacker news Stories.....')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text != 'More' else '')

    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>----------<br>')
content += ('<br><br>End of Message')

# Let's send the Email

print('Composing Email.....')

# update your Email details

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'yv041041@gmail.com'
TO = 'yverma041@gmail.com'
PASS = 'dellvostro2'

# fp = open(file_name, 'rb')
# Create a text/plain message
# msg = MIMEText()
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)

msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
# fp.close()

# Authenticating Server
print('Initiating Server.....')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent......')

server.quit()