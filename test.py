# import multiprocessing
# import time

# # Your foo function
# def foo(n):
#     for i in range(5):
#         print ("Tick")
#         time.sleep(1)

# if __name__ == '__main__':
#     # Start foo as a process
#     p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
#     p.start()

#     # Wait 10 seconds for foo
#     p.join(10)

#     if p.is_alive():
#         print ("foo is running... let's kill it...")

#         # Terminate foo
#         p.terminate()
#         p.join()
#     print("Bitch")

#     # Cleanup

# list = [1,2,3,4]
# list[0] = "fsdfs"
# a = (1,1)
# a[0] += 1
# print(a)
import random
ss = set()
for i in range(10):
    ss.add(i)
print(random.choice(tuple(ss)))