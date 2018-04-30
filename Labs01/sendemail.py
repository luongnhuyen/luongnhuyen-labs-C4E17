from gmail import GMail, Message
from random import choice
gmail=GMail('sone.2809@gmail.com','khoangkhoang')
# mgs=Message('Don xin nghi hoc', to='luongnhuyen@gmail.com',html='<h1><span style="color: #ff0000; background-color: #003300;"><strong>Đơn xin nghỉ học</strong></span></h1>')
html_template='Bác sỹ bảo em bị {{sickness}}...ko em lại lây {{sickness}}.'
sickness_list = ["Thương hàn", "Cảm cúm","Ebola"]
sickness=choice(sickness_list)
html_content =html_template.replace("{{sickness}}","Thương hàn")
mgs=Message('Don xin nghi hoc', to='luongnhuyen@gmail.com',html=html_content)


gmail.send(mgs)
