# 问题分析

1. 网络链路会断开与重连，如果断开后就删除veth peer，重建时会有一定的时间开销。
   如果可以先将所有可能的链路都创建 veth peer，需要连接或断开时，只需添加或删除ovs端口即可。

2. 修改链路时延问题：每隔一秒钟就要更新一次链路时延，同一轨道的卫星之间时延不会有变化，
   因此只需要修改不同轨道间的时延。
   时延的更新间隔为1s，要求并发地更新所有链路的时延，更新的时间开销不能太大。
   可以预先读取下一个时隙每个节点需要更新的端口，然后**并发地对每一个OVS节点进行更新**。

3. 更新流表项：本地数据库中存储了所有可能业务的每个时隙的路由策略，控制器要根据当前的业务项和
   当前的时隙，读取本地数据库中的路由策略，并下发流表项给所有OVS节点。
   更新流表项时，要从每个业务的目的节点-->源节点的顺序进行更新，避免造成丢包。
   此时是**并发地对每个业务进行更新**。


# 仿真流程

1. 读取topo信息，建立网络topo，要包含所有可能的链路。
   用于生成 veth peer 对。

2. 创建OVS节点，并让每个节点启动OVS，设置模式为 secure，即只通过现有流表转发，不自动学习。
   创建bridge，但暂不创建port，port要根据时刻的链路情况来创建。

3. 要同时创建三个进程，分别是业务模拟器，控制器，时延模拟器，链路模拟器。
   业务模拟器用于接收用户指令，生成对应的业务（发送信息给控制器以下发流表，在业务起点产生流量、统计时延、丢包信息）。
   控制器用于接收业务项，并从**数据库**中读取业务路由信息，并**倒序下发流表给相关OVS**。
   时延模拟器定时更新链路时延，时延信息从**数据库**中读取，并按节点并发更新。
   链路模拟器则根据时刻的链路信息，断开或重建链路。

# 数据库数据结构

```bash
kyes:
  - "all_links"     # 所有可能的链路信息，用于一开始生成 veth peer 对
    value: hash[int, string]
        [
            "1101":"1102,1111,1201,1001",
            "1102":"1103,1101,1202,1002",
            ......
            # 当前节点编号：关联节点1，关联节点2，...
        ]
  - "business-{start}-{end}"      # 业务信息，每个业务独占一个键
    value: hash[int, string]
        [
            0:"1101,1102,1202,1302;1101,1201,1301,1302",
            10:"1101,1102,1202,1302;1101,1201,1301,1302",
            ......
            # 时刻(s)："路径1；路径2" 每个时刻有多个路径，以分号分隔。
        ]
  - 0 # 时隙
    value: hash[string, int]
        [
            "1101-1102":0.01345,
            "1101-1201":0.01445,
            ......
            # "节点a-节点b":时延 s
        ]
```