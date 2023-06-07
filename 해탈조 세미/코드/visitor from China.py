from matplotlib import pyplot as plt

x_purpose = ["tourism", "business", "officialaffairs", "studying", "others"]
for _ in result:
    y_number = result[0]

# plt.bar(x_purpose,y_number, width=0.6)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)  # 그래프 두 개를 한 figure 내에 그리기
fig.subplots_adjust(hspace=0.05)  # 두 그래프 사이의 상하 간격 설정

# 각각의 그래프 그리기
ax1.bar(x_purpose, y_number, width=0.6, color=(232 / 255, 217 / 255, 255 / 255))
ax2.bar(x_purpose, y_number, width=0.6, color=(232 / 255, 217 / 255, 255 / 255))
ax3.bar(x_purpose, y_number, width=0.6, color=(232 / 255, 217 / 255, 255 / 255))

ax1.set_ylim(4000000, 5000000)  # 제일 위
ax2.set_ylim(200000, 800000)  # 가운데 부분 y축 범위 설정
ax3.set_ylim(0, 45000)  # 아랫 부분 y축 범위 설정

ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax3.spines['top'].set_visible(False)

ax1.tick_params(axis='x', which='both', bottom=False, top=False)
ax1.tick_params(axis='y', which='both', left=False, right=False)

ax2.tick_params(axis='x', which='both', bottom=False, top=False)
ax2.tick_params(axis='y', which='both', left=False, right=False)

ax1.set_yticklabels([])
ax2.set_yticklabels([])
ax3.set_yticklabels([])

ax1.set_title('visitor from china', fontsize=20, fontweight='bold')
ax3.set_xlabel('Purpose of visit', fontsize=15)
ax2.set_ylabel('Number of visitor', fontsize=15)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_visible(False)

ax1.text(x_purpose[0], y_number[0], "{:,}".format(y_number[0]), fontsize=12, fontweight='bold',
         color=(63 / 255, 0 / 255, 153 / 255), horizontalalignment='center',
         verticalalignment='bottom')
ax3.text(x_purpose[1], y_number[1], "{:,}".format(y_number[1]), fontsize=12, fontweight='bold',
         color=(63 / 255, 0 / 255, 153 / 255), horizontalalignment='center',
         verticalalignment='bottom')
ax3.text(x_purpose[2], y_number[2], "{:,}".format(y_number[2]), fontsize=12, fontweight='bold',
         color=(63 / 255, 0 / 255, 153 / 255), horizontalalignment='center',
         verticalalignment='bottom')
ax2.text(x_purpose[3], y_number[3], "{:,}".format(y_number[3]), fontsize=12, fontweight='bold',
         color=(63 / 255, 0 / 255, 153 / 255), horizontalalignment='center',
         verticalalignment='bottom')
ax2.text(x_purpose[4], y_number[4], "{:,}".format(y_number[4]), fontsize=12, fontweight='bold',
         color=(63 / 255, 0 / 255, 153 / 255), horizontalalignment='center',
         verticalalignment='bottom')

plt.xticks(rotation=45, ha='right')

plt.show()