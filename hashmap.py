#Implementing hashmaps(dictionaries) in python using lists

print hash('Hello')
#Converts string to a number; a built-in function

a=[1,2,3,4]
print list(enumerate(a))
#enumerate fucntion converts lists to tuples; gives 0,1,2... as keys for the values in the list and creates tuple for them

def new(num_buckets=256):
    '''Initialises a map with the given no of buckets'''
    
    aMap=[] #Empty list
    
    for i in range(0,num_buckets):
        aMap.append([])
        
    return aMap
    
def hash_key(aMap,key):
    '''Given a key, (which is a string), create a number(using bulit in hash fuction) and then convert it to an index for the aMap's buckets by dividing by the number of buckets to find the remainder'''
    return hash(key) % len(aMap)
    
def get_bucket(aMap, key):
    '''Given a key, find the bucket where it should go'''
    
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]
    
def get_slot(aMap, key, default=None):
    '''Uses get_bucket to get the bucket the key could be in and then it simply rolls through every element of the bucket, untill it find a matching key.
    Then it returns (i,k,v) which is the index at which the key was found, the key itself, and the value corresponding to that key.'''       
    
    bucket = get_bucket(aMap, key)
    print list(enumerate(bucket))
    for i, kv in enumerate(bucket):
        
        k,v = kv
        
        if key==k:
            return i,k,v
            
            
    return -1,key,default #If not found
    
def get(aMap, key, default='None'):
    '''Get's the value in the bucket for a given key. If not present, it gives out default.'''
    i,k,v = get_slot(aMap, key),default=None) 
    
    return v #returns value
    
def set(aMap, key, value):
    '''Sets the key to value; replaces any existing value'''
    
    bucket=get_bucket(aMap, key)
    i,k,v= get_slot(aMap, key)
    
    if i>= 0:
        #key exists! Set the value for the key.
        bucket[i]=[key,value]
        
    else:
        #Key doesn;t exist; append the list 'bucket' to create it
        bucket.append((key,value))
        
        
def delete(aMap, key):
    '''Deletes the given key from the map'''
    bucket=get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break
            
def list(aMap):    
    '''Print out what\'s''the map'''
    
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print k,v
    
    
    
    
    
    
    
