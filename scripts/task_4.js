/*
Задача 4 (Для языка JavaScript):
Имеются 2 функции которые выполняются асинхронно. С использованием Promise и/или Asinc/Await реализовать вывод в консоль:
- Суммарный результат обеих функций.
- Последовательный вывод сначала 1 функции затем 2 в независимости от времени выполнения обеих функций (даже если 1я функция выполняется дольше 2й)

Я ранее не изучал JavaScript по этому решил задачу на Python.
При необходимости могу изучить JavaScript(файл task_4.py)
*/

Function F1() {
   setTimeout(() => null, 2000);
   return “Result1”
}
Function F2() {
   setTimeout(() => null, 1000);
   return “Result2”
}
F1() + F2() -> Result1Result2
F1() + F2() -> 
Result1
Result2
