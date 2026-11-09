import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "PingFang TC", "Noto Sans CJK TC", "sans-serif"]

fig, ax = plt.subplots(facecolor="white")

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# 象限底色
quadrants = [
    ((0, 0), 10, 10, "#dff5df"),   # 右上
    ((-10, 0), 10, 10, "#fde0e0"), # 左上
    ((-10, -10), 10, 10, "#e6f0ff"), # 左下
    ((0, -10), 10, 10, "#fff6d9"), # 右下
]
for (xy, w, h, color) in quadrants:
    ax.add_patch(Rectangle(xy, w, h, facecolor=color, edgecolor="white"))

# 座標軸
ax.annotate("", xy=(10, 0), xytext=(-10, 0),
            arrowprops=dict(arrowstyle="->", lw=2.2, color="#333"))
ax.annotate("", xy=(0, 10), xytext=(0, -10),
            arrowprops=dict(arrowstyle="->", lw=2.2, color="#333"))

for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

# 標題與軸名
ax.text(0, 10.8, "價量四象限", ha="center", va="bottom", fontsize=22, fontweight="bold")
ax.text(9.6, 0.6, "價格", ha="right", fontsize=14)
ax.text(0.6, 9.3, "成交量", va="top", fontsize=14)

ax.text(5, 5.5, "價漲量增", ha="center", fontsize=18, fontweight="bold", color="#226644")
ax.text(5, 3.6, "偏多\n買盤積極、趨勢健康\n常見於突破或主升段",
        ha="center", va="center", fontsize=12, color="#226644", linespacing=1.6)

ax.text(-5, 5.5, "價跌量增", ha="center", fontsize=18, fontweight="bold", color="#9a2f2f")
ax.text(-5, 3.6, "偏空\n賣壓強、可能續跌\n常見於跌破支撐",
        ha="center", va="center", fontsize=12, color="#9a2f2f", linespacing=1.6)

ax.text(-5, -4.5, "價跌量縮", ha="center", fontsize=18, fontweight="bold", color="#2d5f9a")
ax.text(-5, -6.4, "偏中性偏多\n賣壓不重\n常見於多頭健康回檔",
        ha="center", va="center", fontsize=12, color="#2d5f9a", linespacing=1.6)

ax.text(5, -4.5, "價漲量縮", ha="center", fontsize=18, fontweight="bold", color="#8a6d00")
ax.text(5, -6.4, "偏中性偏空\n追價意願不足\n慎防假突破",
        ha="center", va="center", fontsize=12, color="#8a6d00", linespacing=1.6)

plt.tight_layout()
plt.savefig("price_volume_quadrant_styled.png", dpi=220, bbox_inches="tight")
# plt.savefig("price_volume_quadrant.svg", bbox_inches="tight")
plt.show()
