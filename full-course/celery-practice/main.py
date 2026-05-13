from tasks import exponent

# uuid = exponent.delay(3, 4)
# print(uuid)

for i in range(100):
    uuid = exponent.delay(i, i % 10)
    print(uuid)
