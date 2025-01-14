import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

print('Теперь посмотрим на значения в нечисловых колонках:')
print('State:', df['State'].unique())
print('Make:', df['Make'].unique())
print('Electric Vehicle Type:', df['Electric Vehicle Type'].unique())
print('CAFV Eligibility Simple:', df['CAFV Eligibility Simple'].unique())
print()

print('Из полученных данных видно, что колонка State не представляет интереса, т.к. содержит всего одно значение')
print('Теперь посмотрим на соотношение производителей, типов машин и показателей CAFV. Для этого проведем группировку с подсчетом.')
print('По производителям:')
print(df['Make'].value_counts(), '\n')
print('По типам машин:')
print(df['Electric Vehicle Type'].value_counts(), '\n')
print('По показателю CAFV:')
print(df['CAFV Eligibility Simple'].value_counts(), '\n')
print()

print('Теперь посмотрим более сложную статистику. Посмотрим на кол-во соответствий машин требованиям CAFV среди производителей')
print('Для этого произведем двойную агрегацию (по производителю и показателю CAFV)')
print(df.groupby(['Make', 'CAFV Eligibility Simple'])['Model Year'].count().sort_index())
print()

print('Теперь визуализируем все это !!!!!!!!')
sns.set()
model_fig = sns.displot(data=df, x='Model Year', aspect=2,  kde=True)
model_fig.set_xlabels(label='Model Year (year)').set_ylabels('Count 2')
plt.show()
sns.displot(data=df, x='Electric Range').set_xlabels('')
plt.show()
