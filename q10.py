apple = [3, 1500]
banana = [12, 800]
water_melon = [1, 22000]

print(f"상품명    수량        단가     금액")
print(f"-"*38)
print(f"사과    {apple[0]:<10,} {apple[1]:^8,} {apple[0]*apple[1]:>6,}")
print(f"바나나   {banana[0]:<10,} {banana[1]:^8,} {banana[0]*banana[1]:>6,}")
print(f"수박    {water_melon[0]:<10,} {water_melon[1]:^8,} {water_melon[0]*water_melon[1]:>6,}")
print(f"-"*38)
print(f"합계           {(3*1500)+(12*800)+(1*22000):>10,}")