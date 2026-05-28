# câu 1:
price = int(input('Nhập đơn gía cho sản phẩm: '))
quantity = int(input('Nhập vào số lượng muốn mua: '))

sum = int(price * quantity)

if sum >= 1000000:
    sum = int(sum * 0.9)
else:
    sum = sum
print(f'Số tiền phải thanh toán là: {sum} VNĐ')






