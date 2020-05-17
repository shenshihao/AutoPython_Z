# coding: utf-8
import smtplib
from email.mime.text import MIMEText

HOST = "smtp.qq.com"
SUBJECT = "test email from python"
FROM = "1546126430@qq.com"
TO = "1546126430@qq.com"

msg = MIMEText("""
    <table width="1600" border="0" cellspacing="0" cellpadding="4">
    <tr>
        <td bgcolor="#CECFAD" headers="20" style="font-size:14px">*官网数据</td>
    </tr>
    <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
            1) 日访问量: <font color="red"> 152433</font> <br>
            2）状态码信息 500
        <td>
    </tr>
    </table>
""", 'html', 'utf-8')

# msg = MIMEText(mail_message, 'html', 'utf-8')
# print(msg)

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['to'] = TO
server = smtplib.SMTP(HOST)
server.login("1546126430@qq.com", "skkeoftvqhxkgajb")
server.sendmail(FROM, TO, msg.as_string())
server.quit()
print("send ok")
