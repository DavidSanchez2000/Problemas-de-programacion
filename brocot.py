from sys import stdin

# Problema #10077 stern-brocot tree

def solve(m,n):
	res = ""
	mc, nc = 1, 1
	ml, nl = 0, 1
	mr, nr = 1, 0

	while mc != m or nc != n:
		if m *nc > n* mc:
			ml, nl = mc, nc
			res += "R"
		else:
			mr, nr = mc, nc
			res += "L"
		mc, nc = ml+mr, nl + nr
	print(res)




def main():
	while True:
		m,n = list(map(int, input().split()))
		if m == n == 1:
			break
		solve(m,n)
main()