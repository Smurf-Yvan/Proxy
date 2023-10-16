import requests
import base64
import yaml
from unidecode import unidecode  # 导入unidecode库

# 替换为您的Clash订阅链接
clash_subscribe_url = "YOUR_CLASH_SUBSCRIBE_URL_HERE"

# 发送GET请求获取Clash订阅数据
response = requests.get(clash_subscribe_url)
# 处理订阅数据，将所有Unicode字符转换为ASCII字符
cleaned_subscribe_data = unidecode(response.text.replace('-', '+').replace('_', '/'))
# 使用urlsafe_b64decode()解码，然后将bytes转换为utf-8字符串
clash_subscribe_data = base64.urlsafe_b64decode(cleaned_subscribe_data).decode('utf-8')

# 解析Clash订阅数据
clash_config = yaml.safe_load(clash_subscribe_data)

# 提取V2Ray配置信息
v2ray_config = {
    # ... （与之前的代码保持一致）
}

# 将V2Ray配置信息转换为YAML格式
v2ray_subscribe_data = yaml.dump(v2ray_config, default_flow_style=False)

# 输出V2Ray订阅链接到文件
output_file_path = "v2ray_subscribe.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(f"V2Ray订阅链接:\n\n{v2ray_subscribe_data}")

print(f"V2Ray订阅链接已保存到文件: {output_file_path}")
