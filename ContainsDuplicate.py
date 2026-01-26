



def contains_duplicate(nums: List[int]) -> bool:
    if(len(nums) != len(set(nums))): 
        print("False")
        return False
    else: 
        print("True")
        return True

if __name__ == "__main__":
    raise SystemExit(contains_duplicate([1,2,3,1]))
