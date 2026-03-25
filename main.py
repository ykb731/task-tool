import json
from pathlib import Path

FILE_PATH = Path("tasks.json")


def load_tasks():
    if FILE_PATH.exists():
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def add_task(tasks):
    task = input("タスクを入力してください: ").strip()
    if not task:
        print("空のタスクは追加できません。")
        return
    tasks.append({"title": task, "done": False})
    save_tasks(tasks)
    print("タスクを保存しました。")


def show_tasks(tasks):
    if not tasks:
        print("\nタスクはまだありません。")
        return

    print("\nタスク一覧:")
    for i, task in enumerate(tasks, start=1):
        status = "完了" if task["done"] else "未完了"
        print(f"{i}. [{status}] {task['title']}")


def show_incomplete_tasks(tasks):
    print("\n未完了タスク:")
    for i, task in enumerate(tasks, start=1):
        if not task["done"]:
            print(f"{i}. {task['title']}")
    print(f"{len(tasks)}件のタスクを読み込みました")


def complete_task(tasks):
    if not tasks:
        print("完了にするタスクがありません。")
        return

    show_tasks(tasks)
    try:
        number = int(input("\n完了にするタスク番号を入力してください: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("タスクを完了にしました。")
        else:
            print("その番号のタスクはありません。")
    except ValueError:
        print("数字で入力してください。")


def delete_task(tasks):
    if not tasks:
        print("削除するタスクがありません。")
        return

    show_tasks(tasks)
    try:
        number = int(input("\n削除するタスク番号を入力してください: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"「{removed['title']}」を削除しました。")
        else:
            print("その番号のタスクはありません。")
    except ValueError:
        print("数字で入力してください。")


def main():
    tasks = load_tasks()

    while True:
        print("\n==== タスク管理ツール ====")
        print("1: タスク追加")
        print("2: タスク一覧表示")
        print("3: タスク完了")
        print("4: タスク削除")
        print("5: 終了")

        choice = input("選択してください: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("終了します。")
            break
        else:
            print("無効な入力です。1〜5を選んでください。")


if __name__ == "__main__":
    main()
