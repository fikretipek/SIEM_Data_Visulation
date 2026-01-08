import plotly.graph_objects as go
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Veri yükle
df = pd.read_csv(r"F:\\PythonTest\\fake_network_traffic.csv")
df = df.iloc[1:]  # İlk satır başlık değilse

# Sütun adlarını al
header = df.columns.tolist()

# Label encoding: Her kategoriye sayısal bir değer atayacağız
encoded_df = df.copy()
encoders = {}
for col in header:
    le = LabelEncoder()
    encoded_df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Her satır için "renk değeri" oluştur: örnek olarak ilk sütuna göre
# İstersen farklı stratejiyle gruplayabilirsin (örn: sınıf grubu, coğrafi bölge vb.)
color_values = encoded_df[header[0]].astype(float)

# Renk skalası
colorscale = 'Rainbow'  # Diğerleri: Viridis, Jet, Plasma, Turbo, etc.

# Parcats oluştur
fig = go.Figure(go.Parcats(
    dimensions=[{'label': col, 'values': df[col]} for col in header],
    line={
        'color': color_values,
        'colorscale': colorscale,
        'shape': 'hspline',
        'cmin': color_values.min(),
        'cmax': color_values.max()
    }
))

fig.show()
