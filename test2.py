"""
 * Project name(项目名称)：Python_linecache模块
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 20:25
 * Version(版本): 1.0
 * Description(描述)： 
 """

import random

if __name__ == '__main__':
    for i in range(1, 2):
        filename = "file" + str(i) + ".txt"
        print(filename)
        with open(filename, "w", encoding="utf-8") as file:
            for i in range(0, random.randint(10, 200)):
                file.write("第" + str(i) + "行" + ":-----测试-----" + filename + "\n")
