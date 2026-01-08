import pandas as pd
import random

# Parametreler
num_rows = 100

dst_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]      # 3 farklı hedef IP
src_ips = [f"192.168.1.{i}" for i in range(1, 11)]  # 10 farklı kaynak IP
dst_ports = [25, 465, 587]                         # SMTP portları
app_protocols = ["SMTP", "DNS", "COTP", "unknown-tcp", "not-applicable", "HTTP"]  # 6 farklı protokol

# Rastgele veri üretimi
data = {
    "dst_ip": [random.choice(dst_ips) for _ in range(num_rows)],
    "src_ip": [random.choice(src_ips) for _ in range(num_rows)],
    "dst_port": [random.choice(dst_ports) for _ in range(num_rows)],
    "apppro": [random.choice(app_protocols) for _ in range(num_rows)]
}

df = pd.DataFrame(data)

# Excel'e kaydet
#output_path = "C:\\Test\\fake_network_traffic.xlsx"

####output_path = "C:\Test\fake_network_traffic.xlsx" Burada \f (\x0c) karakteri \f kaçış karakteri olarak algılanıyor, çünkü \T, \f, \n gibi karakterler Python’da özel anlam taşır.
#df.to_excel(output_path, index=False)

output_path = "C:\\Test\\fake_network_traffic.csv"
df.to_csv(output_path, index=False)



output_path
