#!/usr/bin/env python
import click
import yaml
from jinja2 import Environment, FileSystemLoader

SRC_DIR = './templates'


@click.command()
@click.argument('meetups_file', type=click.File('rb'))
@click.argument('output_file', type=click.File('wb'))
def build(meetups_file, output_file):
    jinja_env = Environment(autoescape=True, loader=FileSystemLoader(SRC_DIR))
    meetups = yaml.load(meetups_file)

    context = {
        'meetups': meetups
    }
    template = jinja_env.get_template('README.md')
    output_file.write(template.render(context).encode('utf-8'))


@click.group()
def cli():
    pass


cli.add_command(build)


if __name__ == '__main__':
    cli()
