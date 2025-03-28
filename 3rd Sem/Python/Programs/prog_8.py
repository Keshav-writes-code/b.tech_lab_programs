import random

# Input password length
print("\nRandom Password Generator")
length = int(input("\nEnter length: "))

# Define characters for the password
chars = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9,!,@,#,$,%,^,&,*,(,)"

print("\nGenerating Random password using:\n", chars)

# Generate a random password
rand_pass = ''.join(random.choice(chars.split(',')) for _ in range(length))

print("\nYour Password:", rand_pass)
