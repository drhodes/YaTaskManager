import task_queue
import random

class TestSortQueue:
    def __init__(self):
        self.items = []

    def insert_item_helper(self, item, idxL, idxR):
        #print(f"inserting {item}")
        if idxL == idxR:
            self.items.insert(idxL, item)
        else:
            idxM = idxL + (idxR - idxL) // 2
            midItem = self.items[idxM]
            #print(f"item: {item}, idxL: {idxL}, idxR: {idxR}, idxM: {idxM}, items: {self.items}, midItem: {midItem}")    
            if item > midItem:
                # insert to the left, as the highest priorities are at the front.
                #print("inserting left")
                self.insert_item_helper(item, idxL, idxM)
            else:
                #print("inserting right")
                self.insert_item_helper(item, idxM+1, idxR)
    
    def insert(self, item):
        if len(self.items) == 0:
            self.items.append(item)
        else:
            self.insert_item_helper(item, 0, len(self.items))


def test_item_queue():
    for n in range(1, 30):
        q = TestSortQueue()
        for _ in range(n):
            num = random.randint(0,1000)
            if num in q.items:
                continue # simply skip it.
            q.insert(num)
            # are the items actually sorted?
            # check against pythons sort.
            before_sort = tuple(q.items)
            after_sort = tuple(reversed(sorted(q.items)))
            if not after_sort == before_sort:
                print(f"after_sort : {after_sort}")
                print(f"before_sort: {before_sort}")
                raise Exception("not sorted!")
