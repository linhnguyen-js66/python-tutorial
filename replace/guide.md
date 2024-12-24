```python
def get_num_str(n):
    chars = []
    if(n > 2):
        for num in range(1, n-1):
            chars.append(str(num))
            chars.append(str(num + 2))
    return "-".join(chars)

get_num_str(6)
```
1. Giải thích cách hoạt động replace
   - Với n = 6, vòng lặp for chạy từ 1-5 (vì đang tìm số nguyên dương nên tính từ 1)
   - Lần lặp thứ 1:
   - ```python
     * num = 1 => ["1"] => ["_3"]
     * num = 2 => ["_2"] => ["_4"]
     * num = 3 => ["_3"] => ["_5"]
     * num = 4 => ["_4"] => ["_6"]
     * num = 5 => ["_5"] => ["_7"]
     ```