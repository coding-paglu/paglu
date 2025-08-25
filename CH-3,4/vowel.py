word=input("Enter a word:")
for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        print(i,"is a vowel")
    elif i in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
        print(i,"is a consonant")
    elif i==' ':
        pass
    else:
        print(i,"is not a letter")
