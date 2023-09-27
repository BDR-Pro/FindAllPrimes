import json
import time

start = 2
limit = 99999999

def sieve_of_eratosthenes(start,limit):
    sieve = {}
    if start== 0 or 1:
        start=2
    for i in range(start,limit):
        sieve[i]=True
    for current in range(start, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False
    return sieve


start = time.time()

res=sieve_of_eratosthenes(int(start),int(limit))

with open("PrimeNumber.json",'w') as jsonfile:
    json.dump((res),jsonfile)

print(res)
end = time.time()


print(end-start)