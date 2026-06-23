import numpy as np

# create array

nums = np.array([1,2,3,4,5])
print(nums)
print(type(nums))

print(nums.shape) # size of array
print(nums.dtype) # data type of element in cell

#int64 - 64 bit integer for 1 cell

# data type of array

nums = np.array([1,2,3,4,5], dtype=np.float32)
print(nums)
print(nums.shape)
print(nums.dtype)

# двомірний масив (таблиця.матриця)
nums = np.array(
    [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
)

print(nums)
print(nums.shape)
print(nums.dtype)

#don't use loop "for"
# use numpy functions


# creating and size
nums_list = [1,2,3,4]

nums = np.array(nums_list)

# range
nums = np.arange(10, 20, 2)
print(nums)

#array of 0/1 or random numbers -> create with rule

nums = np.zeros((6,)) # size in tuple
print(nums)

nums = np.ones((5,3)) # 3 column and 5 rows
print(nums)

nums = np.random.rand(2, 3) # size in tuple
print(nums)
print(nums.dtype)

# change size and type
nums = np.arange(12)
print(nums)
print(nums.shape)
print(nums.dtype)

new_nums = nums.reshape(3, 4) # we need to keep the size
print(new_nums)
print(nums.shape)
print(nums.dtype)

nums_float16 = nums.astype(np.float16)
print(nums_float16)
print(nums_float16.shape)
print(nums_float16.dtype)

#перенаповнення
# int 8 = -128 .. 127
nums = np.array([10,20,30, 120], dtype=np.int8)
print(nums)

# increase all to 10

nums = nums +10
print(nums) # [  20   30   40 -126]

#indexes
nums = np.array([10,20,30,40,50])
print(nums[0]) # 10
print(nums[3]) # 40
print(nums[-1]) # 50 last
print(nums[-3]) #30 3rd from last
print(nums[1:4]) # 20, 30, 40 -> slice

# indexes of matrix

nums = np.arange(12).reshape((4,3))
print(nums)

# rows, columns
#nums[index row, index column]

print(nums[1,2])  # 5 row 1, col 2
print(nums[3]) #all  3rd row
print(nums[0:2]) # first two rows
print(nums[:,1]) # all rows, 1 column
print(nums[:, 1:3]) # 2  last columns
print(nums[1:3, 0:2]) # 2 rows, 2 columns

# base operations

nums1 = np.array([1,2,3])
nums2 = np.array([4,5,6])

print(nums1 + 10) # add to each element
print(nums1*nums2) # multiply element wise

# bool masks

nums = np.array([15, 8, 17, 18, 1, 2, 3])
print(nums> 10) # [ True False  True  True False False False] masks

# get elements by mask
mask = nums> 10
print(nums[mask])

# all element by mask increase X2
nums[mask] *= 2
print(nums)

# all elements by mask change on -1
nums[mask] = -1
print(nums)

