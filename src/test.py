import csv

def csv_trans():
    # csv ファイル読み込み
    read_data=[]
    with open('./sample/input.csv') as f:
        reader=csv.DictReader(f)
        read_data = [row for row in reader]
    
    # データ加工
    write_data=[['' for i in range(5)] for j in range(2)]
    for i,row in enumerate(read_data):
        write_data[i][0]=row['ID']
        write_data[i][1]=row['書名']
        write_data[i][2]=row['価格']
        write_data[i][3]=row['冊数']
        #売上の計算
        write_data[i][4]=int(row['冊数'])*int(row['価格'])

    #データ書き込み
    with open('./sample/output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', '書名', '価格','冊数','売上'])
        for row in write_data:
            writer.writerow(row)


if __name__ == "__main__":
    csv_trans()