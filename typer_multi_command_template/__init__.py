import typer

from typer_multi_command_template.bye import bye
from typer_multi_command_template.hello import hello

cli = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]}, no_args_is_help=True
)

# manually call the decorator since the functions are in their own files
cli.command()(hello)
cli.command()(bye)
