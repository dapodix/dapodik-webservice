from dapodik_webservice import __version__

cli = None
try:
    from dapodik_webservice.console import cli  # type: ignore
except ImportError:
    pass


def main():
    if cli:
        cli()
    else:
        print("dapodik-webservice")
        print(f"Versi : {__version__}")


if __name__ == "__main__":
    exit(main())
