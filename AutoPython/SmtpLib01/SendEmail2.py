import smtplib
from email.mime.text import MIMEText

# 登陆邮箱
sent = smtplib.SMTP()
sent.connect('smtp.qq.com', 25)
mail_name = "1546126430@qq.com"  # 发送人邮箱地址
mail_password = "zxh"  # 注意：这里不是密码，而应该填写授权码！！
sent.login(mail_name, mail_password)  # 登陆

# 编辑邮件内容
to = ['receiver@qq.com']  # 收件人邮箱地址
content = MIMEText('你好，我是圣洁不吃冰淇淋🍦')  # 正文内容
content['Subject'] = '漂流瓶'  # 邮件标题
content['From'] = mail_name  # 发件人
content['To'] = ','.join(to)  # 收件人，用逗号连接多个邮件，实现群发

# 发送邮件
try:
    print("该实例暂")
    sent.sendmail(mail_name, to, content.as_string())  # 3个参数 发送人，收件人，邮件内容
    print('Success')
    sent.close()
except smtplib.SMTPException:
    print("Error：Fail")
