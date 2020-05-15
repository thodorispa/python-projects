def save_to_file(keys,values):

    path = '/Users/thodorispachis/Desktop/'
    final = dict(zip(keys,values))

    f = open(path + 'dict.txt', 'w+')
    f.write(str(final))

keys = str(input('Please provide keys of dictionary, hit Enter.')).split(' ')

values = str(input('Now provide values in accordance of keys, hit Enter.')).split(' ')

save_to_file(keys,values)
