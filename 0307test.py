data=[]
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))

sum_len = 0
for d in data:
	sum_len += len(d)

print(sum_len)
print('總平均為', sum_len/len(data),'筆資料')

print(data[0])
print(len(data[0]))

new = []
for e in data:
	if 'good' in e:
		new.append(e)

print(len(new)) 