#function definition of the function to find maximum in k size subarrays
def kMax(arr,k):
	i=0
	end=len(arr)
	#dequeue implementation using a list
	dequeue=[]
	#analyze the first k-size windows 
	while i<k:
		#pop out all the useless element from back that are smaller than current element
		while len(dequeue)!=0 and arr[i]>=arr[dequeue[len(dequeue)-1]]:
			dequeue.pop()
		#push the new element at the back
		dequeue.append(i)
		i+=1
	while i<end:
		print arr[dequeue[0]]
		#remove the elements from the front that are not in current k-size window
		while len(dequeue)!=0 and dequeue[0]<=i-k:
			#to implement remove from front first reverse and the remove from back and then again reverse
			dequeue.reverse()
			dequeue.pop()
			dequeue.reverse()
		#pop out all the useless element from back that are smaller than current element
		while len(dequeue)!=0 and arr[i]>=arr[dequeue[len(dequeue)-1]]:
			dequeue.pop()
		dequeue.append(i)
		i+=1
	print arr[dequeue[0]]

kMax([8, 5, 10, 7, 9, 4, 15, 12, 90, 13],4)