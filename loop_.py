password = 'a123456'
timess = 3

while timess != 0 :
    timess -= 1
    psd = input('請輸入密碼: ')
    if psd == password :
        print('成功登入')
        break
    else:
        print('輸入錯誤，還有'+str(timess) +"次機會")




    