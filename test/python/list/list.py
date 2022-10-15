#!/usr/bin/env python3

myList = []

myList.append("https://boyinblue.github.io")
myList.append("https://blog.naver.com/boyinblue")

for id in range(len(myList)):
  print("URL[{}] : {}".format( id, myList[id]))
