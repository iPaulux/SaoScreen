import os
import glob
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

"""
listeEP = glob.glob(r"F:\ProgramFiles\my_bot\screen\test\*.jpg")
print(listeEP)
n=0


listeEP.sort(key=natural_keys)
""" 

n=0
ep = 98
n=0
os.rename(r'F:\ProgramFiles\my_bot\screen\ep{}'.format(ep),r'F:\ProgramFiles\my_bot\screen\test')
os.rename(r'F:\ProgramFiles\my_bot\screen\temp',r'F:\ProgramFiles\my_bot\screen\ep{}'.format(ep))
listeEP = glob.glob(r"F:\ProgramFiles\my_bot\screen\test\*.jpg")
listeEP.sort(key=natural_keys)
    
for el in listeEP:
    os.rename(el,r'F:\ProgramFiles\my_bot\screen\ep{}\{}.jpg'.format(ep,n))
    n+=1
os.rename(r'F:\ProgramFiles\my_bot\screen\test',r'F:\ProgramFiles\my_bot\screen\temp')
    
