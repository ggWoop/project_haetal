import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#CSV 파일 읽기
df = pd.read_csv('Enter_korea_by_purpose.csv', encoding="utf-8")

#방문객 수 상위 10개 국가 추출
top_10_countries = df.groupby('nation')['visitor'].sum().nlargest(7).index.tolist()
df_top_10 = df[df['nation'].isin(top_10_countries)].copy()

for i, country in enumerate(top_10_countries):

    df_country = df_top_10[df_top_10['nation'] == country]

    plt.figure(i+1, figsize=(14, 8))

    sns.lineplot(x='date', y='visitor', data=df_country, label='Visitor')

    sns.scatterplot(x='date', y='visitor', data=df_country, s=50, color='black')

    plt.xticks(rotation='horizontal')

    plt.title("Changes in the number of tourists from {} in South Korea".format(country), fontsize=15)

    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Visitor Count', fontsize=12)

    max_visitor = df_country['visitor'].max() * 1.1

    yticks = np.round(np.linspace(1, max_visitor, 7) / 5) * 5
    plt.yticks(yticks, [str(int(i)) for i in yticks])

    plt.legend(fontsize='medium')

    # x와 y축의 중앙 값을 계산합니다.
    x_center = (plt.xlim()[0] + plt.xlim()[1]) / 2
    y_center = (plt.ylim()[0] + plt.ylim()[1]) / 2

    # 계산된 중앙에 국가 이름을 표시합니다.
    plt.text(x_center, y_center, country,
             fontsize=120,
             color='red',
             ha='center',
             va='center',
             alpha=0.3)

plt.show()
