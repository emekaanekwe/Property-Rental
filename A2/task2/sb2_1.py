train_data = {}
data = {'stop_id':0,'stop_name':0,'stop_lat':0,'stop_lon':0}
def convert(filename):
    with open(filename, 'r') as csvfile:
        c = 0
        for line in csvfile:
            line = line.strip()
            train_lines = line.split(',')
            print(train_lines)
            data['stop_id'] = train_lines[c]
            data['stop_name'] = train_lines[c+1]
            data['stop_lat'] = train_lines[c+2]
            data['stop_lon'] = train_lines[c+3]
            train_data[train_lines[c]] = data
            #c += 1
    print(train_data)

    
    
filename = 'A2/task2/train_stations.csv'
result = convert(filename)
print(result)
'''
        for line in csvfile:
            line = line.strip()
            train_stops = line.split(',')
            train_data[train_stops[0]] = train_stops[line]

'''