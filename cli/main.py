# cli/main.py

import click
from phase_manager import PhaseManager, Phase

@click.command()
@click.option("--phase", type=click.Choice(["meeting", "develop", "test"]))
def main(phase):
    pm = PhaseManager()
    pm.current = Phase[phase.upper()]

    # ここに将来的にフェーズ処理を挿入できる（例：Gemini CLI 呼び出しなど）
    print(f"🔷 現在のフェーズ: {pm.current.name}")
    
    # 仮に全て成功とする
    pm.complete_phase(success=True)

if __name__ == "__main__":
    main()
