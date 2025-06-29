---
title: "PLAN：軽量AI開発 - 第1ラウンド"
date: 2025-06-29
authors: ["熊谷義行", "ChatGPT"]
phase: "会議"
status: "draft"
---

# 📝 ラウンド目的
軽量AI v0.1 を **ユーザー発言 → 署名付き Petal ログ保存 → 観測者AI キュー連携** まで動かし、  
今後の拡張 (UI・詩幣通知) に耐えられる基盤を固める。

---

## 1. スコープ
| 区分 | 対象 | 備考 |
|------|------|------|
| **含む** | `/statements` POST 正常／異常系 | FastAPI & Pydantic |
|  | Ed25519 署名ユーティリティ | `pynacl` |
|  | Petal JSONL ログローテーション (月次) | UTC ISO8601 |
| **除外** | HSM 本番鍵管理 | 次ラウンド |
|  | Redis → gRPC 置換 | 次ラウンド |
|  | UI 実装 | 別プロジェクト |

---

## 2. TODO & タスク分解

| # | タスク | 担当 | 期限 |
|---|--------|------|------|
| 1 | `domain/schema.py` で `StatementRequest` / `StatementResponse` 定義 | ChatGPT | 06-30 |
| 2 | 署名ユーティリティ単体テスト (`verify_signature`) | Gemini | 07-01 |
| 3 | Schemathesis 契約テスト導入 | Gemini | 07-02 |
| 4 | CP 残高永続化 (SQLite→Redis mock) | ChatGPT | 07-02 |
| 5 | ドキュメント (`docs/index.md`) 自動生成スクリプト | Gemini | 07-03 |

---

## 3. 受け入れ基準 (Definition of Done)

- [ ] `pytest -q` で 0 failed  
- [ ] `/statements` API が OpenAPI 3.1 に合致  
- [ ] 署名付き JSONL が `output_logs/statements/` に出力  
- [ ] `docs/` に API 更新が反映  
- [ ] PLAN の全タスク完了チェック

---

## 4. スケジュール

```

06-29  会議フェーズ完了 → 開発フェーズ開始
07-02  開発フェーズ完了 → テストフェーズ開始
07-03  テストフェーズ完了 → 最終報告書生成

```

---

## 5. リスク & 対策

| リスク | 対策 |
|--------|------|
| httpx バージョン依存問題 | 0.23.0 に固定 (`requirements-dev.txt`) |
| 署名鍵流出 | `.env` と `.gitignore` で除外、HSM検討 |
| datetime 型変換バグ | `json.dumps(default=str)` を標準化 |

---

## 6. Gemini への要望

- [ ] Pydantic v2 への移行是非をレビュー  
- [ ] Schemathesis シナリオ自動生成  
- [ ] Redis → gRPC 置換時の推奨ライブラリまとめ

---

## 7. 参考資料

- `docs/system_overview/starling_system_overview.md`
- `docs/system_overview/token_handling.md`
- `docs/system_overview/communication_policy.md`

---

## 8. 署名
```

提出者: 熊谷義行 / ChatGPT
提出日: 2025-06-29

```
```

---