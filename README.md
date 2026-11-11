# UKPM Property Management — 網站改版概念設計

[ukpm.uk](https://ukpm.uk/) 的改版提案。純靜態網站（HTML / CSS / JS），不需要建置步驟，任何靜態主機（例如 GitHub Pages）都能直接部署。

> **概念設計展示**：由 [UX CIRCLES](https://ux-circles.com/professionals) 設計，並非 UKPM 官方網站。
> 每頁頂端有「Concept」標示列，所有頁面設為 `noindex`，`robots.txt` 禁止搜尋引擎收錄。
> 如果正式採用：刪掉 `_build/build.py` 裡的 `.concept-bar` 及 `noindex`，重新生成，並把 `robots.txt` 改回 `Allow: /`。

## 頁面

原站 11 頁（每項服務一頁，部分只有兩三句）整合為 7 頁：

| 檔案 | 內容 | 原站頁面 |
|---|---|---|
| `index.html` | 首頁：香港 / 英國即時雙時鐘、8 項服務、為甚麼選 UKPM、四步出租流程、睇屋收費、按揭 | 首頁 |
| `about.html` | 團隊介紹、Property Redress Scheme 會員 | 公司簡介 |
| `landlords.html` | 物業出租、物業管理、出租證書周期表 | 物業出租、物業管理 |
| `buying.html` | 遙距睇屋（附即時收費估算）、物業買賣 | 遙距睇屋、物業買賣 |
| `mortgage.html` | 貸款額估算、DIP 三步、按揭問答（10 題） | 物業貸款 |
| `home-services.html` | 保險服務、水電煤寬頻（UW）、裝修工程 | 保險服務、水電煤寬頻、裝修工程 |
| `contact.html` | 聯絡資料；查詢表把資料整理成 WhatsApp 訊息，不需要伺服器 | Contact Us |

## 修改方式

所有頁面由 `_build/build.py` 生成（共用頁首、頁尾、聯絡資料）。改內容後執行：

```bash
python3 _build/build.py
python3 -m http.server 5173   # 預覽 http://localhost:5173
```

WhatsApp、Facebook、PRS 編號、貸款申請表連結都在 `build.py` 頂部。改了 CSS / JS 記得把 `CSS_V` / `JS_V` +1。

## 設計

- 顏色取自原站標誌：青綠 `#00ABBF`（按鈕及文字用加深的 `#00808F` 以符合 AA 對比）+ 嫩綠 `#75C873`，配深墨綠 `#0E2A31`
- 標誌的時鐘延伸成首頁「你在香港 / 我們在英國」即時雙時鐘，點出遙距管理的賣點；時差會按夏令時間自動顯示 7 或 8 小時
- 字體：Noto Sans TC（中文）+ Outfit（英文及數字）
- 相片：`remote.webp` 來自原站；其餘英國房屋相片為 Pexels 示意圖

## 上線前待確認

- [ ] **聯絡電郵**：原站只有 WhatsApp 及網上表格，找不到公開電郵，所以查詢表只發 WhatsApp。如有電郵請補上
- [ ] **按揭利率**：原站寫「1.7 厘至 6–8 厘，大部分客戶 2–3 厘」，屬低息年代的數字，已刪除，請按現時市況補充
- [ ] **按揭例子**：原站三個借貸計算例子數字前後不一（例如例子 3 的算式與結論不符，供養人扣減 0.8% 與結果對不上），已改為估算工具，只用「年收入 4.5 倍 / 樓價 75%（自住）/ 樓價 60%（出租）」，請確認是否沿用
- [ ] **出租證書周期表**（`landlords.html`）為英格蘭一般規定，是新加的內容，請核實並按 Renters' Rights Act 等最新法例更新
- [ ] **貸款申請表**連結改用 `https://ukpm.uk/loanApplicationform.pdf`（原站連到測試網域 myftpupload.com，已失效）
- [ ] **睇屋收費**「每英里 £1 來回 + 每個物業 £15」照搬原站，請確認仍然適用
- [ ] 首頁「8 項服務」、「服務全英國」等字眼按原站文案整理，請確認
