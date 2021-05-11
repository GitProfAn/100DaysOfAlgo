# Solution 1
# O(nlog(n)) time / O(n) space
# n - length of the times array 

def laptopRentals(times):
  if len(times) == 0:
    return 0

  times.sort(key = lambda x: x[0])

  timesWhenLaptopIsUsed = [times[0]]
  heap = MinHeap(timesWhenLaptopIsUsed)

  for idx in range(1, len(times)):
    currentInterval = times[idx]
    if heap.peek()[1] <= currentInterval[0]:
      heap.remove()

    heap.insert(currentInterval)

  return len(timesWhenLaptopIsUsed)

class MinHeap:
  def __init__(self, array):
    self.heap = self.buildHeap(array)

  def buildHeap(self, array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
      self.siftDown(currentIdx, len(array) - 1, array)
    return array

  def siftDown(self, currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
      childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
      if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
        idxToSwap = childTwoIdx
      else:
        idxToSwap = childOneIdx
      if heap[idxToSwap][1] < heap[currentIdx][1]:
        self.swap(currentIdx, idxToSwap, heap)
        currentIdx = idxToSwap
        childOneIdx = currentIdx * 2 + 1
      else:
        return

  def siftUp(self, currentIdx, heap):
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
      self.swap(currentIdx, parentIdx, heap)
      currentIdx = parentIdx
      parentIdx = (currentIdx - 1) // 2

  def peek(self):
    return self.heap[0]

  def remove(self):
    self.swap(0, len(self.heap) - 1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, len(self.heap) - 1, self.heap)
    return valueToRemove

  def insert(self, value):
    self.heap.append(value)
    self.siftUp(len(self.heap) - 1, self.heap)

  def swap(self, i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]


# Solution 2
# O(nlog(n)) time / O(n) space
# n - length of the times array 

def laptopRentals(times):
  if len(times) == 0:
    return 0

  usedLaptops = 0
  startTimes = sorted([interval[0] for interval in times])
  endTimes = sorted([interval[1] for interval in times])

  startIterator = 0
  endIterator = 0
  
  while startIterator < len(times):
    if startTimes[startIterator] >= endTimes[endIterator]:
      usedLaptops -= 1
      endIterator += 1
    
    usedLaptops += 1
    startIterator += 1
  return usedLaptops
