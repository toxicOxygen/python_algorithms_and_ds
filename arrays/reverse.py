def reverse(arr):
  start_index = 0
  end_index = len(arr) - 1

  while start_index < end_index:
    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]

    start_index += 1
    end_index -= 1
  
  print(arr)


if __name__ == "__main__":
  mArr = [1,2,3,4,5]
  reverse(mArr)