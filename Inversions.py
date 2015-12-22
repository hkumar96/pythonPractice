#Counting the number of inversions

def merge(arr,left,right):
	inv=0
	mid=(left+right)/2
	i=left
	j=mid
	temp=[]
	while i<mid and j<=right:
		if arr[i]<=arr[j]:
			temp.append(arr[i])
			i+=1
		else:
			temp.append(arr[j])
			j+=1
			inv+=mid-i
	while i<mid:
		temp.append(arr[i])
		i+=1
	while j<=right:
		temp.append(arr[j])
		j+=1
	for i in range(len(temp)):
		arr[i]=temp[i]
	return inv
def count_inversion(arr,left,right):
	inv=0
	if left<right:
		mid=(left+right)/2
		inv+=int(count_inversion(arr,left,mid))
		inv+=int(count_inversion(arr,mid+1,right))
		inv+=int(merge(arr,left,right))
	return inv;
arr=[2,3,57,8,64,5]
end=len(arr)-1
print count_inversion(arr,0,end)