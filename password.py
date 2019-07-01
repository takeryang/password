print('這是一個猜密碼的遊戲程式')

password = 'a123456'
i = 3
while i > 0:
	psw = input('請輸入密碼: ')
	if psw == password:
		print('登入成功!')
		break
	else:
		i = i - 1
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('沒機會了!遊戲結束!')