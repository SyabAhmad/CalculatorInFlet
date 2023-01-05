import flet
import flet as ft
from flet import (
    row,
    column,
    colors,
    Text,
    TextField,
    TextButton,
    FilledButton,
    floating_action_button
)


def main(page: ft.Page):
    page.title = "Calculator"
    result = ft.Text(value="0", color="white")

    ac = ft.ElevatedButton(text="AC", color="red")
    plusminus = ft.ElevatedButton(text="+/-")
    percent = ft.ElevatedButton(text="%")
    divide = ft.ElevatedButton(text="/")
    seven = ft.ElevatedButton(text="7", color="orange")
    eight = ft.ElevatedButton(text="8", color="orange")
    nine = ft.ElevatedButton(text="9", color="orange")
    multiply = ft.ElevatedButton(text="*")
    four = ft.ElevatedButton(text="4", color="orange")
    five = ft.ElevatedButton(text="5", color="orange")
    six = ft.ElevatedButton(text="6", color="orange")
    minus = ft.ElevatedButton(text="-")
    one = ft.ElevatedButton(text="1", color="orange")
    two = ft.ElevatedButton(text="2", color="orange")
    three = ft.ElevatedButton(text="3", color="orange")
    plus = ft.ElevatedButton(text="+")
    zero = ft.ElevatedButton(text="0")
    point = ft.ElevatedButton(text=".")
    equals = ft.ElevatedButton(text="=")
    page.add(
        # ft.Row(
        #     controls=[
        #         result = ft.alignment(end)
        #     ]
        # ),
        ft.Row(
            controls=[
                ac,
                plusminus,
                percent,
                divide
            ]
        ),
        ft.Row(
            controls=[
                seven,
                eight,
                nine,
                multiply,
            ]
        ),
        ft.Row(
            controls=[
                four,
                five,
                six,
                minus,
            ]
        ),
        ft.Row(
            controls=[
                one,
                two,
                three,
                plus
            ]
        ),
        ft.Row(
            controls=[
                zero,
                equals,
                point
            ]
        ),
    )

ft.app(target=main)