import json
import geoip2.database

# 使用 GeoLite2 数据库获取 IP 地址的国家/地区信息的函数
def get_country(ip):
    # 将 "GeoLite2-Country.mmdb" 替换为你的 GeoLite2 数据库文件的路径
    with geoip2.database.Reader('GeoLite2-Country.mmdb') as reader:
        try:
            response = reader.country(ip)
            return response.country.name
        except:
            return None

# 从文件中读取 IP 地址列表
with open('ip_all.txt', 'r') as f:
    ip_all = f.read().splitlines()

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
for i, ip in enumerate(ip_all):
    new_template = template.copy()
    country = get_country(ip)
    tag = f"IP-{i + 1} ({country})" if country else f"IP-{i + 1}"
    new_template['tag'] = tag  # 如果有国家信息，将其添加到标签中
    new_template['server'] = ip
    templates.append(new_template)

# 使用换行符连接模板
result = ',\n'.join(json.dumps(t, indent=2) for t in templates)

# 读取原始模板文件
with open('original_template.json', 'r') as f:
    original_template = f.read()

# 将生成的结果添加到原始模板文件中
updated_template = original_template.replace('"  在此位置加入生成的结果"', result)

# 写入更新后的模板文件
with open('config-all.json', 'w') as f:
    f.write(updated_template)

# 读取 JSON 文件
with open('config-all.json', 'r') as f:
    config = json.load(f)

# 更新第一个 outbounds 的值
outbounds_1 = [template["tag"] for template in templates]
config["outbounds"][0]["outbounds"] = outbounds_1

# 更新第二个 outbounds 的值
outbounds_2 = [template["tag"] for template in templates]
config["outbounds"][1]["outbounds"] = outbounds_2

# 将 JSON 对象转换为字符串，并添加换行符
updated_config_str = json.dumps(config, indent=2)
updated_config_str = updated_config_str.replace('],', '],\n')  # 添加换行符

# 删除多余的换行符
updated_config_str = updated_config_str.replace('\n\n', '\n')

# 写入更新后的 JSON 文件
with open('Sing-Box-All.json', 'w') as f:
    f.write(updated_config_str)
