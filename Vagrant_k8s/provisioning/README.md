# ansible 自动化安装k8S

使用Ansible Playbook进行生产级别kubernetes集群部署，包含初始化系统配置、自动签发集群证书、安装配置etcd集群、calico、coredns、metrics-server等，并使用bootstrap方式认证以及kubernetes组件健康检查。本Playbook使用二进制方式部署，使用docker。

## 分支说明
* uat分支，部署公司uat环境的k8s集群。
## 配置
### 1.1、配置inventory

请按照inventory模板格式修改对应资源；
- [all:vars] env=xxx 为部署环境，区分certs的目录
todo：优化设计

### 1.2、配置集群安装信息

编辑group_vars/all.yml文件，填入自己的配置。
 - loadbalance: single=True时，此配置无效；适用于单节点master

## 二、安装步骤

### 2.1、ansible安装
ansible版本2.9以上,建议使用pip install
```bash
pip3 install ansible==2.9.21
pip3 install netaddr -i https://mirrors.aliyun.com/pypi/simple/
```

### 2.2、部署集群
```bash 
ansible-playbook playbook.yml -i inventory [-e env=xxx]
```

## 三、扩容节点
  Todo

## 四、升级证书

   Todo
## 五、升级kubernetes
   Todo

## 其他
to do:
1. 减少依赖，不使用filter_plugins
2. etcd配置文件变量使用不完全
3. 减少依赖，不使用next_nth_usable
4. init唯一主机的设计，有待优化
5. 集群扩容的操作，比如，新增一个node
6. 替换集群证书、kubernetes版本升级等
7. tags梳理
8. adventise的设计优化以及梳理
9. verify补充优化
11. 服务重启的触发优化
12. 配置分离，token、loadbalance及其他，可以的话，使用配置分离加载的方式；