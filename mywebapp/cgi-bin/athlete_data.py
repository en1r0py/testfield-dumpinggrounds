from athlete_class import Athlete
import pickle

def get_athlete_data(a_filename):
    l = []
    try:
        f = open(a_filename, "r")
        l = f.readline().strip().replace(".","-").replace(":","-").split(",")
        return Athlete(l.pop(0), l.pop(0), l)

    except IOError as err:
        print "An error occurred", err

def put_to_store(files_list):
    athlete_dict = {}
    for each_file in files_list:
        a = get_athlete_data(each_file)
        athlete_dict[a.name] = a
    pickle.dump(athlete_dict,open("athletes.pik","wb"))
    return athlete_dict

def get_from_store():
    athlete_dict = pickle.load(open("athletes.pik","rb"))
    return athlete_dict

if __name__ == '__main__':
    files_list = ["sarah2", "james2", "mikey2", "julie2"]
    new_files_list = []

    for each_file in files_list:
        new_files_list.append("../data/" + each_file + ".txt")

    put_to_store(new_files_list)

    athlete_dict = get_from_store()

    for k in athlete_dict:
        print athlete_dict[k].name
        print athlete_dict[k].dob
        print athlete_dict[k]
        print "--"

