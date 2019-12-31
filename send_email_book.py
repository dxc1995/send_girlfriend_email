from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import random,time,schedule
import find_moves 

def sender_girl_email():
    # QQ邮箱smtp服务器
    host_server = "smtp.qq.com"
    # sender_qq为发件人的qq号码
    sender_qq = "xxxx此处替换成你的qq号"
    # pwd为QQ邮箱的授权码
    pwd = "xxxx输入你的验证码"
    # 发件人的邮箱
    sender_qq_email = "xxxx输入发件人邮箱"
    # 收件人邮箱
    receiver = "xxxx填入收件人邮箱"
    #邮件的正文内容
    mail_content = read()
    # 邮件标题
    mail_title   = "xxx标题自选"

    #ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglever()是用来调试的,参数值为1表示开启调试模式,参数值为关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", "utf-8")
    msg["Subject"] = Header(mail_title, "utf-8")
    msg["From"] = sender_qq_email
    msg["To"] = receiver
    smtp.sendmail(sender_qq_email, receiver, msg.as_string())
    smtp.quit()

def read():
    file = open("猫眼电影最近上映.txt", "r", encoding="utf-8").read()
    return file
# 任务调度器 每天17：30抓取电影信息发送邮箱给女朋友
schedule.every().day.at("17:30").do(sender_girl_email)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
    


