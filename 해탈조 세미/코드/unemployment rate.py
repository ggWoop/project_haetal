import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 읽기
data = pd.read_csv('실업률_시도__20230602143912.csv', encoding="euc-kr")

# 전체 데이터에서 시도별과 성별이 '계'인 데이터 선택
national_data = data[(data['시도별'] == '계') & (data['성별'] == '계')]

# 필요한 열 선택 (2019.1/4부터 2023.1/4까지)
columns = data.columns[2:]

# 데이터를 숫자로 변환
national_data_values = pd.to_numeric(national_data.iloc[0, 2:])

# 데이터프레임으로 변환
df = pd.DataFrame({
    'Quarter': columns,
    'Value': national_data_values
})

plt.figure(figsize=(14, 8))

# 산점도 그리기
sns.scatterplot(x='Quarter', y='Value', data=df, color='red', s=100)

# 그래프 그리기
sns.lineplot(x='Quarter', y='Value', data=df)

plt.xlabel('Quarter', fontsize=15)
plt.ylabel('Value', fontsize=15)
plt.title('Unemployment Rate in South Korea', fontsize=25)
plt.xticks(rotation=45)
plt.show()
