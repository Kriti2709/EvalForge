from app.core.config import settings


def main():

    print("=" * 40)
    print("Welcome to EvalForge")
    print("=" * 40)

    print(f"Project: {settings.PROJECT_NAME}")
    print(f"Version: {settings.VERSION}")
    print(f"Environment: {settings.ENVIRONMENT}")

    print("\nEvalForge initialized successfully!")


if __name__ == "__main__":
    main()