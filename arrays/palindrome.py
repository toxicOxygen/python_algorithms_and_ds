def palindrome(word):
  start_index = 0
  end_index = len(word) - 1

  word = word.lower()

  while start_index < end_index:
    if word[start_index] != word[end_index]:
      return False
    
    start_index += 1
    end_index -= 1
  return True


if __name__ == "__main__":
  words = ["test",'radar','madam','scan']

  for word in words:
    print(palindrome(word))