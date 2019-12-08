#coding:utf8

import time
import threading

class ThreadSafeQueueException(Exception):
  pass


## 线程安全的队列
class ThreadSafeQueue(object):
  def __init__(self, max_size=0, logger=None):
    self.queue = []
    self.max_size = max_size
    self.lock = threading.Lock()
    self.condition = threading.Condition()
    self.logger = logger

  ## 返回当前队列数量
  def size(self):
    self.lock.acquire()
    size = len(self.queue)
    self.lock.release()
    return size

  ## 往队列里放元素
  def put(self, item):
    print 'put', self.logger==None
    if not self.logger:
      logger.debug('put %s', str(item))
    if self.max_size != 0 and self.size() > self.max_size:
      return ThreadSafeQueueException()

    if not self.logger:
      logger.debug('put lock')
    self.lock.acquire()
    self.queue.append(item)
    self.lock.release()
    if not self.logger:
      logger.debug('put unlock')


    if not self.logger:
      logger.debug('pup condition lock')
    self.condition.acquire()
    self.condition.notify()
    self.condition.release()
    if not self.logger:
      logger.debug('pup condition unlock')

    pass

  def extend(self, items):
    if not isinstance(items, list):
      items = list(items)

    for item in items:
      slef.put(item)

  ## 从队列取出元素
  def pop(self, block=True, timeout=None):
    if self.size() == 0:
      ## 需要阻塞等待
      if block:
        self.condition.acquire()
        self.condition.wait(timeout=timeout)
        self.condition.release()

      else:
        return None

    self.lock.acquire()
    item = None
    if len(self.queue) > 0:
      item = self.queue.pop()
    self.lock.release()
    return item

  def get(self, index):
    self.lock.acquire()
    item = self.queue[item]
    self.lock.release()
    return item

  def remove(self, item):
    if not self.logger:
      logger.debug('remove lock')

    self.lock.acquire()
    if item in self.queue:
      self.remove(item)
    self.lock.release()

    if not self.logger:
      logger.debug('remove unlock')

    if not self.logger:
      logger.debug('remove condition lock')
    self.condition.acquire()
    self.condition.notify()
    self.condition.release()
    if not self.logger:
      logger.debug('remove condition release')

