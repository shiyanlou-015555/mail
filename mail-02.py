from email.mime.text import  MIMEText

mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>

        <h1> 这是一封HTML格式邮件</h1>

        </body>
        </html>
        """

msg = MIMEText(mail_content, "html", "utf-8")

# 构建发送者地址和登录信息
from_addr = "15530258872@163.com"
from_pwd = "qq168571"


# 构建邮件接受者信息
to_addr = "15530258872"

smtp_srv = "smtp.163.com"


try:
    import smtplib

    srv = smtplib.SMTP(smtp_srv.encode(), 25)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)
