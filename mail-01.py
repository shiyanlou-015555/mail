#导入包：
import smtplib
from email.mime.text import  MIMEText
# 参数
# 1.邮件内容
# 2.MIME子类型,我们用plain表示text类型
# 3.邮件编码格式
msg = MIMEText("hello","plain","utf-8")
#发送email地址，要账号密码，但是密码不是你的用户密码，而是授权码
from_addr = "15530258872@163.com"
from_pwd = "qq168571"
#收件人信息
to_addr = "1685715822@qq.com"
#输入smtp服务器地址
#任何一家邮件都需要开启授权权限
smtp_srv = "smtp.163.com"
try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),8872)

    #服务器地址byte流，465默认加密端口
    srv.set_debuglevel(1)
    srv.starttls()
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr=from_addr, to_addrs=to_addr,msg=msg.as_string())
    srv.quit()
except Exception as e:
    print(e)
    print("cuo")


