import time

sentence = "Python is fun to learn"

input("Press enter to start")

start = time.time()
typed = input("Type this sentence: " + sentence + "\n")
end = time.time()

print("Time taken:", end - start, "seconds")
