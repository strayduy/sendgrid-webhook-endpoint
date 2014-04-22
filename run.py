import sys
from app import main

DEFAULT_PORT = 8080

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = DEFAULT_PORT

    main.app.run(port=port, debug=True)

