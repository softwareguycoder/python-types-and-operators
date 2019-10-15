def main():
    x = []
    for i in range(26):
        x.append(i)
        
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    dict = {}
    for i in range(26):
        dict[letters[i]]=x[i]
        
        
    with open("/home/mypairs-inorder.txt", "w") as f:
        for letter in letters:
            f.write("'{0}': {1}\n".format(letter, dict[letter]))
        
        
    with open("/home/mypairs-reversed.txt", "w") as f:
        for letter in letters[::-1]:
            f.write("'{0}': {1}\n".format(letter, dict[letter]))
        

if __name__=="__main__":
    main()
