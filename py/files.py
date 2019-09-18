from pathlib import Path
import random
import time

Path = Path('../files/read_file.txt')
if Path.exists():
    print('Path exists')
    file = open(Path, 'r')  # открытие файла для чтения
    print(file.read())
else:
    print('Oopsie')
file = open(Path, 'r')
for line in file:
    print(line + '1')
file.close()  # закрытие файла

genIndex = 0
numIndex = []
genTime = []
while genIndex < 15:
    rand = random.randrange(-1000, 1000)
    timeRand = random.randrange(3.0)
    numIndex[genIndex:genIndex + 1] = [rand]
    genTime[genIndex:genIndex + 1] = [timeRand]
    print(f'index[{genIndex}] =  {numIndex[genIndex]}')  # вывод значений по индексам
    time.sleep(timeRand)
    print(f'Time[{genIndex}] = {genTime[genIndex]} second(s)')
    genIndex += 1
    if genIndex >= 15:
        fileWrite = open('../files/genTest.txt', 'w')
        fileWrite.write(f'Full index = {numIndex}' + '\n')
        numIndex.sort()
        index = (f'Sorted index = {numIndex}' + '\n' + f'Full time = {genTime}' + '\n' + 'Time summary = ' +
                 str(sum(genTime)) + ' seconds' + '\n')
        fileWrite.write(index)
        fileWrite.write('End')
        fileWrite.close()
testVar = [str(i) + str(i - 1) for i in range(20)]  # генерация списка
print(testVar)
fileWrite2 = open('../files/genTest2.txt', 'w')
for i in testVar:
    fileWrite2.write(i + '\n')
fileWrite2.close()
