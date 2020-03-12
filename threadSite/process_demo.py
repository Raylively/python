import subprocess
from multiprocessing import Process


def check_alive(i):
    ip = "192.168.19.{}".format(i)
    result = subprocess.call('ping -w 1000 -n 1 %s' %
                             ip, stdout=subprocess.PIPE, shell=True)
    if result == 0:
        h = subprocess.getoutput('ping ' + ip)
        resp_time = h.split('平均 = ')[1]
        info = ('%s 能ping通，延迟平均值为：%s' % (ip, resp_time))
        print(info)

    else:
        with open('notalive.txt', 'a') as f:
            f.write('\n' + ip)
        info = ('%s ping 不通！' % ip)
        print(info)


def main():
    for i in range(256):
        p = Process(target=check_alive, args=(i,))
        p.start()


if __name__ == '__main__':
    main()
