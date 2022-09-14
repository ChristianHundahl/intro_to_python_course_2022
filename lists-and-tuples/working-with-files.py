#Create a file and call it lyrics.txt (it does not need to have any content)

#Create a new file and call it songs.docx and in this file write 3 lines of text to it.
songs = open('songs.txt', 'w')
songs.write('I can\'t explain you would not understand\nThis is not how I am\nI have become comfortably numb\n')
songs.close()

#Open and read the content and write it to your terminal window. 
# * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).
songs = open('songs.txt')
print(songs.read()) #Reads all of file

songs = open('songs.txt')
print(songs.readline()) #Reads first line of file

songs = open('songs.txt')
print(songs.readlines()) #Puts each line into a list