import smtplib
msg='mail sent from python'
smtpObj=smtplib.SMTP('gmail.com',587)
smtpObj.login('vivek111vivu555@gmail.com','Act@Sony111999')
smtpObj.sendmail('vivek111vivu555@gmail.com','viveksharma11125@gmail.com',msg)
