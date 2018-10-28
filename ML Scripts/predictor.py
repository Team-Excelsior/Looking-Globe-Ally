def predict(argv):
    mm = open('zika_map.txt')
    arr_vm = mm.readline().split(' ')

    lat_offset = 180
    long_offset = 179

    lat = argv[0]
    long = argv[1]

    lat = (float(lat)*2) + lat_offset
    long = float(long) + long_offset

    return min(float(arr_vm[int(long*360 + lat)]), 1.0)


