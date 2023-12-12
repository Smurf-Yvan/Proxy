import json
import base64

# 读取配置文件
with open("config.json", "r") as config_file:
    server_config = json.load(config_file)

# 将配置信息转换为JSON字符串
config_json = json.dumps(server_config)

# 将JSON字符串进行Base64编码
base64_encoded_config = base64.urlsafe_b64encode(config_json.encode()).decode()

# 构建订阅链接
subscribe_link = f"vmess://{base64_encoded_config}"

# 将订阅链接写入文件
with open("V2ray.json", "w") as output_file:
    output_file.write(subscribe_link)

print("订阅链接已保存到 V2ray.json 文件中。")
