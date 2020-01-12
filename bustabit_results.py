from hashlib import sha256
import hmac
import math
import binascii

hash_id=["79f6bbae758befa1e06f0ecb3722458144610de4bb72fd548b9709120618e54f", 2729956] #hash and game id of the hash
N=100 # results to check, starting from game id
assert N<=hash_id[1]
busted=list()

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    if iteration == total:
        print()

def result(seed, salt='0000000000000000004d6ec16dafe9d8370958664c1dc422f452892264c59526'):
    bits = 52  
    seed = hmac.new(salt.encode(), binascii.unhexlify(seed), digestmod=sha256).hexdigest()
    seed = seed[0:int(bits/4)]
    r = int(seed, 16)
    res = r/pow(2, bits)
    res = 99/(1-res)
    result = math.floor(res)
    return max(1, result/100)

print("Checking results...")
printProgressBar(0, N, length = 50)
for i in range(N):
    busted.append(str(hash_id[1]) + ": " + str(result(str(hash_id[0]))) + "\n")
    hash_id[0] = sha256(str(hash_id[0]).encode('utf-8')).hexdigest()
    hash_id[1]-=1
    if i%(int(N/100))==0:
        printProgressBar(i + 1, N, length = 50)

print("\nWriting on file...")
printProgressBar(0, N, length = 50)
with open("results.txt", "a") as f:
    for i in range(N):
        f.write(busted[i])
        if i%(int(N/100))==0:
            printProgressBar(i + 1, N, length = 50)
print()