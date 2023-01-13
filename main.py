from src.prints import print_header, print_footer, print_cases, print_respondent_gender, print_respondent_education, \
	print_respondent_profession, print_bar_graph, print_final
from src.cases import get_rule_manipulation_cases, get_power_abuse, get_affection_selling, get_suap, get_calo, \
	get_cheat, get_black_market, get_all_average_score
import os


def main():
	opt = input("""
	Opsi program: 
	1. Cetak jenis kelamin respondensi
	2. Cetak pendidikan terakhir respondensi
	3. Cetak profesi respondensi
	4. Cetak kasus korupsi
	5. Cetak grafik batang
	6. Cetak semua1
	9. Closing statement dan keluar program
	
	Input: """)
	if opt == "1":
		os.system("cls")
		print_header()
		print_respondent_gender()
		print_footer()
	elif opt == "2":
		os.system("cls")
		print_header()
		print_respondent_education()
		print_footer()
	elif opt == "3":
		os.system("cls")
		print_header()
		print_respondent_profession()
		print_footer()
	elif opt == "4":
		os.system("cls")
		print_header()
		print_cases(get_rule_manipulation_cases(), "manipulasi aturan")
		print_cases(get_power_abuse(), "penyalahgunaan kekuasaan")
		print_cases(get_affection_selling(), "menjual pengaruh")
		print_cases(get_suap(), "suap")
		print_cases(get_calo(), "pencaloan")
		print_cases(get_cheat(), "kecurangan")
		print_cases(get_black_market(), "transaksi rahasia")
		print_footer()
	elif opt == "5":
		os.system("cls")
		print_bar_graph()
		print_header()
	elif opt == "6":
		os.system("cls")
		print_header()
		print_respondent_gender()
		print_respondent_education()
		print_respondent_profession()
		print_cases(get_rule_manipulation_cases(), "manipulasi aturan")
		print_cases(get_power_abuse(), "penyalahgunaan kekuasaan")
		print_cases(get_affection_selling(), "menjual pengaruh")
		print_cases(get_suap(), "suap")
		print_cases(get_calo(), "pencaloan")
		print_cases(get_cheat(), "kecurangan")
		print_cases(get_black_market(), "transaksi rahasia")
		print_bar_graph()
		print_footer()
	elif opt == "9":
		os.system("cls")
		print_header()
		print_final()
		print_footer()
		exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	while True:
		main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
