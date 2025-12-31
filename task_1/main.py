import uvicorn
import argparse
import sys
import logging
from src.api.app import app
logging.basicConfig(stream=sys.stdout, 
                    level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    parser = argparse.ArgumentParser(
                    description="Option to run the FastAPI server"
                )
    parser.add_argument(
                "--option",
                "-o",
                required=True,
                help="option to run the server",
                default="runserver",
                type=str
            )

    args = parser.parse_args()

    if args.option == "runserver":
        uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
        
    else:
        logging.info("Invalid option. Use --option runserver to start the server.")

if __name__ == "__main__":
    main()
    