"""Входная точка, разбор аргументов, запуск игры."""

import argparse

from monstromaker.cli import prompt_player_names, run_game
from monstromaker.i18n import setup_i18n


def main() -> None:
	"""Разобрать аргументы, запустить игру."""
	parser = argparse.ArgumentParser(
		prog="monstromaker",
		description="Монстродел — карточная игра на страшность монстров.",
	)
	parser.add_argument(
		"--lang",
		default="ru_RU",
		metavar="LOCALE",
		help="Display language: ru_RU (default) or en_US",
	)
	parser.add_argument(
		"--players",
		nargs="*",
		metavar="NAME",
		help="Player names (2–4); skip to enter them interactively",
	)

	args = parser.parse_args()
	setup_i18n(args.lang)

	if args.players and 2 <= len(args.players) <= 4:
		print("ok") # TODO
	else:
		print("err") # TODO

	print("start game") # TODO


if __name__ == "__main__":
	main()
