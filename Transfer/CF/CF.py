import json
import re
# 读取文件中的IP地址列表
with open('ip_addresses.txt', 'r') as f:
    ip_addresses = f.read().splitlines()

# 准备模板
template ={
      "type": "vless",
      "tag": "",
      "server": "",
      "server_port": 8880,
      "uuid": "161aa91f-9517-49ad-bc15-d22921ff9167",
      "network": "tcp",
      "transport": {
        "type": "ws",
        "path": "/?ed=2048",
        "headers": {
          "Host": "yvan-proxy.filmtv.workers.dev"
        }
      }
    }

# 生成多个模板并保存到列表中
templates = []
for i, ip in enumerate(ip_addresses):
    new_template = template.copy()
    new_template['tag'] = f"IP-{i + 1}"
    new_template['server'] = ip
    templates.append(new_template)

# 将多个模板以换行符连接起来
result = ',\n'.join(json.dumps(t, indent=2) for t in templates)

# 读取原始模板文件
with open('original_template.json', 'r') as f:
    original_template = f.read()

# 在原始模板文件中添加生成的结果
updated_template = original_template.replace('"  在此位置加入生成的结果"', result)

# 写入更新后的模板文件
with open('config.json', 'w') as f:
    f.write(updated_template)

# 读取IP地址列表
with open('ip_addresses.txt', 'r') as f:
    ip_addresses = f.read().splitlines()

# 读取JSON文件
with open('config.json', 'r') as f:
    config = json.load(f)

# 更新第一个outbounds的值
outbounds_1 = ["IP-" + str(i + 1) for i in range(len(ip_addresses))]
config["outbounds"][0]["outbounds"] = outbounds_1

# 更新第二个outbounds的值
outbounds_2 = ["IP-" + str(i + 1) for i in range(len(ip_addresses))]
config["outbounds"][1]["outbounds"] = outbounds_2

# 将JSON对象转换为字符串，并添加换行符
updated_config_str = json.dumps(config, indent=2)
updated_config_str = updated_config_str.replace('],', '],\n')  # 添加换行符

# 写入更新后的JSON文件
with open('Sing-Box.json', 'w') as f:
    f.write(updated_config_str)