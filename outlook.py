import win32com.client


def send_mail(to, subject, content, atch=[]):
    # Outlook Object Model 불러오기
    new_Mail = win32com.client.Dispatch("Outlook.Application")
    Txoutlook = new_Mail.CreateItem(0)

    # 메일 수신자
    Txoutlook.To = to
    # 메일 참조
    # new_Mail.CC = "mail-add-for-cc@testadd.com"
    # 메일 제목
    Txoutlook.Subject = subject
    # 메일 내용
    Txoutlook.HTMLBody = content

    # 첨부파일 추가
    if atch:
        for file in atch:
            Txoutlook.Attachments.Add(file)

    # 메일 발송
    Txoutlook.Send()