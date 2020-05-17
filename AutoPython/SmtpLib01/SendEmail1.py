import smtplib
import string

HOST = "smtp.qq.com"
SUBJECT = "test email from python"
FROM = "1546126430@qq.com"
TO = "1546126430@qq.com"
text = "python alert"
BODY = "\n".join(
    ("From: %s" % FROM,
     "To: %s" % TO,
     "Subject: %s" % SUBJECT,
     "", text
     )
)
print("简单文本的发邮件功能")
server = smtplib.SMTP(HOST)
server.login("1546126430@qq.com", "skkeoftvqhxkgajb")
server.sendmail(FROM, [TO], BODY)
server.quit()
