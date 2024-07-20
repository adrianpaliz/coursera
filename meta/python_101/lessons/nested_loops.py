import time

start_time = time.time()

# Outer loop
for index in range(5):
    # Inner loop
    for item in range(10):
        print(0, end = " ")
    print()

print(round((time.time() - start_time), 2)) 
