"""Список карт Монстродела."""

from enum import Enum

WIN_THRESHOLD = 15
MAX_HAND_SIZE = 6
INITIAL_HAND_SIZE = 4


class CardType(Enum):
	"""Тип карты."""

	OBLIK = "ОБ"
	ACTION = "ДЕ"
	THREAT = "УГ"


class Card:
	"""Объект карты."""
	def __init__(
		self,
		key: str,
		card_type: CardType,
		name: str,
		description: str,
		stars: int = 0,
		shield: bool = False,
		ascii_art: str = "",
		count: int = 1,
		boost: int = 0,
	) -> None:
		self.key = key
		self.card_type = card_type
		self.name = name
		self.description = description
		self.stars = stars
		self.shield = shield
		self.ascii_art = ascii_art
		self.count = count
		self.boost = boost

	def display_type(self) -> str:
		return f"[{self.card_type.value}]"

	def total_stars(self) -> int:
		return self.stars + self.boost

	def copy(self) -> "Card":
		return Card(
			key=self.key,
			card_type=self.card_type,
			name=self.name,
			description=self.description,
			stars=self.stars,
			shield=self.shield,
			ascii_art=self.ascii_art,
			count=self.count,
			boost=0,
		)


_CATALOG: list[Card] = [
	# ── ОБЛИК ───
	Card(
		key="krilya",
		card_type=CardType.OBLIK,
		name="Крылья",
		description="+2★ навсегда",
		stars=2,
		count=2,
	),
	Card(
		key="roga",
		card_type=CardType.OBLIK,
		name="Металл-рога",
		description="+3★ навсегда",
		stars=3,
		count=2,
	),
	Card(
		key="hvost",
		card_type=CardType.OBLIK,
		name="Хвост",
		description="+1★ навсегда",
		stars=1,
		count=2,
	),
	Card(
		key="kogti",
		card_type=CardType.OBLIK,
		name="Ядовитые когти",
		description="+2★ навсегда",
		stars=2,
		count=2,
	),
	Card(
		key="bronya",
		card_type=CardType.OBLIK,
		name="Бронечешуя",
		description="+2★, щит от Пекла",
		stars=2,
		shield=True,
		count=2,
	),
	Card(
		key="glaza",
		card_type=CardType.OBLIK,
		name="Три глаза",
		description="+2★ навсегда",
		stars=2,
		count=2,
	),
	Card(
		key="shchupalca",
		card_type=CardType.OBLIK,
		name="Щупальца",
		description="+3★ навсегда",
		stars=3,
		count=2,
	),
	Card(
		key="klyki",
		card_type=CardType.OBLIK,
		name="Клыки",
		description="+2★ навсегда",
		stars=2,
		count=2,
	),
	Card(
		key="zhalo",
		card_type=CardType.OBLIK,
		name="Жало",
		description="+1★ навсегда",
		stars=1,
		count=2,
	),
	Card(
		key="gorb",
		card_type=CardType.OBLIK,
		name="Горб шипов",
		description="+2★ навсегда",
		stars=2,
		count=1,
	),
	Card(
		key="golova2",
		card_type=CardType.OBLIK,
		name="Двойная голова",
		description="+3★ навсегда",
		stars=3,
		count=1,
	),
	# ── ДЕЙСТВИЕ ───
	Card(
		key="laser",
		card_type=CardType.ACTION,
		name="Лазеры из глаз",
		description="выбери игрока: он теряет 1 облик",
		ascii_art="  O===>>~~~*\n  O===>>~~~*",
		count=2,
	),
	Card(
		key="teleport",
		card_type=CardType.ACTION,
		name="Телепортация",
		description="укради 1 облик у любого игрока",
		ascii_art="  *         *\n   \\       /\n    ---> /\n  (хоп!)",
		count=2,
	),
	Card(
		key="hunt",
		card_type=CardType.ACTION,
		name="Охота на ближн.",
		description="укради облик у соседнего игрока",
		ascii_art="  --> (хвать)\n  <-- (тащу!)",
		count=2,
	),
	Card(
		key="enhance",
		card_type=CardType.ACTION,
		name="Камень усиления",
		description="следующий облик +2★ дополнительно",
		ascii_art="   /~~~~\\\n  | *+2★ |\n   \\____/",
		count=2,
	),
	Card(
		key="evolve",
		card_type=CardType.ACTION,
		name="Эволюция",
		description="+2 карты, сброси 1 из руки",
		ascii_art="  +++>>>\n  ++карты",
		count=2,
	),
	Card(
		key="roar",
		card_type=CardType.ACTION,
		name="Рёв ужаса",
		description="все другие сбрасывают 1 карту из руки",
		ascii_art="   (((!!!\n  )))!!!)))\n   ~~БУ!~~",
		count=1,
	),
	Card(
		key="spy",
		card_type=CardType.ACTION,
		name="Монстро-шпион",
		description="тайно посмотри руку любого игрока",
		ascii_art="  (~_eye_~)\n  (слежка)",
		count=1,
	),
	Card(
		key="mutate",
		card_type=CardType.ACTION,
		name="Мутация",
		description="замени свой облик на верх колоды",
		ascii_art="  ОБЛ ~> X\n  <~~ НОВ",
		count=1,
	),
	Card(
		key="steal_discard",
		card_type=CardType.ACTION,
		name="Кража из сброса",
		description="возьми любую карту из сброса",
		ascii_art="  [/////]\n    <---\n  (нашёл!)",
		count=1,
	),
	# ── УГРОЗА ────
	Card(
		key="peklo",
		card_type=CardType.THREAT,
		name="Пекло",
		description="без Бронечешуи: потерять 1 облик",
		ascii_art="   /\\  /\\  /\\\n  /  \\/  \\/  \\\n   (жарко!!!)",
		count=2,
	),
	Card(
		key="catcher",
		card_type=CardType.THREAT,
		name="Монстролов",
		description="забери 1 облик у лидера",
		ascii_art="  o---[]<---o\n  (попал в сеть)",
		count=2,
	),
	Card(
		key="exam",
		card_type=CardType.THREAT,
		name="Экзамен по ОКам",
		description="все сбрасывают 1 карту из руки",
		ascii_art="  [?! ТЕСТ !?]\n   !!  !!  !!\n  (сдавай!!!)",
		count=1,
	),
	Card(
		key="mirror",
		card_type=CardType.THREAT,
		name="Зеркало страха",
		description="поменяйся обликом с лидером",
		ascii_art="  |] <~~~> [|\n  (всё наоборот)",
		count=1,
	),
]


def build_deck() -> list[Card]:
	"""Собрать колоду."""
	deck: list[Card] = []
	for template in _CATALOG:
		for _ in range(template.count):
			deck.append(template.copy())
	return deck


LEVEL_NAMES = [
	(0, 3, "Пугало из огорода"),
	(4, 6, "Кошмарик"),
	(7, 10, "Жуть"),
	(11, 14, "Ужастик"),
	(15, 9999, "НЕЧТО НЕВОЗМОЖНОЕ"),
]


def level_name(stars: int) -> str:
	"""Вернуть уровень по числу звезд."""
	for low, high, name in LEVEL_NAMES:
		if low <= stars <= high:
			return name
	return "НЕЧТО НЕВОЗМОЖНОЕ"

