# xpath是xml文档中搜索内容的一门语言
# HTML是xml的子集
# 可以从根结点搜索
# 安装lxml
class One:
    from lxml import etree
    xml="""
    <book>
        <name>野花遍地香</name>
        <price>1.23</price>
        <nick>臭豆腐</nick>
        <author>
            <nick id='10086'>周搭腔</nick>
            <nick id='10010'>周芷若</nick>
            <nick id='joy'>周杰伦</nick>
            <nick id='yilin'>蔡依林</nick>
            <div>
                <nick>热热热热热1</nick>
            </div>
            <span>
                <nick>热热热热热2</nick>
            </span>
        </author>
    </book>
    """
    tree=etree.XML(xml)
    # result=tree.xpath("/book/name/text()")#text()代表取文本
    result=tree.xpath("/book/author//nick/text()")#注意//默认匹配父节点下所有儿子结点中的含有孙子结点的内容
    #在author中找热1和热2。*表示任意的，通配符
    result1=tree.xpath("/book/author/*/nick/text()")
    result2=tree.xpath("/book//nick/text()")
    # print(result)
    # print(result1)
    # print(result2)

from lxml import etree
path="./爬虫/learn_from/xpath/tx.html"
tree=etree.parse(path)
result=tree.xpath('/html/body/ul/li[1]/a/text()')#xpath顺序从第一个开始，【】表示索引
#href="dapao"
result1=tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")#中括号里可以筛选属性的值
#ol中每个li做遍历
ol_li_list=result2=tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    #从li中提取文字信息
    name=li.xpath("./a/text()")#在li中继续去查找，相当于相对查找
    #拿到a标签里面的值
    href=li.xpath("./a/@href")#拿到属性值通过@
    # print(href)
