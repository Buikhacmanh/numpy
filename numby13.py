import numpy as np
np.random.randint(0, 2) # Ngẫu nhiên số nguyên trong khoảng [0, 2)
coins = np.random.randint(2, size=1000) 
print(coins.shape)
(1000,)
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
coins = np.random.choice([0, 1], size=1000, p=[0.2, 0.8]) # random.choice sẽ lấy ngẫu nhiên các phần tử trong mảng ở tham số đầu tiên với xác suất ở tham số p
print("% số lần tung được mặt ngửa: ", (coins == 0).mean() * 100)
print("% số lần tung được mặt úp: ", (coins == 1).mean() * 100)
#Trong trường hợp đồng xu, “n” sẽ là số lần lật và “p” sẽ là xác suất thành công ( = 0.5):
np.random.binomial(20, 0.5) # Số mặt ngửa nhận được khi tung đồng xu 10 lần
np.random.binomial(20, 0.5, 10) # Số mặt ngửa nhận được khi tung đồng xu 20 lần trong 10 lần lặp
print("Trung bình số mặt ngửa nhận được khi tung đồng xu 20 lần trong vòng 10 lần lặp: ", np.random.binomial(20, 0.5, 10).mean())
