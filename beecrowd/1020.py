days = int(input())
years = days // 365
months = (days - years * 365) // 30
days_new = (days - years * 365 - months * 30) 
print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days_new} dia(s)')