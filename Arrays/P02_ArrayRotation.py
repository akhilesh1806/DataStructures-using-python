# Author: AKHILESH SANTOSHWAR

# Python program to cyclically rotate
#an array by one
# Method for rotation
def rotate(A, n):
   x = A[n - 1]
   for i in range(n - 1, 0, -1):
      A[i] = A[i - 1];
   A[0] = x;
# Driver function
A=list()
n=int(input("Enter the size of the List ::"))
print("Enter the Element of  List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
print ("The array is ::>")
for i in range(0, n):
   print (A[i], end = ' ')
rotate(A, n)
print ("\nRotated array is")
for i in range(0, n):
   print (A[i])

    # OUTPUT:
    # Enter size: 10
    # Enter Elements : 0 1 2 3 4 5 6 7 8 9
    # Before Rotation: 0 1 2 3 4 5 6 7 8 9
    # After Rotation: 3 4 5 6 7 8 9 0 1 2
