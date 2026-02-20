import sys

if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()

    for line in input_data:
        if line == '0':
            break

        data = list(map(int, line.split()))
        n = data[0]
        heights = data[1:]

        heights.append(0)
        stack = []
        max_area = 0

        for i in range(n + 1):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                w = i if not stack else i - stack[-1] - 1

                if max_area < h * w:
                    max_area = h * w
            stack.append(i)

        print(max_area)