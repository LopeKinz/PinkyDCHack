REQURIEMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    install_requires=REQURIEMENTS
)