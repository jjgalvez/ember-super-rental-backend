import click
from superrental import app

@click.command()
@click.option('-d/-n', '--debug/-nomral', default=False)
def main(debug):
    app.run(debug=debug)

if __name__ == '__main__':
    main()
