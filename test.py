# câu 1:
# price = int(input('Nhập đơn gía cho sản phẩm: '))
# quantity = int(input('Nhập vào số lượng muốn mua: '))
#
# sum = int(price * quantity)
#
# if sum >= 1000000:
#     sum = int(sum * 0.9)
# else:
#     sum = sum
# print(f'Số tiền phải thanh toán là: {sum} VNĐ')

# câu 2:
# password = 123456
# for count in range(1, 4):
#
#     check_pass = int(input(f'Nhập mật khẩu lần thứ {count}: '))
#     if check_pass == password:
#         print(f'Đăng nhập thành công!')
#         break
#     else:
#         print(f'Mật khẩu sai vui lòng nhập lại')
#
#     if count == 3:
#         print(f'Tài khoản bị khóa')
# cau 3:
sum_quantity_product = 0
count_quantity_box = 0
while True:
    quantity_box = int(input('Nhập số thùng hàng: '))

    if quantity_box < 0:
        print(f'Số lượng không hợp lệ bỏ qua thùng này!')
    elif quantity_box == 0:
        break
    else:
        sum_quantity_product += quantity_box
        count_quantity_box += 1

print(f'Tổng số thùng hàng hợp lệ đã đếm: {count_quantity_box}')
print(f'Tổng số lượng sản phẩm thu được: {sum_quantity_product}')




