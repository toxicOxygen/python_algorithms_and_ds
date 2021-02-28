def anagram(word1, word2):
  if len(word1) != len(word2):
    return False

  word1 = word1.lower()
  word2 = word2.lower()

  s1 = sorted(word1)
  s2 = sorted(word2)
  
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      return False

  return True



if __name__ == "__main__":
  w1 = "restful"
  w2 = "fluster"

  print(anagram(w1,w2))