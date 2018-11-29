from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart
#添加带附件的邮件
mail_mul = MIMEMultipart()
#构建邮件正文
mail_text = MIMEText("hello","plain","utf-8")
#把邮件正文添加进入附件中
mail_mul.attach(mail_text)
# 假设还有一个本地文件
with open("a.txt","rb") as f:
    s = f.read()
    m = MIMEText(s,"base64","utf-8")
    m["Content-Type"]= "application/octet-stream"
    m["Content-Disposition"] = "attachment;filename = 'a.txt'"
    mail_mul.attach(m)
#填写收件人信息
from_addr = "15530258872@163.com"
from_pwd = "qq168571"
to_addr = "15530258872@163.com"
smtp_srv = "smtp.163.com"
try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) #SMTP协议默认端口25
    #登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接受地址，必须是list形式
    # 3. 发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)