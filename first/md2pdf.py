import sys
import markdown

src = sys.argv[1]
dst = sys.argv[2]

with open(src, encoding="utf-8") as f:
    text = f.read()

body = markdown.markdown(text, extensions=["tables"])

css = """
body { font-family: 'Microsoft YaHei', 'SimSun', sans-serif; max-width: 800px;
       margin: 40px auto; padding: 0 20px; line-height: 1.8; color: #222; font-size: 14px; }
h1 { font-size: 22px; text-align: center; border-bottom: 2px solid #333; padding-bottom: 10px; }
h2 { font-size: 17px; margin-top: 28px; border-left: 4px solid #185FA5; padding-left: 8px; }
h3 { font-size: 15px; margin-top: 20px; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 13px; }
th, td { border: 1px solid #999; padding: 6px 10px; text-align: center; }
th { background: #E6F1FB; }
hr { border: none; border-top: 1px dashed #aaa; margin: 24px 0; }
"""

html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"

with open(dst, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML written:", dst)
