def split_num(num,output=[],divider=1024.0):
    remainder = 0.0
    units = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    index = 0
    for unit in units:
        if abs(num) < 1.0:
            break
        if abs(num) < divider:
            output.append({'num': int(num), 'unit': unit})
            if divider == 1024.0:
                remainder = round( (num - int(num)) * 2**(index*10) )  # when 1 kB = 1024 B
            elif divider == 1000.0:
                remainder = round( (num - int(num)) * 10**(index*3) )  # When 1 kB = 1000 B
            else:
                print('I only know what to do with divider = 1024.0 or 1000.0')
                remainder = 0
            output = split_num(remainder,output=output,divider=divider)
            return output
        num /= divider
        index += 1
    return output

def fmt_num(num,divider=1024.0):
    outputstring = ''
    index = 0
    for thing in split_num(num,output=[],divider=divider):
        if index > 0:
            thing['num'] = abs(thing['num'])
        outputstring += str(thing['num']) + ' ' + thing['unit'] + 'B '
        index += 1
    # outputstring += '\n'
    return outputstring
