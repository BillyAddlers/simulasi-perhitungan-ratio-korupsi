from matplotlib import pyplot
from numpy import array


class Cases:
	def __init__(self, always, often, sometimes, never):
		self.always = always
		self.often = often
		self.sometimes = sometimes
		self.never = never
		self.total_resp = always + often + sometimes + never

	def get_ratio(self):
		total = self.total_resp
		always_percent = (self.always / total) * 100
		often_percent = (self.often / total) * 100
		sometimes_percent = (self.sometimes / total) * 100
		never_percent = (self.never / total) * 100
		return {
			"always": always_percent,
			"often": often_percent,
			"sometimes": sometimes_percent,
			"never": never_percent
		}

	def get_piechart(self):
		data = array([self.always, self.often, self.sometimes, self.never])

		pyplot.pie(data, labels=["Selalu", "Sering", "Jarang", "Tidak Ada"])
		pyplot.show()

	def get_average_score(self):
		total = self.get_ratio()["never"]
		total = round((total / 50) * 2, 3)

		return total


def get_rule_manipulation_cases():
	return Cases(13, 5, 69, 1638)


def get_power_abuse():
	return Cases(16, 5, 52, 1652)


def get_affection_selling():
	return Cases(14, 5, 50, 1624)


def get_suap():
	return Cases(16, 8, 77, 1624)


def get_calo():
	return Cases(16, 17, 55, 1637)


def get_cheat():
	return Cases(13, 15, 71, 1626)


def get_black_market():
	return Cases(12, 8, 35, 1670)


def get_all_cases():
	return {
		"rule_manip": get_rule_manipulation_cases(),
		"power_abuse": get_power_abuse(),
		"affection_selling": get_affection_selling(),
		"suap": get_suap(),
		"calo": get_calo(),
		"cheat": get_cheat(),
		"black_market": get_black_market()
	}


def get_all_average_score():
	current_value = 0
	for avg in get_all_cases().values():
		current_value += avg.get_average_score()

	result = current_value / len(get_all_cases())
	result = round(result, 3)
	return result


def get_bar_plot():
	raw_data = get_all_cases().values()
	courses = get_all_cases().keys()
	values = map(lambda x: x.get_average_score(), get_all_cases().values())
	values = list(values)

	fig = pyplot.figure(figsize=(10, 5))

	pyplot.bar(courses, values)
	pyplot.xlabel("Kasus")
	pyplot.ylabel("Skor Rata-Rata")
	pyplot.title("Skor Rata-Rata Kasus Korupsi")
	pyplot.show()
