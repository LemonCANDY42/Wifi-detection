from tqdm import tqdm
import time


NUM = 10

if __name__ == '__main__':

    with tqdm(total=NUM) as bar: # total表示预期的迭代次数
        for i in range(NUM): # 同上total值

            time.sleep(0.1)
            bar.set_description("正在打印 %s" % i)
            bar.update(1)  #每次更新进度条的长度