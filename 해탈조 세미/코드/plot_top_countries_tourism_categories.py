import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# CSV 파일 읽기
df = pd.read_csv('Enter_korea_by_purpose.csv', encoding="utf-8")


# 방문객 수 상위 10개 국가 추출
top_10_countries = df.groupby('nation')['visitor'].sum().nlargest(7).index.tolist()
df_top_10 = df[df['nation'].isin(top_10_countries)].copy()


# 카테고리 설정 (visitor 제외)
categories = ['tourism', 'business', 'official affairs', 'studying', 'others']



# 각각의 나라에 대한 그래프 순차적으로 보여주기
for i, country in enumerate(top_10_countries):
    df_country = df_top_10[df_top_10['nation'] == country]
    
    
    # 새로운 그래프 창 열기
    plt.figure(i+1, figsize=(12, 8))
    
    
    # 각 카테고리에 대한 선형 그래프 그리기 (로그 스케일)
    for category in categories:
        sns.lineplot(x='date', y=category, data=df_country, label=category)
    
    
    # 각 모서리에 점 찍기
    for category in categories:
        sns.scatterplot(x='date', y=category, data=df_country, s=50, color='black')
    
    
    # x축 레이블 방향 설정
    plt.xticks(rotation='horizontal')
    
    # 제목 설정 
    plt.title("Changes in the number of tourists from {} in South Korea (Log Scale)".format(country), fontsize=15)
    
    
    # x축, y축 레이블 및 폰트 크기 설정
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Count (Log Scale)', fontsize=12)
    
    
    # y축 스케일을 로그 스케일로 설정
    plt.yscale('log')
    
    
    # 범례 추가
    plt.legend(title='Category', fontsize='medium')
    
    
# 그래프 출력   
plt.show()