# coding=utf-8
import os
import time
from utils.topo import topo
from utils.scripts import *

if __name__ == "__main__":

    print("使用root用户运行, 并分配好足够的 hugepage! 任意键继续")
    input()

    # 1. 创建拓扑
    tp = topo()

    # 2. 创建容器并启动 OVS
    start = time.time()
    run_ovs_docker(tp)
    end = time.time()
    print("create and start ovs cost time: ", end - start)


    # 3. 创建 veth peer，并挂载到对应的容器
    time.sleep(30)      # 等待容器启动 OVS

    start = time.time()
    mount_veth_peer(tp)
    end = time.time()
    print("create veth peer cost time: ", end - start)

    time.sleep(5)

    # 4. 开始维护链路（通断与延迟）
    tp.update_link_delay()


