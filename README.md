<<<<<<< HEAD
## 🌌 開発標語（Motto）

> 機械の律を超克し、未知の詩脈で宇宙を再配置せよ
>>>>>>> 78055f3 (Phase A implementation: CPService, MessageService, test updates, and reference docs)

## ラウンド完了〜次ラウンド開始フロー

1. **最終フェーズ到達**  
   `python cli/main.py --advance`  
   → `reports/round_final_<N>_<project>.md` が自動生成
2. **開始テンプレをコピー**  
   `python cli/main.py --copy-start-template`  
   → `reports/round_start_<N+1>_<project>.md`
3. VSCode で編集し、内容を固めたら  
   ```bash
   git add reports/round_start_*
   git commit -m "Add round {N+1} start report"
   git push
