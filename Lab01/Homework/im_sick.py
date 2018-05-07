from gmail import GMail, Message
from datetime import datetime

now = datetime.now()
print (now)

while True:
    if now.hour >= 7:
        mail = GMail('sone.2809@gmail.com', 'khoangkhoang')
        mgs = Message("Don xin nghi om", to="luongnhuyen@gmail.com", text = "Em xin phep nghi om")
        mail.send(mgs)
        break
