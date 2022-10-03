#Найти программу, которая найдёт произведение пар чисел списка.
#Парой является первый и последний элемент, второй и последний и тд

import random

n = int(input('Введите N: '))

lst = []#создаём список
for i in range(1, n + 1): 
    lst.append(random.randint(1,10))#добавляем рандомные значения в диапазоне
print(lst)

lstNew = []#создаём новый список либо чётный либо нечётный

if (len(lst) %2 == 0):
    nNew =len(lst) / 2 
for i in range(1, len(lst)//2 + 1):
    new_lst = [lst[i]*lst[len(lst)-i-1]]
print(new_lst)


int[] pairs;//новый массив либо чётный либо нечётный
if (numbers.Length % 2 == 0)
{
    pairs = new int [numbers.Length / 2];//чётный
}
else
{
    pairs = new int [numbers.Length / 2 + 1];//нечётный
    pairs[pairs.Length - 1] = numbers[numbers.Length / 2];//число без пары в последний элемент массива(по умолчанию ноль)
}


for (int i = 0; i < numbers.Length / 2; i++)
    {
       pairs[i] = numbers[i] * numbers[numbers.Length -1 -i];
    }
PrintArray(pairs);



void FillArrayRandomNumbers(int [] array)// рандом числа в массив
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(0, 5);
    }
}

void PrintArray(int[] array)//вывод массива на экран
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
Console.WriteLine();
}

int ReadInt(string message)
{
    Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}