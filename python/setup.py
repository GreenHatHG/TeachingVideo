import study163
import utils
import bili

file = "../resource/data.xlsx"
keyword = "java"
websites = ('网易云课堂', 'Bilibili')

if __name__ == '__main__':
    utils.check(file)
    for website in websites:
        utils.printStart(website)

        # if website == '网易云课堂':
        #     study163.start(keyword, file)

        if website == 'Bilibili':
            bili.start(keyword, file)

        utils.printEnd(website)