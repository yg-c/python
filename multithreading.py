# Multithreading 

import threading
import time

class myThread(threading.Thread):
	def __init__(self, threadId, name, count):
		threading.Thread.__init__(self) # parent constructor method
		self.threadId = threadId
		self.name = name
		self.count = count

	def run(self):
		print('Starting' + self.name + '\n')
		print_time(self.name, 1 ,self.count)
		print('Exiting:' + self.name + '\n')


def print_time(name, delay, count):
	while count:
		time.sleep(delay)
		print('%s: %s %s' % (name, time.ctime(time.time()), count) + '\n')
		count -= 1

thread1 = myThread(1, 'Thread1', 10)
thread2 = myThread(2, 'Thread2', 5)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('Done main thread')

''' 
Checkout example 

- Process payment 5s
- Send email confirmation 10s
- Load thx page 3s

'''

class myThread(threading.Thread):
	def __init__(self, threadId, name, count):
		threading.Thread.__init__(self) # parent constructor method
		self.threadId = threadId
		self.name = name
		self.count = count

	def run(self):
		print('Starting' + self.name + '\n')
		threadLock.aquire() # lock
		print_time(self.name, 1 ,self.count)
		threadLock.release() # release
		print('Exiting:' + self.name + '\n')

class myThread2(threading.Thread):
	def __init__(self, threadId, name, count):
		threading.Thread.__init__(self) # parent constructor method
		self.threadId = threadId
		self.name = name
		self.count = count

	def run(self):
		print('Starting' + self.name + '\n')
		threadLock.aquire() # lock, if another thread is locked before running it
		threadLock.release() # release
		print_time(self.name, 1 ,self.count)
		print('Exiting:' + self.name + '\n')


def print_time(name, delay, count):
	while count:
		time.sleep(delay)
		print('%s: %s %s' % (name, time.ctime(time.time()), count) + '\n')
		count -= 1

thread1 = myThread(1, 'Payment', 5)
thread2 = myThread2(2, 'Sending e-mail', 10)
thread3 = myThread2(3, 'Loading page', 3)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()

print('Done main thread')