def main():
    ##################################################
    # Comlete your code here
    ##################################################

    numM = int(input('Please enter the number of males in the class.')) 
    numF = int(input('Please enter the number of females in the class.')) 
    total = int(numM + numF)
    percM = float(numM / total * 100) 
    percF = float(numF/ total * 100)
    print ('The total number of students:', total)
    print ('The number of males and females:', numM, numF)
    print (f'The percentage of males and females: {percM:.2f} {percF:.2f}')

    pass


if __name__ == '__main__':
    main()
