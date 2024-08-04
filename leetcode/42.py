height = [0,1,0,2,1,0,1,3,2,1,2,1]

stack = []
vol = 0

for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
        top = stack.pop()

        if not stack:
            break

        dist = i - stack[-1] - 1
        water = min(height[i],height[stack[-1]]) - height[top]

        vol += dist*water
    stack.append(i)

print(vol)