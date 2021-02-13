import requests as rq
import xlrd#相关

workbook = xlrd.open_workbook('/Users/xxx/xxx/xxx/members.xlsx')#Excel所在位置,打开Excel

sheet1 = workbook.sheet_by_index(0)#默认sheet名称为sheet1
print (sheet1.name,sheet1.nrows,sheet1.ncols)#显示sheet的名称，行数，列数
cols = sheet1.col_values(0) # 获取玩家ID
print (cols)
x = 0
while(x<sheet1.nrows):
    file='/users/xxx/xxx/xxx/'+ cols[x] + '.png'#头像存储位置
    url="https://mc-heads.net/avatar/"+ cols[x] +"/300"#建议网站地址，末尾有玩家ID,默认大小300
    re=rq.get(url)
    with open(file,'wb')as f:
        f.write(re.content)#爬虫
    x=x+1
    print (x,"finished")#爬完一张
