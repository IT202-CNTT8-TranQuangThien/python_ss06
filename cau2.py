# câu 2:
password = 123456

for count in range(1, 4):
        check_pass = int(input(f'Nhập mật khẩu lần thứ {count}: '))
        if check_pass == password:
            print(f'Đăng nhập thành công!')
            break
        else:
            if count == 3:
                print(f'Tài khoản bị khóa')
                break
            print(f'Mật khẩu sai vui lòng nhập lại')
