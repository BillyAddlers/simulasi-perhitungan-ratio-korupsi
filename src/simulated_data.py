from matplotlib import pyplot
from numpy import array


def get_respondent_gender_data():
	male = 1101
	female = 624
	return {
		"male": male,
		"female": female,
		"total": male + female
	}


def get_respondent_gender_data_ratio(data):
	male_data = int(data["male"])
	female_data = int(data["female"])
	total_data = male_data + female_data
	male_percent = (male_data / total_data) * 100
	female_percent = (female_data / total_data) * 100
	return {
		"male": male_percent,
		"female": female_percent
	}


def get_respondent_gender_piechart(data):
	male_data = int(data["male"])
	female_data = int(data["female"])
	data = array([male_data, female_data])

	pyplot.pie(data, labels=["Male", "Female"])
	pyplot.show()


def get_respondent_education_data():
	under_highschool = 2
	highschool = 185
	diploma1 = 3
	diploma2 = 13
	diploma3 = 90
	bachelor = 906
	master = 485
	doctorate = 41
	return {
		"under_highschool": under_highschool,
		"highschool": highschool,
		"diploma1": diploma1,
		"diploma2": diploma2,
		"diploma3": diploma3,
		"bachelor": bachelor,
		"master": master,
		"doctorate": doctorate,
		"total": under_highschool + highschool + diploma1 + diploma2 + diploma3 + bachelor + master + doctorate
	}


def get_respondent_education_ratio(data):
	under_highschool = int(data["under_highschool"])
	highschool = int(data["highschool"])
	diploma1 = int(data["diploma1"])
	diploma2 = int(data["diploma2"])
	diploma3 = int(data["diploma3"])
	bachelor = int(data["bachelor"])
	master = int(data["master"])
	doctorate = int(data["doctorate"])
	total = under_highschool + highschool + diploma1 + diploma2 + diploma3 + bachelor + master + doctorate
	under_highschool_percent = (under_highschool / total) * 100
	highschool_percent = (highschool / total) * 100
	diploma1_percent = (diploma1 / total) * 100
	diploma2_percent = (diploma2 / total) * 100
	diploma3_percent = (diploma3 / total) * 100
	bachelor_percent = (bachelor / total) * 100
	master_percent = (master / total) * 100
	doctorate_percent = (doctorate / total) * 100
	return {
		"under_highschool": under_highschool_percent,
		"highschool": highschool_percent,
		"diploma1": diploma1_percent,
		"diploma2": diploma2_percent,
		"diploma3": diploma3_percent,
		"bachelor": bachelor_percent,
		"master": master_percent,
		"doctorate": doctorate_percent
	}


def get_respondent_education_piechart(data):
	under_highschool = int(data["under_highschool"])
	highschool = int(data["highschool"])
	diploma1 = int(data["diploma1"])
	diploma2 = int(data["diploma2"])
	diploma3 = int(data["diploma3"])
	bachelor = int(data["bachelor"])
	master = int(data["master"])
	doctorate = int(data["doctorate"])
	data = array([under_highschool, highschool, diploma1, diploma2, diploma3, bachelor, master, doctorate])

	pyplot.pie(data,
	           labels=["Under Highschool", "Highschool", "Diploma 1", "Diploma 2", "Diploma 3", "Bachelor", "Master",
	                   "Doctorate"])
	pyplot.show()


def get_respondent_profession_data():
	government_worker = 1464
	military = 4
	police = 2
	private_worker = 42
	entrepreneur = 12
	freelancer = 69
	others = 132
	return {
		"government_worker": government_worker,
		"military": military,
		"police": police,
		"private_worker": private_worker,
		"entrepreneur": entrepreneur,
		"freelancer": freelancer,
		"others": others,
		"total": government_worker + military + police + private_worker + entrepreneur + freelancer + others
	}


def get_respondent_profession_ratio(data):
	government_worker = int(data["government_worker"])
	military = int(data["military"])
	police = int(data["police"])
	private_worker = int(data["private_worker"])
	entrepreneur = int(data["entrepreneur"])
	freelancer = int(data["freelancer"])
	others = int(data["others"])
	total = government_worker + military + police + private_worker + entrepreneur + freelancer + others
	government_worker_percent = (government_worker / total) * 100
	military_percent = (military / total) * 100
	police_percent = (police / total) * 100
	private_worker_percent = (private_worker / total) * 100
	entrepreneur_percent = (entrepreneur / total) * 100
	freelancer_percent = (freelancer / total) * 100
	others_percent = (others / total) * 100
	return {
		"government_worker": government_worker_percent,
		"military": military_percent,
		"police": police_percent,
		"private_worker": private_worker_percent,
		"entrepreneur": entrepreneur_percent,
		"freelancer": freelancer_percent,
		"others": others_percent
	}


def get_respondent_profession_piechart(data):
	government_worker = int(data["government_worker"])
	military = int(data["military"])
	police = int(data["police"])
	private_worker = int(data["private_worker"])
	entrepreneur = int(data["entrepreneur"])
	freelancer = int(data["freelancer"])
	others = int(data["others"])
	data = array([government_worker, military, police, private_worker, entrepreneur, freelancer, others])

	pyplot.pie(data,
	           labels=["Government Worker", "Military", "Police", "Private Worker", "Entrepreneur", "Freelancer",
	                   "Others"])
	pyplot.show()
