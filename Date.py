import datetime

now = datetime.datetime.now()

print(now)
print(f'Today: {now:%d} {now:%B} of {now:%Y}')
print(f'Time: {now:%H}:{now:%M}:{now:%S}')
