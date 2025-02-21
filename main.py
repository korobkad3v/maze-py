import core
import config as c

def main():

    mz = core.Maze()
    mz.map.display_map()
    mz.run()

    input("Press any key to exit")

if __name__ == "__main__":
    main()