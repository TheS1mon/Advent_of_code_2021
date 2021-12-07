from collections import defaultdict
# GET DATA
data = []
with open("06_input.txt") as f:
    data = f.readlines()
# save Data to array
current_timers = list(map(int, data[0].split(',')))
counter = defaultdict(int)
# initial counter, how many occurences of fish by time exists
for time in current_timers: counter[time] += 1

for _ in range(256):
    new_counter = defaultdict(int)
    for time in counter:
        if time == 0:
            new_counter[8] += counter[0]
            new_counter[6] += counter[0]
        else:
            new_counter[time - 1] += counter[time]

    counter = new_counter
print(sum(counter.values()))