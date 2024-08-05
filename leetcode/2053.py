from collections import Counter

def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        order_arr = []

        for v in arr:
            if v in counter and counter[v] is 1:
                order_arr.append(v)
        
        return order_arr[k-1] if k <= len(order_arr) else ""