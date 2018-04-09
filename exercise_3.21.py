N=1000
k=5
gamma=0.9
v=[[0. for _ in range(k)] for _ in range(k)]
A=[[0,1],[4,1]]
B=[[0,3],[2,3]]
for t in range(N):
	for i in range(k):
		for j in range(k):
			if [i,j]==A[0]: 
				r=10
				v[i][j]=(r+gamma*v[A[1][0]][A[1][1]]) 
				continue
			elif [i,j]==B[0] : 
				r=5
				v[i][j]=(r+gamma*v[B[1][0]][B[1][1]])
				continue
			rew=[0.]*4
			for a in range(4):
				#a=0,1,2,3 stands for up,right,down,left respectively.
				r=0
				pos=[i,j]
				if a==0:
					if i==0: r=-1
					else: pos=[i-1,j]
				elif a==1:
					if j==k-1: r=-1
					else: pos=[i,j+1]
				elif a==2:
					if i==k-1: r=-1
					else: pos=[i+1,j]
				elif a==3:
					if j==0: r=-1
					else: pos=[i,j-1]
				rew[a]=r+gamma * v[pos[0]][pos[1]]
			v[i][j]=max(rew)

	print(t,'-->',v)

print('res:',v)