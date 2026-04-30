import streamlit as st


def inject_global_theme():
    """注入全局 CSS 主题，极简克制的样式优化"""
    st.markdown(
        """
<style>
/* 使用 Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Noto+Sans+SC:wght@400;500;600&display=swap');

/* CSS 变量定义 */
:root {
  --primary-color: #2563EB;
  --primary-hover: #1D4ED8;
  --background-color: #FFFFFF;
  --secondary-bg: #F7FAFC;
  --text-color: #1A202C;
  --text-secondary: #718096;
  --border-color: #E2E8F0;
  --border-radius: 10px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
}

/* 全局字体 */
html, body, .stApp {
  font-family: "Inter", "Noto Sans SC", system-ui, sans-serif;
}

/* ========== 侧边栏样式 ========== */
section[data-testid="stSidebar"] {
  background: var(--secondary-bg);
  border-right: 1px solid var(--border-color);
}

/* 侧边栏 expander 样式 */
section[data-testid="stSidebar"] .streamlit-expanderHeader {
  background: var(--background-color);
  border-radius: 8px;
  border: 1px solid var(--border-color);
  font-weight: 600;
  padding: 0.75rem 1rem;
}

section[data-testid="stSidebar"] .streamlit-expanderContent {
  background: var(--background-color);
  border-radius: 0 0 8px 8px;
  border: 1px solid var(--border-color);
  border-top: none;
  padding: 1rem;
}

/* ========== 按钮样式 ========== */
button {
  border-radius: var(--border-radius) !important;
  font-weight: 500;
  transition: all 0.2s ease;
}

button[kind="primary"] {
  background-color: var(--primary-color) !important;
  color: white !important;
  border: none !important;
}

button[kind="primary"]:hover {
  background-color: var(--primary-hover) !important;
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

/* ========== 输入框样式 ========== */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
  border-radius: var(--border-radius) !important;
  border: 1px solid var(--border-color) !important;
  padding: 0.75rem;
  transition: all 0.2s ease;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
  border-color: var(--primary-color) !important;
  box-shadow: 0 0 0 3px rgba(37,99,235,0.1);
  outline: none;
}

/* ========== 选择框样式 ========== */
.stSelectbox [data-baseweb="select"] > div {
  border-radius: var(--border-radius) !important;
  border: 1px solid var(--border-color) !important;
  min-height: 2.5rem;
}

.stSelectbox [data-baseweb="select"]:hover > div {
  border-color: #CBD5E0 !important;
}

.stSelectbox [data-baseweb="select"]:focus-within > div {
  border-color: var(--primary-color) !important;
  box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
}

/* ========== 多选框样式 ========== */
.stMultiSelect [data-baseweb="select"] > div {
  border-radius: var(--border-radius) !important;
  border: 1px solid var(--border-color) !important;
}

.stMultiSelect [data-baseweb="tag"] {
  border-radius: 6px !important;
  background: var(--primary-color) !important;
  color: white !important;
  border: none !important;
}

/* ========== Tabs 样式 ========== */
.stTabs [data-baseweb="tab-list"] {
  gap: 0px;
  border-bottom: 2px solid var(--border-color);
  overflow-x: auto;
  flex-wrap: nowrap;
}

.stTabs [data-baseweb="tab"] {
  padding: 0.75rem 1.25rem;
  border-radius: 0 !important;
  background: transparent;
  color: var(--text-secondary);
  font-weight: 500;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.stTabs [data-baseweb="tab"]:hover {
  background: rgba(37,99,235,0.04);
  color: var(--text-color);
}

.stTabs [aria-selected="true"] {
  background: transparent !important;
  color: var(--primary-color) !important;
  font-weight: 600 !important;
  border-bottom: 2px solid var(--primary-color) !important;
  margin-bottom: -2px;
}

/* ========== Expander 样式 ========== */
.streamlit-expanderHeader {
  border-radius: var(--border-radius);
  background: var(--secondary-bg);
  border: 1px solid var(--border-color);
  font-weight: 500;
}

/* ========== 容器边框 ========== */
div[data-testid="stVerticalBlockBorderWrapper"] {
  border-radius: var(--border-radius);
  border: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
}

/* ========== Metric 卡片样式 ========== */
[data-testid="stMetric"] {
  background: var(--background-color);
  border-radius: var(--border-radius);
  padding: 1rem;
  border: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
}

[data-testid="stMetric"]:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
  transition: all 0.2s ease;
}

/* ========== 响应式设计 ========== */
@media (max-width: 768px) {
  /* KPI 卡片改为 2 列 */
  [data-testid="stHorizontalBlock"] {
    flex-wrap: wrap;
  }
  [data-testid="stHorizontalBlock"] > div {
    flex: 1 1 45%;
    margin-bottom: 0.5rem;
  }
  
  /* Tab 栏可滚动 */
  .stTabs [data-baseweb="tab-list"] {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  
  .stTabs [data-baseweb="tab"] {
    padding: 0.5rem 0.75rem;
    font-size: 0.875rem;
  }
  
  /* 侧边栏全宽 */
  section[data-testid="stSidebar"] {
    width: 100% !important;
    min-width: unset !important;
  }
  
  /* 主内容区 padding */
  .main .block-container {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  /* KPI 卡片单列 */
  [data-testid="stHorizontalBlock"] > div {
    flex: 1 1 100%;
  }
  
  /* 标题缩小 */
  h1 {
    font-size: 1.5rem !important;
  }
}

/* ========== 滚动条美化 ========== */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: var(--secondary-bg);
}

::-webkit-scrollbar-thumb {
  background: var(--border-color);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: #A0AEC0;
}

/* ========== 选中文本颜色 ========== */
::selection {
  background: rgba(37,99,235,0.2);
  color: var(--text-color);
}
</style>
""",
        unsafe_allow_html=True,
    )
