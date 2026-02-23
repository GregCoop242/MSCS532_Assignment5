import random
import time



# Quick Sort Implementation with Random Pivot Selection
def quick_sort_r(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr) # Choosing a random pivot to improve performance on sorted and reverse sorted arrays
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    return quick_sort_r(low) + equal + quick_sort_r(high)

#deterministic quick sort Impmlementation
def quick_sort_d(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # Choosing the middle element as the pivot
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    return quick_sort_d(low) + equal + quick_sort_d(high)



def create_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def create_sorted_array(size):
    return list(range(1, size + 1))


def create_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def create_repeating_elements_array(size):
    return [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]

def call_and_time_quick_sort(num_elements):
 
    start = time.time()
    random_array_r = quick_sort_r(create_random_array(num_elements))
    end = time.time()
    random_array_r_time = end - start
  
    start = time.time()
    empty_array_r = quick_sort_r([])
    end = time.time()
    empty_array_r_time = end - start

    start = time.time()
    sorted_array_r = quick_sort_r(create_sorted_array(num_elements))
    end = time.time()
    sorted_array_r_time = end - start

    start = time.time()
    reverse_sorted_array_r = quick_sort_r(create_reverse_sorted_array(num_elements))
    end = time.time()
    reverse_sorted_array_r_time = end - start

    start = time.time()
    repeated_array_r = quick_sort_r(create_repeating_elements_array(num_elements))
    end = time.time()
    repeated_array_r_time = end - start
 
  
    start = time.time()
    random_array_d = quick_sort_d(create_random_array(num_elements))
    end = time.time()
    random_array_d_time = end - start
 
    start = time.time()
    empty_array_d = quick_sort_d([])
    end = time.time()
    empty_array_d_time = end - start
 
    start = time.time()
    sorted_array_d = quick_sort_d(create_sorted_array(num_elements))
    end = time.time()
    sorted_array_d_time = end - start
 
    start = time.time()
    reverse_sorted_array_d = quick_sort_d(create_reverse_sorted_array(num_elements))
    end = time.time()
    reverse_sorted_array_d_time = end - start
 
    start = time.time()
    repeated_array_d = quick_sort_d(create_repeating_elements_array(num_elements))
    end = time.time()
    repeated_array_d_time = end - start
 

   #Table of Results
    print("\nSummary of Execution Times:")
    print("--------------------------------")
    print(f"{'Test Case':<30} {'Random Pivot (s)':<20} {'Deterministic Pivot (s)':<25} {'Number of Elements':<20} {num_elements:<20}")
    print(f"{'-'*30} {'-'*20} {'-'*25}")
    print(f"{'Random Array':<30} {random_array_r_time:.10f}          {random_array_d_time:.10f}")
    print(f"{'Empty Array':<30} {empty_array_r_time:.10f}          {empty_array_d_time:.10f}")
    print(f"{'Sorted Array':<30} {sorted_array_r_time:.10f}          {sorted_array_d_time:.10f}")
    print(f"{'Reverse Sorted Array':<30} {reverse_sorted_array_r_time:.10f}          {reverse_sorted_array_d_time:.10f}")
    print(f"{'Repeating Elements Array':<30} {repeated_array_r_time:.10f}          {repeated_array_d_time:.10f}")
    print("--------------------------------")





if __name__ == "__main__":

   call_and_time_quick_sort(10)
   call_and_time_quick_sort(100)  
   call_and_time_quick_sort(1000)
   call_and_time_quick_sort(10000)
   call_and_time_quick_sort(1000000)