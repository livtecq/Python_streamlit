import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')



st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})


# データフレーム
st.dataframe(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```
"""

df1 =pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

# 折れ線グラフ
st.line_chart(df1)

# エリアチャート
st.area_chart(df1)

# 棒グラフ
st.bar_chart(df1)


df2 =pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

# 新宿付近の緯度経度マッピング

st.map(df2)



st.write('Display Image')

img = Image.open('main.png')

# 画像の表示
st.image(img, caption='bonobono', use_column_width=True)

#チェックボックスの有無で画像の表示・非表示
if st.checkbox('Show Image'):
    st.image(img, caption='bonobono', use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えて下さい、',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

# テキスト入力
st.write('Interactive Widgets')
text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味：', text

# スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition
