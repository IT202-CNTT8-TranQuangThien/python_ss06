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