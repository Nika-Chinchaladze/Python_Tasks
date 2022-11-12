from datetime import datetime
from Message_Class import SendEmail, my_gmail
from Work_Pandas import PandaDealer
from Text_Class import PrepareText

# my objects:
birthday = PandaDealer()
text_form = PrepareText()

# current date:
now = datetime.now()
current_month = now.month
current_day = now.day

# receiver's name and mail:
receiver_name = birthday.return_name(now_month=current_month, now_day=current_day)
receiver_mail = birthday.return_mail(now_month=current_month, now_day=current_day)

# send message:
if receiver_name != "not found" and receiver_mail != "not found":
    message = text_form.return_text(name=receiver_name)
    send_tool = SendEmail(sender=my_gmail, receiver=receiver_mail, subject="Happy Birthday", body=message)
    send_tool.send_mail()
    print("BirthDate Email has been sent, Successfully!")
else:
    print("Today is not your friend's birthdate!")
