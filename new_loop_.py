password = 'a123456'
timess = 3

while timess != 0 :
    timess -= 1
    psd = input('請輸入密碼: ')
    if psd == password :
        print('成功登入')
        break
    else:
        print('密碼錯誤')
        if timess > 0 :
            print('還有',timess ,"次機會")
        else:
            print('已鎖帳號，請洽詢服務人員')




    