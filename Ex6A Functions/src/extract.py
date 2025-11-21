
def location(block):
    # Your code here
    sta = (block.find(' ',10)) 
    en = (block.find(' END')) -1
    string = ( block[en:sta:-1])
    string = string.capitalize()
    sente = ''
    i = 0
    while i < len(string):
        if string[i] == ' ':
            sente = sente + string[i] + string[i+1].upper()
            i = i + 2
        else:
            sente = sente + string[i]
            i = i +1
    return sente

def temperature(block):
    # Your code here
    sta = (block.find(' ',5)) +1
    en = block.find('_')
    return float( block[sta:en:])


def x_coordinate(block):
    # Your code here
    sta = (block.find(':')) +1
    en = block.find(',')
    return ( block[sta:en:])


def y_coordinate(block):
    # Your code here
    sta = (block.find(',')) +1
    en = block.find(' ',10)
    return ( block[sta:en:])


def pressure(block):
    # Your code here
    sta = (block.find('_')) +1
    en = block.find(':')
    return float( block[sta:en:])


def get_block(data):
    # Your code here
   sat = data.find('BEGIN')
   en = (data.find('END')) + 3
   return ( data[sat:en])

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
