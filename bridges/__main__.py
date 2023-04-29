import uvicorn

def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        'bridges.app.boot:get_app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )


if __name__ == '__main__':
    main()
