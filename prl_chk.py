def prl_chk():
    password: str = input("Введите пароль: ")
    if password.lower() != password and password.upper() != password:
        j=0
        for i in password:
            j += 1
            spl_chars = "!@$%^&*-_=+0123456789"
            if i in spl_chars:
                print("Пароль успешно принят")
                break
            else:
               if j == len(password):
                # if i == password.end:
                   print("Пароль не может быть принят, так как не содержит\nспециальных "
                         "символов или цифр")
    else:
        print("Пароль должен содержать буквы в верхнем и нижнем регистре,\nа так же цифры"
              " или специальные символы\nПовторите ввод пароля")
        return password

prl_chk()