from src.views.menu import run

def main():
    db = {
        "usuarios": {},
        "tickets": {}
    }
    run(db)

if __name__ == "__main__":
    main()