print("-------Queue----Also Knowns as FIFO--")

from collections import deque

bank = deque(["rahim","Karim","Wahid"])

print(bank)
bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("No person left")
