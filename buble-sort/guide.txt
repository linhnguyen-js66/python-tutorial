1. Giải thích cách hoạt động của thuật toán buble sort:
Bubble Sort là thuật toán sắp xếp đơn giản nhất hoạt động 
bằng cách hoán đổi liên tục các phần tử liền kề nếu chúng không đúng thứ tự.
Thuật toán này không phù hợp với các tập dữ liệu lớn vì độ phức tạp thời gian 
trung bình và trường hợp xấu nhất của nó khá cao.
2. Giải thích cách hoạt động của buble sort
a) Vòng lặp ngoài (for i):
- Biến i đại diện cho vị trí hiện tại trong mảng đang được kiểm tra. Đây là ví trí 
mà giá trị nhỏ nhất từ các phần tử còn lại sẽ được đặt vào

b) Vòng lặp trong (for j):
- Biến j bắt đầu từ i+1 và kiểm tra các phần tử sau i trong mảng
- So sánh giá trị numbers[j] với numbers[i]

c) Điều kiện hoán đổi (if numbers[j] < numbers[i])
- Nếu giá trị tại numbers[j] nhỏ hơn number[i], thì hoán đổi hai giá trị 
- Dùng bién temp để lưu giá trị tạm thời trong quá trình hoán đổi

d) Kết quả sau mỗi lần lặp
- Bubble Sort là thuật toán sắp xếp đơn giản nhất hoạt động bằng cách hoán đổi liên tục các 
phần tử liền kề nếu chúng không đúng thứ tự. Thuật toán này không phù hợp với các tập dữ liệu 
lớn vì độ phức tạp thời gian trung bình và trường hợp xấu nhất của nó khá cao.

e) Minh hoạ: 

numbers = [20, 10, 16, 6, 89]
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[i]:
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp

1. Lần lặp đầu tiên i = 0:
- So sánh từng phần tử:
* numbers[1] (10) < numbers[0] (20): Hoản đổi [10, 20, 16, 6, 89]
* numbers[2] (16) > numbers[0] (10): Không hoán đổi
* numbers[3] (6) < numbers[0] (10): Hoán đổi [6, 20, 16, 10, 89]
* numbers[4] (89) > numbers[0] (6): Không hoán đổi

2. Lần lặp thứ 2 (i = 1): Lúc này mảng đang có dạng [6, 20, 16, 10, 89]
- So sánh phần tử:
* numbers[2] (20) < number[1] (16): Hoán đổi [6,16,20,10,89]
* numbers[3] (10) < number[1] (16): Hoán đổi [6,10,20,16,89]
* numbers[4] (89) > number[1] (10): Không hoán đổi

3. Lần lặp thứ 3 (i = 2): Lúc này mảng đang có dạng  [6,10,20,16,89]
- So sánh phần tử: 
* numbers[3] (16) < numbers[2] (20): Hoán đổi [6,10,16,20,89]
* numbers[4] (89) > numbers[2] (16): Không hoán đổi

4. Lần thứ 4: Còn 1 phần tử cuối
 => IN RA MẢNG CUỐI: [6,10,16,20,89]