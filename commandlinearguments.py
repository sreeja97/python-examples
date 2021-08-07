import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("language")
    parser.add_argument("name")

    args = parser.parse_args()


    if(args.language == "Python"):
        print("Yes, that is a great choice")
    else:
        print("Have you tried python")

    print(f'Hello {args.name}, this was a simple introduction to argparse module')

"""try running below
    python commandlinearguments.py Python David

    python commandlinearguments.py Java Lisa

    python commandlinearguments.py -h

"""

