poetry run pip install -e git+https://github.com/cycraig/gym-platform#egg=gym_platform
poetry run pip install -e git+https://github.com/cycraig/gym-goal#egg=gym_goal

apt-get install libqt4-dev cmake-qt4 libboost-system-dev libboost-filesystem-dev  # qt4 packages typically missing
poetry run pip install -e git+https://github.com/cycraig/gym-soccer#egg=gym_soccer