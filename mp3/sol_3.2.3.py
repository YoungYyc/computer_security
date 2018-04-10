import urllib2 
import sys
from random import*
import re

def get_status(u):
    req = urllib2.Request(u)
    try :
        f = urllib2.urlopen(req)
        print f.code
        return f.code
    except urllib2.HTTPError, e:
        print e.code
        return e.code

def get_C_Inverse(y):
    url = "http://72.36.89.11:9999/mp3/haiyang3/?"

    r = [0]*16
    for j in range(0,16):
        r[j] = randint(0x10,0xFF)

    new_url = url
    i = -1

    while (get_status(new_url) != 404) :
        i = i + 1
        r_block = ""
        for j in range(0,15) :
            r_block = r_block + '%02x' % (r[j]) 
        r_block = r_block + '%02x' % (r[15] ^ i)
        new_url = url + r_block + y
    r[15] = r[15] ^ i
    
    #determine the length of padding
    for n in range(0,15):
        #print n
        r_block = ""
        #concstruct r
        for j in range(0,16):
            if (j == n) :
                r_block = r_block + '%02x' % (r[j] ^ 1) 
            else :
                r_block = r_block + '%02x' % (r[j]) 
        new_url = url + r_block + y
        if (get_status(new_url) != 404) :
            n = n - 1
            break
    n = n + 1
    
    num_padding = 16 - n
    a = [0] * 16 #known 

    #calculate known C^-1
    pad = 0x10
    for j in range(n, 16):
        a[j] = pad ^ r[j]
        pad = pad - 1 
         
    #get rest of the block
    
    #we want the last a_i we know to result in 0x10 padding
    for j in range(n-1 , -1, -1): #j is the index of the next byte to find
        r_block_pre = ""
        r_block_suf = ""    
        a_block = ""
        pad = 0xf
        for i in range (0, 16) :
            if (i > j) :
                r[i] = a[i] ^ pad
                pad = pad -1
        for k in range(0,16):
            if (k < j) :
                r_block_pre = r_block_pre + '%02x' % (r[k])  
            if (k > j) :
                r_block_suf = r_block_suf + '%02x' % (r[k])  
            a_block = a_block + '%02x' % a[k]
        i = -1
        new_url = url
        while (get_status(new_url) != 404):
          i = i+1
          r_block = r_block_pre + '%02x' % (r[j] ^ i) + r_block_suf
          print a_block
          print hex(int(r_block,16)^int(a_block,16))
          new_url = url + r_block + y
          print r_block_suf
          print new_url
        r[j] = r[j] ^ i
        a[j] = r[j] ^ 0x10 

    out = "" #return value
    for i in range(0,16) :
        out = out +'%02x' % (a[i]) 
    return out
       
 
 #start of main function
with open(sys.argv[1]) as cipher_text:
	cipher_blocks = cipher_text.read().strip() 
with open(sys.argv[2], "w+") as output:	
    IV = cipher_blocks[0:32]
    y_previous = IV
    num_blocks = len(cipher_blocks) / 32
    for i in range (1, num_blocks) :
        y_curr = cipher_blocks[32*i:32*(i+1)]
        y_inv_curr =  get_C_Inverse(y_curr) 
        x_curr = int(y_previous,16) ^ int(y_inv_curr,16)
        x_curr_hex = '%032x' % x_curr
        #strip padding
        if (i == num_blocks -1) :
            j = 15
            temp = list(x_curr_hex)
            while (temp[2*j:2*j+2] != ['1','0']):
                temp = temp[:-2]
                j = j - 1
            temp = temp[:-2]
            x_curr_hex  = "".join(temp)
        output.write(x_curr_hex.decode("hex"))
        y_previous = y_curr
