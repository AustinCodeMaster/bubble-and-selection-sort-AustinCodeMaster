def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)-1,0,-1):
         for j in range(i):
              if unsorted_list[j]>unsorted_list[j+1]:
                   temp=unsorted_list[j]
                   unsorted_list[j]=unsorted_list[j+1]
                   unsorted_list[j+1] = temp
                   
                   print(unsorted_list)
# Define the list to be sorted
unsorted_list =[5,3,8,6,7,2]
bubble_sort(unsorted_list)
print(unsorted_list)