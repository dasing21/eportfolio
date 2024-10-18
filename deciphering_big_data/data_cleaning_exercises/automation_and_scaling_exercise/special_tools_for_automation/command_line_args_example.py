from import_config import get_config
import sys


def main(env):
    config = get_config(env)
    print(config)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        env = sys.argv(1)
    else:
        env = "TEST"
    main(env)

# Running script example:
#  python my_script.py DEV ANALYSIS
#  python my_script.py PROD COLLECTION
# python my_script.py DEV /var/log/apache2/
# python my_script.py PROD /var/log/nginx/