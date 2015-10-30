#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def sendemail(sender,receiver,subject,content,smtpserver,smtpuser,smtppass):
    msg = MIMEText(content,'html','utf-8')#中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '<%s>' % sender
    msg['To'] = ";".join(receiver)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(smtpuser, smtppass)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception,e:
        print e