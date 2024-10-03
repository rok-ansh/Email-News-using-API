import smtplib, ssl


def get_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "rohitdswork1@gmail.com"
    password = "bitd uvlf mahs roii"

    receiver = "rohitdswork1@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

