#密碼重試程式 
#password = 'abc123'
#使用者最多可以輸入3次密碼
#輸入正確便會印出'登入成功'
#輸入錯誤便會印出'密碼錯誤 還有____次機會'

password = 'abc123'
x = 3 #輸入密碼的剩餘次數
while x > 0:
    x = x - 1
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!')
        break
    else:
        print('密碼錯誤!')
        if x > 0:
            print('還有', x, '次機會')
        else:
            print('登入失敗!')
           
		    