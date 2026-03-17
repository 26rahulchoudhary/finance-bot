import streamlit as st
import requests
import yfinance as yf
import plotly.graph_objects as go

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="AI Stock Analyzer", layout="wide")

# -------------------------------
# Helpers
# -------------------------------
def format_indian_number(num):
    try:
        num = int(num)
        s = str(num)

        last3 = s[-3:]
        rest = s[:-3]

        if rest != "":
            rest = rest[::-1]
            rest = ','.join([rest[i:i+2] for i in range(0, len(rest), 2)])
            rest = rest[::-1]
            return rest + ',' + last3
        else:
            return last3
    except:
        return "N/A"


def format_inr_short(num):
    try:
        num = float(num)
        if num >= 1e7:
            return f"₹ {num/1e7:.2f} Cr"
        elif num >= 1e5:
            return f"₹ {num/1e5:.2f} L"
        else:
            return f"₹ {num}"
    except:
        return "N/A"


def safe_format(num):
    return format_inr_short(num) if num else "N/A"


# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("Settings")

period = st.sidebar.selectbox(
    "Select Time Period",
    ["1mo", "6mo", "1y", "5y"],
    index=2
)

# -------------------------------
# Title
# -------------------------------
st.title("AI Fundamental Stock Analyzer")

# -------------------------------
# Input
# -------------------------------
ticker = st.text_input("Enter Stock Ticker", "RELIANCE.NS")

analyze = st.button("Analyze")

# -------------------------------
# Main Logic
# -------------------------------
if analyze and ticker:

    with st.spinner("Analyzing stock..."):

        try:
            # Call FastAPI backend
            response = requests.get(f"http://localhost:8000/analyze/{ticker}")
            data = response.json()

            data_block = data.get("data", {})

            # -------------------------------
            # Tabs
            # -------------------------------
            tab1, tab2 = st.tabs(["Overview", "AI Analysis"])

            # ===============================
            # TAB 1: OVERVIEW
            # ===============================
            with tab1:

                # Metrics
                st.subheader("Key Metrics")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric("Price", safe_format(data_block.get("price")))
                col2.metric("P/E Ratio", data_block.get("pe_ratio", "N/A"))
                col3.metric("Market Cap", safe_format(data_block.get("market_cap")))
                col4.metric(
                    "ROE",
                    f"{(data_block.get('roe') or 0)*100:.2f}%" if data_block.get("roe") else "N/A"
                )

                # -------------------------------
                # Chart
                # -------------------------------
                stock = yf.Ticker(ticker)
                hist = stock.history(period=period)

                fig = go.Figure()

                fig.add_trace(go.Scatter(
                    x=hist.index,
                    y=hist["Close"],
                    mode='lines',
                    name='Price'
                ))

                fig.update_layout(
                    title="Stock Price",
                    xaxis_title="Date",
                    yaxis_title="Price",
                    template="plotly_dark"
                )

                st.plotly_chart(fig, use_container_width=True)

            # ===============================
            # TAB 2: AI ANALYSIS
            # ===============================
            with tab2:

                # Insights
                st.subheader("Insights")

                for insight in data.get("insights", []):
                    st.success(insight)

                # Score
                score = min(len(data.get("insights", [])) * 2, 10)

                st.subheader("Fundamental Score")
                st.progress(score / 10)
                st.markdown(f"### {score}/10")

                # Summary
                st.subheader("AI Summary")

                st.markdown(f"""
                <div style="background-color:#1e1e1e;padding:15px;border-radius:10px">
                {data.get("summary", "No summary available")}
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error("Error fetching data. Make sure FastAPI backend is running.")

elif analyze:
    st.warning("Please enter a valid stock ticker")