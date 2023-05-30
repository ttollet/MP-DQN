import click
import ast
import inspect  # Accessing function parameters


class ClickPythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except Exception as e:
            print(e)
            raise click.BadParameter(value)


def get_calling_function_parameters():
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    calling_function_parameters = {
        arg: values[arg] for arg in args if arg != 'self'}
    return calling_function_parameters
