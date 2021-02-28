# this is not an in-place algorithm
def find_duplicate(n):
  d = {}

  for c in n:
    d[c] = d.get(c, 0) + 1
  
  for k,v in d.items():
    if v > 1:
      print(k)

# this is an in place algorithm
# this only works for positive numbers where no 
# element is longer than the length of array
def duplicates(nums):

  for n in nums:
    if nums[abs(n)] >= 0:
      nums[abs(n)] *= (-1)
    else:
      print(f"repetition found, {abs(n)}")

if __name__ == "__main__":
  l = [1,2,3,2,4,5,1]
  duplicates(l)