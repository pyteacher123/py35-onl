import sys
from db_gateway import DbGateway
from dao import CountryDAO


ALLOWED_FLAGS = ('-d', '-n')


if __name__ == '__main__':
    args = sys.argv[1:]
    for index in range(0, len(args), 2):
        flag = args[index]
        if flag not in ALLOWED_FLAGS:
            raise ValueError('Invalid flag')
        elif flag == '-d':
            db_name = args[index + 1]
        elif flag == '-n':
            records_number = int(args[index + 1])
        
        print("Records generating started.")
        db_gate = DbGateway(db_name=db_name)
        
