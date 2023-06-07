import requests
from bs4 import BeautifulSoup

article_list_url_format = "http://apis.data.go.kr/B260003/DevCprTrendService2/getDevCprTrendList2?serviceKey=zjlglbiehEtBoLbA69fmBvINtaSrDz0%2Br3P5Rch4lsGreQJnQ%2BLNCvxhSPeLY3WHcsZ4vZ9unuFkaMKGFHeaJA%3D%3D&pageNo={pages}&numOfRows=10"

from tqdm import tqdm


def crawl_list():
    total_relation_list = []
    for i in tqdm(range(29)):
        article_list_url = article_list_url_format.format(pages=(i + 1))
        resp = requests.get(article_list_url)
        resp_json = resp.json()
        for item in resp_json["data"]:
            total_relation_list.append(
                [item["country_nm"], item["rgrd_link"], item["field_cd_nm"], item["trend_title_nm"], item["bdtxt_1_cn"],
                 item["bdtxt_2_cn"], item["bdtxt_3_cn"]])
    return total_relation_list


total_relation_list = crawl_list()

total_relation_list

import csv

# title=["국가","규제정책"]
# regulation_data = title.append(update_regulation_list)
# CSV 파일 쓰기 모드로 열기
with open("./covid_relationship.csv", "w", newline="", encoding="utf-8") as fw:
    writer = csv.writer(fw)
    writer.writerow(["국가명", "링크", "분류", "기사제목", "내용1", "내용2", "내용3"])
    # 각 행을 CSV 파일에 쓰기
    for row in total_relation_list:
        writer.writerows(total_relation_list)
