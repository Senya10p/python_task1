# первое задание
# date = input('Введите дату: ')
# task = input('Введите задачу: ')
# print(date + ' ' + task)

# второе задание
# tasks = []
# i = 1
# while i <= 3:
#   tasks.append(
#     {
#       'date':input('Введите дату: '),
#       'task':input('Введите задачу: '),
#     }
#   )
#   i+=1
  
# for task in tasks:
#   print(task['date'] + ' ' + task['task'])

# третее задание
tasks = {}
i = 1
while i <= 3:
  date = input('Введите дату: ')
  task = input('Введите задачу: ')
  tasks[date] = task
  i+=1