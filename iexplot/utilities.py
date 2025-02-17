from numpy import inf

def make_nstack_list(obj,*nums,**kwargs):
    """
    obj is ndata object (e.g. data.AD or data.mda or data.mda[scanNum].EA)
    nums is scanNum or EAnum
    **kwargs from make_num_list):
        none
    """
    
    nData_list=[]
    scanNum_list = make_num_list(*nums,**kwargs)
    for scanNum in scanNum_list:
        nData_list.append(obj[scanNum])
    return nData_list

def make_num_list(*nums,**kwargs):
    """
    Making a shortlist based on *num
    *num =>
        nums: for a single scan
        first,last: for all numbers between and including first and last; last can be inf
        first,last,countby: to load a subset
        [num1,num2]: to load a subset does not need to be consecutive  
    """
    kwargs.setdefault('debug',False)
    if kwargs['debug']:
        print('_make_num_list')
        print('nums: ',*nums)

    num_list=[]
    if len(nums) == 1:
        if type(nums[0]) == int:
            num_list = [nums[0]]
        elif type(nums[0]) == list:
            num_list = nums[0]
        else:
            print(nums,'not a valid argument, see doc string')    
            return None
    elif len(nums) >= 2:
        if len(nums) == 2:
            first,last = nums
            countby = 1
        elif len(nums) == 3:
            first,last,countby = nums
        else:
            print(nums,'not a valid argument, see doc string') 
            return None
        for n in range(int(first),int(last+countby),int(countby)):
            num_list.append(n)
    else:
        print(nums,'not a valid argument, see doc string') 
        return None

    return num_list

def _shortlist(*nums,llist,**kwargs):
    """
    Making a shortlist based on *num
    *num =>
        nums: for a single scan
        inf: for all num in longlist
        first,last: for all numbers between and including first and last; last can be inf
        first,last,countby: to load a subset
        [num1,num2]: to load a subset of scans
    kwargs:
        debug=False
    """
    kwargs.setdefault("debug",False)
    
    if kwargs['debug']:
        print('\n_shortlist')
        print("\tnums: ",nums)
        print("\tllist",llist)

    llist.sort()

    ### dealing with inf
    last = llist[-1]
    if inf in nums:
        numslist = list(nums)
        numslist[numslist.index(inf)] = last
        nums = tuple(numslist)

    #creating number list
    num_list = make_num_list(*nums)
    shortlist = []
    for n in num_list: 
        if n in llist:
            shortlist.append(n)
    if kwargs["debug"]:
        print("shortlist: ",shortlist)
    return shortlist

    
def take_closest_value(my_list,my_number):
    """
    Given a list of integers, I want to find which number is the closest to a number x.
    
    Previously: TakeClosest
    """
    return min(my_list, key=lambda x:abs(x-my_number))


