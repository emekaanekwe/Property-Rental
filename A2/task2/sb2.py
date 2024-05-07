train = "17204,Wallan Railway Station (Wallan),-37.416861,145.0053723"

id = train[0:5]

def info(text):
    id = text[0:5]
    #eparate text into commas
        #extract text from each index
    trains = {'stop_id':0, 'stop_name': 0, 'stop_lat':0, 'stop_lon':0}
    train_dic = {id: trains}
    
'''
parts = train.split(',')

# Creating a dictionary
train_dict = {
    "code": parts[0],
    "station_name": parts[1],
    "latitude": float(parts[2]),
    "longitude": float(parts[3])
}
'''

train_data = {}

# Split the string into elements using comma as delimiter
def convert(filename):
    with open(filename, 'r') as csvfile:
        for line in csvfile:
            line = line.strip()
            train_stops = line.split(',')
            train_data[train_stops[0]] = train_stops[line]
    print(train_data)
    
filename = 'A2/task2/train_stations.csv'
result = convert(filename)
print(result)