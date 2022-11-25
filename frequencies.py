f1 = open('articles/2001.txt','r') #file 1
f2 = open('articles/positive.txt','r') #file 2

file_list = [f1, f2] # This would hold all your open files
num_files = len(file_list)

frequencies = {} # We'll just make one dictionary to hold the frequencies

for i, f in enumerate(file_list): # Loop over the files, keeping an index i
    for line in f: # Get the lines of that file
        for word in line.split(): # Get the words of that file
            if not word in frequencies:
                frequencies[word] = [0 for _ in range(num_files)] # make a list of 0's for any word you haven't seen yet -- one 0 for each file

            frequencies[word][i] += 1 # Increment the frequency count for that word and file

if 
print (frequencies)