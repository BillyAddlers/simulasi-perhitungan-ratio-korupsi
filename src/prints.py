from src.cases import get_rule_manipulation_cases, get_bar_plot, get_all_average_score
from src.simulated_data import get_respondent_gender_data, get_respondent_gender_data_ratio, \
	get_respondent_gender_piechart, get_respondent_education_data, get_respondent_education_piechart, \
	get_respondent_education_ratio, get_respondent_profession_data, get_respondent_profession_ratio, \
	get_respondent_profession_piechart


def print_header():
	print("""
	====== Anti-Korupsi Data Simulation ======
	path: main.py
	sample_data: Laporan_SPAK_TIII_35781.pdf
	""")


def print_respondent_gender():
	resp = get_respondent_gender_data()
	ratio = get_respondent_gender_data_ratio(resp)

	print(f"""
	Jumlah responden pria: {resp["male"]} {round(ratio["male"], 2)}%
	Jumlah responden wanita: {resp["female"]} {round(ratio["female"], 2)}%
	Total responden: {resp["total"]}
	""")
	get_respondent_gender_piechart(resp)


def print_respondent_education():
	resp_edu = get_respondent_education_data()
	ratio_edu = get_respondent_education_ratio(resp_edu)

	print(f"""
	Jumlah responden dengan pendidikan dibawah SMA: {resp_edu["under_highschool"]} {round(ratio_edu["under_highschool"], 2)}%
	Jumlah responden dengan pendidikan SMA: {resp_edu["highschool"]} {round(ratio_edu["highschool"], 2)}%
	Jumlah responden dengan pendidikan D1: {resp_edu["diploma1"]} {round(ratio_edu["diploma1"], 2)}%
	Jumlah responden dengan pendidikan D2: {resp_edu["diploma2"]} {round(ratio_edu["diploma2"], 2)}%
	Jumlah responden dengan pendidikan D3: {resp_edu["diploma3"]} {round(ratio_edu["diploma3"], 2)}%
	Jumlah responden dengan pendidikan S1: {resp_edu["bachelor"]} {round(ratio_edu["bachelor"], 2)}%
	Jumlah responden dengan pendidikan S2: {resp_edu["master"]} {round(ratio_edu["master"], 2)}%
	Jumlah responden dengan pendidikan S3: {resp_edu["doctorate"]} {round(ratio_edu["doctorate"], 2)}%
	Total responden: {resp_edu["total"]}
	""")
	get_respondent_education_piechart(resp_edu)


def print_respondent_profession():
	resp_prof = get_respondent_profession_data()
	ratio_prof = get_respondent_profession_ratio(resp_prof)

	print(f"""
	Jumlah responden dengan profesi sebagai berikut:
	PNS: {resp_prof["government_worker"]} {round(ratio_prof["government_worker"], 2)}%
	Pegawai Swasta: {resp_prof["private_worker"]} {round(ratio_prof["private_worker"], 2)}%
	Wiraswasta: {resp_prof["entrepreneur"]} {round(ratio_prof["entrepreneur"], 2)}%
	TNI/Polisi: {int(resp_prof["military"]) + int(resp_prof["police"])} {round((ratio_prof["military"] + ratio_prof["police"]), 2)}%
	Freelancer: {resp_prof["freelancer"]} {round(ratio_prof["freelancer"], 2)}%
	Lain-lain: {resp_prof["others"]} {round(ratio_prof["others"], 2)}%
	Total responden: {resp_prof["total"]}
	""")
	get_respondent_profession_piechart(resp_prof)


def print_cases(cases, case_name):
	print(f"""
	Jumlah kasus {case_name}: {cases.always + cases.often + cases.sometimes} {round((cases.always + cases.often + cases.sometimes) / cases.total_resp * 100, 2)}%
	Jumlah responden yang selalu melakukan {case_name}: {cases.always} {round(cases.get_ratio()["always"], 2)}%
	Jumlah responden yang sering melakukan {case_name}: {cases.often} {round(cases.get_ratio()["often"], 2)}%
	Jumlah responden yang kadang-kadang melakukan {case_name}: {cases.sometimes} {round(cases.get_ratio()["sometimes"], 2)}%
	Jumlah responden yang tidak pernah melakukan {case_name}: {cases.never} {round(cases.get_ratio()["never"], 2)}%
	""")

	cases.get_piechart()


def print_bar_graph():
	print(f"""
	Inilah grafik batang dari kasus korupsi yang didapat dari responden:
	""")

	get_bar_plot()


def print_final():
	avg = get_all_average_score()
	statement = "BEBAS DARI KORUPSI"
	ipk = "0.00"
	if 1.00 <= avg <= 1.75:
		statement = "TIDAK BEBAS DARI KORUPSI"
		ipk = "25-43.75"
	elif 1.76 <= avg <= 2.50:
		statement = "KURANG BERSIH DARI KORUPSI"
		ipk = "43.76-62.50"
	elif 2.51 <= avg <= 3.25:
		statement = "CUKUP BERSIH DARI KORUPSI"
		ipk = "62.51-81.25"
	elif 3.26 <= avg <= 4.00:
		statement = "BEBAS DARI KORUPSI"
		ipk = "81.26-100"
	print(f"""
	Indeks {avg} jika dikonversi menjadi presentase menjadi {(avg / 2) * 50}% yang selanjutnya jika dikonversikan dalam tabel persepsi,
	maka skor indeks tersebut masuk pada persepsi kinerja unit pelayanan {statement}, dimana nilai interval konversi Indeks Persepsi Korupsi berada pada angka {ipk}
	""")


def print_footer():
	print("""
	====== Anti-Korupsi Data Simulation ======
	""")
