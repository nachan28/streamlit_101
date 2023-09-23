import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

df = pd.DataFrame(np.random.rand(20, 3), columns=["a", "b", "c"])

st.write("データフレーム")
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# st.write(df)は引数にwidth, heightを取ることができない

st.write("テーブル")
st.table(df)

st.write("折れ線グラフ")
st.line_chart(df)

st.write("エリアグラフ")
st.area_chart(df)

st.write("棒グラフ")
st.bar_chart(df)

"""
# Hello world!
## nanako
### python

```python
import streamlit as st
import numpy as np
import pandas as pd
"""
# マジックコマンドでマークダウン、コードを書ける。streamlitでは他にもLaTexなども書ける。

map_df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70], columns=["lat", "lon"]
)
st.write("マップ")
st.map(map_df)


st.write("Interactive Widgets")
if st.checkbox("Show image"):
    img = Image.open("sample.png")
    st.write("Display image")
    st.image(img, caption="ねこの画像", use_column_width=True)

options = st.selectbox("あなたの好きな数字を教えてください", list(range(1, 10)))
"あなたの好きな数字は", options, "です"

text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味：", text

condition = st.slider("あなたの今のコンディションを教えてください", 0, 100, 50)
"あなたの今のコンディション：", condition

st.sidebar.write("サイドバーはこのように作ります")

st.write("レイアウト")
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここが右カラム")

expander = st.expander("問い合わせ1")
expander.write("問い合わせ1の回答")
expander = st.expander("問い合わせ2")
expander.write("問い合わせ2の回答")
expander = st.expander("FAQに")
expander.write("よく使われるよ")

st.write("プログレスバーの表示")
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"
