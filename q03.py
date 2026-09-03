seconds = 3725
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_1 = (seconds % 3600) % 60
print(f"{hours}시간 {minutes}분 {seconds_1}초")