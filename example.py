from send_mail import send_mail

send_from = ""
send_to = ""
subject = ""
message = ""
files = [""]
server = ""
port = 587
username = ""
password = ""
use_tls = True

send_mail(send_from, send_to, subject, message, files,
              server, port, username, password,
              use_tls)
