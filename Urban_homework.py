import types
def flat_list_sum(list_):
  #Если передан список/кортеж, то раскрываем
  if isinstance(list_, list|tuple):

    if len(list_) == 0:
      return 0  #Если дошли до конца, вернуть ноль

    if isinstance(list_[0], int|float): #Если элемент списка число/булево, возвращаем его и идем дальше
      return list_[0] + flat_list_sum(list_[1:])

    if isinstance(list_[0], str): #Если элемент списка строка, возвращаем ее длину и идем дальше
      return len(list_[0]) + flat_list_sum(list_[1:])

    if isinstance(list_[0], list|tuple): #Если элемент списка список или кортеж - раскрываем его и смотрим дальше
      return flat_list_sum(list_[0]) + flat_list_sum(list_[1:])

    if isinstance(list_[0], set): #Если элемент списка множество - перевести в список, раскрыть его и смотрим дальше
      return flat_list_sum(list(list_[0])) + flat_list_sum(list_[1:])

    if isinstance(list_[0], dict):
      key_sum, value_sum = 0, 0
      for key, value in list_[0].items():
        key_sum += flat_list_sum(key)
        value_sum += flat_list_sum(value)
      return key_sum + value_sum + flat_list_sum(list_[1:])
    else: return 0 #Для типа данных None (если часть списка)

  #Если передано число/строка/словарь, то считаем и выдаем.
  #Если множетсво, то в словарь и раскрываем
  if isinstance(list_, int|float): #Если элемент число/булево, возвращаем его
    return list_

  if isinstance(list_, str): #Если элемент строка, возвращаем ее длину
    return len(list_)

  if isinstance(list_, dict): #Если словарь, то считаем его
    key_sum, value_sum = 0, 0
    for key, value in list_.items():
      key_sum += flat_list_sum(key)
      value_sum += flat_list_sum(value)
    return key_sum + value_sum

  if isinstance(list_, set): #Если элемент множество - перевести в список, раскрыть его и смотрим дальше
    return flat_list_sum(list(list_))
  else: return 0 #Для типа данных None

print(flat_list_sum([1,2,[3,4]]))