seconds = int(input())
hour = seconds // 3600
minutes = (seconds - (hour*3600)) // 60
new_seconds = seconds - (hour*3600 + minutes*60)
print(f'{hour}:{minutes}:{new_seconds}')