def merge_list(list1, list2):
    # Check if both inputs are lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs should be lists.")
    
    # Check if elements in the lists are integers
    for item in list1 + list2:
        if not isinstance(item, int):
            raise TypeError("Lists should only contain integers.")
    
    merged_list = []
    i = 0
    j = 0
    
    # Merge the two lists while maintaining sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Add any remaining elements from list1 and list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list
