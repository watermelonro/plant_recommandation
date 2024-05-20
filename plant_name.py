import requests
from bs4 import BeautifulSoup
import csv

pageNo = 1

try:
    while True:
        # Send GET request to the API URL
        url = 'http://api.nongsaro.go.kr/service/garden/gardenList'
        params = {
            'apiKey': '__',
            'pageNo': pageNo
        }
        response = requests.get(url, params=params)

        # Parse the XML response
        soup = BeautifulSoup(response.content, 'xml')
        tags = ['cntntsNo', 'cntntsSj']
        
        items = soup.find_all('item')
        if not items:
            break
            
        with open('gardenName.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            if csvfile.tell() == 0: #파일 시작 부분에 현재 포인터가 있는지
                writer.writerow(tags) # tags를 헤더 행으로 작성
                csvfile.seek(0) # 파일 포인터를 다시 시작부분으로 이동 
                
            for item in items:
                row = [item.find(tag).text for tag in tags]
                writer.writerow(row)
                
        # Increase pageNo by 1 for the next request
        pageNo += 1

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)





