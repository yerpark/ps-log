import sys

if __name__ == "__main__":
    n, m  = map(int, sys.stdin.readline().split())
    no_listen = set()
    no_listen_no_see = set()

    for _ in range(n):
        no_listen.add(sys.stdin.readline().strip())
    
    for _ in range(m):
        tmpStr = sys.stdin.readline().strip()
        if (tmpStr in no_listen):
            no_listen_no_see.add(tmpStr)

    no_listen_no_see_sort = sorted(no_listen_no_see)

    print(len(no_listen_no_see_sort))
    for i in range(len(no_listen_no_see_sort)):
        print(no_listen_no_see_sort[i])
    
        