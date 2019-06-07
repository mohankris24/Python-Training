# Read text file and reformat (using Functions)
date_var = ' '
date_yyyy = ' '
date_dd = ' '
date_mm = ' '
line_var = ' '
date_format = ' '


def move_dates(date_var):
    '''
    Convert date format from MM-DD-YYYY to YYYYMMDD
    :param date_var:
    :return: YYYYMMDD format --> date_format variable
    '''
    date_yyyy = date_var[2]
    date_dd = date_var[1]
    date_mm = date_var[0]
    date_format = date_yyyy + date_mm + date_dd
    return date_format

with open(r"C:\Users\mohan\Desktop\Python Files\Test1.txt", mode='r+') as test_file:
    # read_file = test_file.readlines().split()
    for read_line in test_file:
        # store read_line into list
        line_var = read_line.split(',')
        date_var = line_var[2].split('-')
        # date_yyyy = date_var[2]
        # date_dd = date_var[1]
        # date_mm = date_var[0]
        # date_format = "%s-%s-%s" % (date_yyyy, date_mm, date_dd)
        # date_format = date_yyyy + date_mm + date_dd
        line_var[2] = move_dates(date_var)
        date_var = line_var[3].replace('\n', '').split('-')
        line_var[3] = move_dates(date_var)
        line_var.append('')
        line_var.append('')
        line_var.append('')
        line_var[4] = line_var[2]
        line_var[6] = line_var[3]
        line_var[2] = line_var[1]
        line_var[3] = ','
        line_var[1] = ','
        line_var[5] = ','
        with open(r"C:\Users\mohan\Desktop\Python Files\Test2.txt", mode='a') as test_write:
            write_file = test_write.writelines(line_var)
            test_write.write('\n')
K=2
# Functions

