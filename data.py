from youtubesearchpython import ChannelsSearch
import time

data_output = open("data.txt")
list_id = data_output.readlines()

data_input = open("data.txt", "a")

request = input("Введите запрос-> ")
depth = int(input("Введите глубину(1-3600)-> "))

start_time = time.time()

search = ChannelsSearch(request, limit = 20, region='UK') #, region='US'

for i in range(depth):
	results = search.result()
	search.next()

	for result in results['result']:
		if result['id']+'\n' in list_id:
			continue
		
		list_id.append(result['id']+'\n')
		data_input.write(result['id']+'\n')

	print("  Progress {:2.2%}".format(i / depth), end="\r")

data_input.close()

print("Время выполнения: "+str(time.time()-start_time)+"s.")