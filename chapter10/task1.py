class intDict(object):

    def __init__(self, numBuckets):

        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, key, dictVal):
        hashBucket = self.buckets[key % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal))

    def getValue(self, key):
        hashBucket = self.buckets[key % self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None


def __str__(self):
    result = "{"
    for b in self.buckets:
        for e in b:
            result = result + str(e[0]) + ":" + str(e[1]) + ","
    return result[:-1] + "}"
