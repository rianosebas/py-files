def readFile(name):
  with open(name, "r", errors="ignore", encoding="utf-8") as file:
   return file.read()



def wordCount(text):
    return len(text.split())

def uniqueWordCount(text):
  # return count
  return 0

def findContent(text, word):
  # return count
  return 0