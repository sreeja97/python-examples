if __name__ == '__main__':

    filename = 'myfile.txt'
    with open(filename, 'w') as f:
        f.write('this is my file\n') # creating or deleting and creating a new file and then writing
        f.write(' this is another line in my file\n')
        f.write('this is next line\n')


    with open(filename, 'r') as f:
        print(f.read()) # reading
        print(f.tell()) 
        f.seek(0)  #resetting curr position
        print(f.tell())
        print(f.readlines())

    with open(filename, 'a') as f:
        f.writelines('this is my file\n') #appending
        f.writelines(' this is another line in my file\n')
        f.writelines('this is next line\n')

    with open(filename, 'r') as f:
        print(f.read())
        print(f.tell())
        f.seek(0)
        print(f.tell())
        print(f.readlines())



