#
#     Написать генератор, который принимает список списков, и возвращает их плоское представление. Например
#
# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f'],
# 	[1, 2, None],
# ]
# for item in  flat_generator(nested_list):
# 	print(item)

def flat_generator(list_: list):
	i = -1
	k = -1
	while True:
		if len(list_) == i+1:
			break
		i += 1
		while True:
			if len(list_[i]) == k+1:
				k = -1
				break
			k += 1
			yield list_[i][k]


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
for item in flat_generator(nested_list):
	print(item)
