import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

print('Считаем данные из EV_Population.csv и переведем его в датафрейм Pandas.')
df = pd.read_csv('EV_Population.csv')
print('Общая информация о массиве: кол-во строк и столбцов, наличие пропусков данных, тип данных.')
print(df.info())
print()

print('Пропусков данных нет. Перейдем к описанию.')
print('Датафрейм имеет следующие колонки:',
      'State - штат США, где зарегистрирована машина',
      'Model Year - дата изготовления',
      'Make - производитель',
      'Electric Vehicle Type - тип электромобилея',
      'Electric Range - дальность поездки на одной зарядке',
      'Base MSRP - рекомендованная производителем стоимость машины',
      'Legislative District - законодательный округ, где зарегистрирована машина',
      'CAFV Eligibility Simple - упрощенный показатель права на участие машины в программе CAFV (Машина на чистом топливе)',
      sep='\n')
print()

print('Начнем с базового анализа числовых данных')
print(df.describe())
print()

print('Теперь посмотрим на значения категориальных данных:')
print('State:', df['State'].unique())
print('Make:', df['Make'].unique())
print('Electric Vehicle Type:', df['Electric Vehicle Type'].unique())
print('CAFV Eligibility Simple:', df['CAFV Eligibility Simple'].unique())
print()

print('Из полученных данных видно, что колонка State не представляет интереса, т.к. содержит всего одно значение')
print(
    'Теперь посмотрим на соотношение производителей, типов машин и показателей CAFV. Для этого проведем группировку с подсчетом.')
print('По производителям:')
print(df['Make'].value_counts(), '\n')
print('По типам машин:')
print(df['Electric Vehicle Type'].value_counts(), '\n')
print('По показателю CAFV:')
print(df['CAFV Eligibility Simple'].value_counts(), '\n')
print()

print(
    'Теперь посмотрим более сложную статистику. Посмотрим на кол-во соответствий машин требованиям CAFV среди производителей')
print('Для этого произведем двойную агрегацию (по производителю и показателю CAFV)')
print(df.groupby(['Make', 'CAFV Eligibility Simple'])['Model Year'].count().sort_index())
print()

print('Теперь визуализируем все это !!!!!!!!')
print('Первым делом выведем статистику по годам. Это будет:',
      ' - общее кол-во выпущенных машин',
      ' - изменение максимальной дальности пробега',
      ' - рекомендованная производителем стоимость машины', sep='\n')
print()

# ____Далее пойдут графики____
fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(df['Model Year'].value_counts().sort_index().index, df['Model Year'].value_counts().sort_index(), '--g')
ax.bar(df['Model Year'].value_counts().sort_index().index, df['Model Year'].value_counts().sort_index())
ax.set_xticks(df['Model Year'].unique())
ax.set_xticklabels(df['Model Year'].unique(), rotation=90)
ax.set_title('Общее кол-во выпущенных машин (по годам)')
plt.annotate('ВНИМАНИЕ', (0.1, 0.87), xycoords='axes fraction', color='r')
plt.annotate('В пропущенных датах данные о выпуске\nмашин отсутствуют', (0.1, 0.85), xycoords='axes fraction',
             verticalalignment='top')
plt.show()

df_year_range = df.groupby('Model Year')['Electric Range'].max().loc[1999:2024]
df_year_MSRP_max = df.groupby('Model Year')['Base MSRP'].max().loc[1999:2024]
df_year_MSRP_mean = df.groupby('Model Year')['Base MSRP'].mean().loc[1999:2024]
fig, ax = plt.subplots(3, 1, figsize=(13, 13))
ax[0].set_title('Изменение максимального дальности на однйо зарядке по годам (1999-2024)')
ax[0].plot(df_year_range.index, df_year_range)
ax[0].set_ylabel('Максимальная дальность, миль')
ax[0].grid()
ax[1].set_title('Рекомендованная производителем стоимость машины (максимальные значения)')
ax[1].plot(df_year_MSRP_max.index, df_year_MSRP_max)
ax[1].set_ylabel('Стоимость, $')
ax[1].grid()
ax[2].set_title('Рекомендованная производителем стоимость машины (средние значения)')
ax[2].plot(df_year_MSRP_mean.index, df_year_MSRP_mean)
ax[2].set_ylabel('Стоимость, $')
ax[2].grid()
plt.show()

print('По графикам можно сказать следующее:',
      ' - до 2011 выпуск крайне незначительный, затем резкий рост до 2018 года, спад в пандемию и плавный рост (2025 не учитываем)'
      ' - график максимальной дальности имеет странный провал в период 2022-2023 годов',
      ' - в остальном плавное увеличение до 250-200 миль (400-480 км) и далее плато',
      ' - максимальная стоимость имеет всплеск в 2015',
      ' - средняя стоимость имеет всплеск в период 2003-2010',
      ' - сама статистика стоимости очень странная - до 3 квантиля он равен 0 (т.е. 75% значений равны 0)',
      sep='\n')
print()

print('Далее представим обобщенную статистику по кол-ву выпущенных производителями машин и допущенных/недопущенных по программе CAFV среди них')
print('Примечание: учитываются только производители с выпуском более 1000 машин')
# Очень сложный график для меня был, Долго разбирался как вообще его строить. Получилось не сразу, но получилось !!!!

car_list = df['Make'].value_counts()[df['Make'].value_counts() > 1000].index  # Агрегируем по производителям, фильтруем по кол-ву и получаем список производителей
cars_CAFV = df.groupby(['Make', 'CAFV Eligibility Simple'])['Model Year'].count()   # Двойная агрегация (производитель -> CAFV)
df_car_CAFV = pd.DataFrame({}, columns=['Eligible', 'Not Eligible'], index=car_list)      # Формируем пустой датафрейм с индексами car_list и колонками допущен/недопущен

# Заполняем пустой датафрейм. В пустые ячейки записываем 0. Это необходимо для построения диаграммы
for car in car_list:
    eligible = 0
    not_eligible = 0
    if 'Eligible' in cars_CAFV[car].index:
        eligible = cars_CAFV[car]['Eligible']
    if 'Not Eligible' in cars_CAFV[car].index:
        not_eligible = cars_CAFV[car]['Not Eligible']
    df_car_CAFV.loc[car] = (eligible, not_eligible)
df_car_CAFV['Full'] = df_car_CAFV['Eligible'] + df_car_CAFV['Not Eligible']

fg = plt.figure(figsize=(17, 8), constrained_layout=True)
gs = gridspec.GridSpec(ncols=3, nrows=1, figure=fg, wspace=0.05)
fg.add_subplot(gs[0, 1:])
plt.title('Соотношение допущенных/недопущенных машин по CAFV')
x = np.arange(car_list.shape[0])
width = 0.4
el = plt.bar(x - 0.2, df_car_CAFV['Eligible'], width, label='Eligible', color='g')
plt.bar_label(el, padding=3, rotation=90)
not_el = plt.bar(x+0.2, df_car_CAFV['Not Eligible'], width, label='Not Eligible', color='r')
plt.bar_label(not_el, padding=3, rotation=90)
plt.xticks(x, car_list, rotation=90)
plt.grid(True, axis='y', linestyle='--')
plt.ylim(0, 30000)
plt.ylabel('Кол-во машин')
plt.legend()

fg.add_subplot(gs[0, 0])
plt.barh(df['Make'].value_counts().sort_values(ascending=True).index, width=df['Make'].value_counts().sort_values(ascending=True))
plt.title('Кол-во машин, выпущенных производителями')
plt.xlabel('Общее кол-во выпущенных машин')
plt.grid(axis='x')
plt.show()

print('Из построенных диаграмм видно следующее:',
      ' - имеются явные лидеры: Tesla, Nissan, Chevrolet (больше всего машин, все допущены по CAFV)',
      ' - далее по уменьшению идут остальные с разным соотношение допущенных по CAFV (вплоть до полного отсутствия допущенных)',
      ' - видно, что общее число производителей со значимым объемом производства не столь велико',
      sep='\n')
print()
print('На этом отчет будем считать законченным :-)')