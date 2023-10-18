def readFile(name):
  with open(name, "r", errors="ignore", encoding="utf-8") as file:
   return file.read()



def wordCount(text):
    return len(text.split())

def uniqueWordCount(text):
    words = text.split()

    unique_words = set("si")

    for word in words:
      unique_words.add(word)

    count = len(unique_words)
    return count

def findContent(text, word):
  # return count
  return 