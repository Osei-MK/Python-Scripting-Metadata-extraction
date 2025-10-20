'''
week 5
'''
# 3rd party libraries 
import itertools 
import pickle 
import hashlib

# password lengths 
charset   = 'abc123&'
minlength = 4 
maxlength = 7

rainbow_table =  {}

print("Create Rainbow table")


for length in range( minlength, maxlength + 1):
    for combo in itertools.product(charset, repeat = length):
        password = ''.join (combo)
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        rainbow_table[password] = md5_hash
        
        
    #S the rainbow\file 
with open ('rainbow.db' , 'wb') as f:
    pickle.dump(rainbow_table, f)
    
    #entries for each one
    sorted_hashes = sorted(rainbow_table.items())
    
    #first
    print("\nFirst 5 entries:")
    print(f"{'Password':<35} {'HASH'}")
    print("=" * 50)
    for h, pwd in sorted_hashes[:5]:
        print(f"{h:<35} {pwd}")
        
     #last   
    print("\nLast 5 entries:")
    print(f"{'Password':<35} {'HASH'}")
    print("=" * 50)
    for h, pwd in sorted_hashes[-5:]:
        print(f"{h:<35} {pwd}")
        
    print(f"passwords hash: {len(rainbow_table)}") 
    print(f"\nRainbow Size: {len(rainbow_table)}")