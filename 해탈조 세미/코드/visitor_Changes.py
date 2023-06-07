import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#CSV 파일 읽기
df = pd.read_csv('Enter_korea_by_purpose.csv', encoding="utf-8")

#방문객 수 상위 10개 국가 추출
top_10_countries = df.groupby('nation')['visitor'].sum().nlargest(7).index.tolist()
df_top_10 = df[df['nation'].isin(top_10_countries)].copy()

#각각의 나라에 대한 그래프 순차적으로 보여주기
for i, country in enumerate(top_10_countries):

    df_country = df_top_10[df_top_10['nation'] == country]

    # 새로운 그래프 창 열기
    plt.figure(i+1, figsize=(14, 8))

    # 각 나라에 대한 방문객 수에 대한 선형 그래프 그리기 
    sns.lineplot(x='date', y='visitor', data=df_country, label='Visitor')

    # 각 모서리에 점 찍기
    sns.scatterplot(x='date', y='visitor', data=df_country, s=50, color='black')

    # x축 레이블 방향 설정
    plt.xticks(rotation='horizontal')

    # 제목 설정 
    plt.title("Changes in the number of tourists from {} in South Korea".format(country), fontsize=15)

    # x축, y축 레이블 및 폰트 크기 설정
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Visitor Count', fontsize=12)

    # 최대 방문객 수 찾기 (여기서 10% 여유를 둠)
    max_visitor = df_country['visitor'].max() * 1.1

    # 최대 방문객 수를 7등분한 값으로 y축 눈금 설정, 가장 가까운 5의 배수로 반올림
    yticks = np.round(np.linspace(1, max_visitor, 7) / 5) * 5
    plt.yticks(yticks, [str(int(i)) for i in yticks])

    # 범례 추가
    plt.legend(fontsize='medium')

# 그래프 출력
plt.show()
