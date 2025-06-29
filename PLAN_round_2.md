# Phase A 開発計画書 (Round 2)

## 1. 大テーマ
CP (Compute Point) サービスの新規実装と、それを利用したメッセージ予約機能の実現。

## 2. WBS (Work Breakdown Structure)

| タスク ID | タスク内容 | 担当者 | 見積工数 (人時) |
|---|---|---|---|
| A-01 | `PLAN_round_2.md` の作成 | AI | 0.1 |
| A-02 | `app/cp_service.py` の新規作成と `CPService` の実装 | AI | 1.0 |
| A-03 | `tests/test_cp_service.py` の新規作成とテスト5ケース実装 | AI | 1.0 |
| A-04 | `app/message_service.py` への `reserve_message` メソッド追加 | AI | 1.5 |
| A-05 | `tests/test_message_service.py` の更新と `reserve_message` のテスト実装 | AI | 1.5 |
| A-06 | CLIによるCP消費・メッセージ予約の動作確認 | User | 0.5 |

## 3. リスクと代替案

| リスク | 代替案 |
|---|---|
| `CPService` の設計が将来の要件（例：複数種類のCP）に対して単純すぎる可能性がある。 | 初期実装ではシンプルなカウンターとし、将来的な要求が明確になった時点でリファクタリングする。 |
| `MessageService` と `CPService` の結合度が高くなりすぎる懸念。 | DI（Dependency Injection）パターンを導入し、`MessageService` の初期化時に `CPService` のインスタンスを注入する方式を検討する。これにより、テスト容易性が向上し、疎結合を維持できる。 |

## 4. 完了判定基準

1.  **自動テストの成功**: `pytest` コマンドを実行し、すべてのテストがエラーなくパスすること（緑色の結果）。
2.  **手動動作確認**: CLIツール等を用いて、以下のシナリオが正常に動作することを確認できる。
    - メッセージを予約する。
    - 予約時に指定したCPが消費され、残高が減少する。
    - CPが不足している場合に予約が失敗する。
