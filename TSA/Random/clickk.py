import click


@click.command()
@click.option('--count', '-c',  default=1 , help='Number of greetings.')
@click.option('--name', '-n', prompt='Your name', help='The person to greet')
def hello(count, name):
    for i in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()