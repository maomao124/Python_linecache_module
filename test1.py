"""
 * Project name(项目名称)：Python_linecache模块
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 20:21
 * Version(版本): 1.0
 * Description(描述)：
 函数基本格式	功能
linecache.getline(filename, lineno, module_globals=None)	读取指定模块中指定文件的指定行（仅读取指定文件时，无需指定模块）。
其中，filename 参数用来指定文件名，lineno 用来指定行号，module_globals 参数用来指定要读取的具体模块名。
注意，当指定文件以相对路径的方式传给 filename 参数时，该函数以按照 sys.path 规定的路径查找该文件。
linecache.clearcache()	如果程序某处，不再需要之前使用 getline() 函数读取的数据，则可以使用该函数清空缓存。
linecache.checkcache(filename=None)	检查缓存的有效性，
即如果使用 getline() 函数读取的数据，其实在本地已经被修改，而我们需要的是新的数据，
此时就可以使用该函数检查缓存的是否为新的数据。注意，如果省略文件名，该函数将检车所有缓存数据的有效性。
 """
import linecache
import random

if __name__ == '__main__':
    # print(linecache.getline(linecache.__file__, 42))
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")
    print(linecache.getline(linecache.__file__, random.randint(2, 178)), end="")

    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
    print(linecache.getline("file1.txt", random.randint(2, 178)), end="")
