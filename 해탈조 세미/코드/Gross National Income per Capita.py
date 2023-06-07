import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 읽기
data = pd.read_csv('1인당_국민총소득_당해년가격__20230602135844.csv', encoding="euc-kr")

# 전체 데이터에서 국가별이 '대한민국'인 데이터 선택
korea_data = data[data['국가별'] == '대한민국']

# 필요한 열 선택 (2015부터 2021까지)
columns = data.columns[1:]

# 데이터를 숫자로 변환
korea_data_values = pd.to_numeric(korea_data.iloc[0, 1:])

# 데이터프레임으로 변환
df = pd.DataFrame({
    'Year': columns,
    'Value': korea_data_values
})

plt.figure(figsize=(14, 8))

# 산점도 그리기
sns.scatterplot(x='Year', y='Value', data=df, color='red', s=100)

# 그래프 그리기
sns.lineplot(x='Year', y='Value', data=df)

plt.xlabel('Year', fontsize=15)
plt.ylabel('Value', fontsize=15)
plt.title("Korea's per capita gross national income", fontsize=25)
plt.xticks(rotation=45)
plt.show()
