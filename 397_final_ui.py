from flask import *
from scipy import spatial
from datetime import datetime
import csv


# API: given splits, calculate result
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():

    # get and parse users' current results into user_times
    _5k_split = request.args.get('5k')
    _10k_split = request.args.get('10k')
    _15k_split = request.args.get('15k')
    _20k_split = request.args.get('20k')
    _25k_split = request.args.get('25k')
    _30k_split = request.args.get('30k')
    _35k_split = request.args.get('35k')
    _40k_split = request.args.get('40k')

    results = [_5k_split, _10k_split, _15k_split, _20k_split, _25k_split, _30k_split, _35k_split, _40k_split]

    user_times = []
    # if 15k is not None; 5k, 10k also must not be none

    if _5k_split is not None:
        user_times.append(int(_5k_split))
    if _10k_split is not None:
        user_times.append(int(_10k_split))
    if _15k_split is not None:
        user_times.append(int(_15k_split))
    if _20k_split is not None:
        user_times.append(int(_20k_split))
    if _25k_split is not None:
        user_times.append(int(_25k_split))
    if _30k_split is not None:
        user_times.append(int(_30k_split))
    if _35k_split is not None:
        user_times.append(int(_35k_split))
    if _40k_split is not None:
        user_times.append(int(_40k_split))

    num_user_times = len(user_times)
    if num_user_times == 0:
        return 0

    # open array

    rows = []

    actual_times = {}
    t = 0
    with open("marathon_results_2017.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):

            lal = line[0].split(",")

            formatted = [lal[11], lal[12], lal[13], lal[14], lal[16], lal[17], lal[18], lal[19]]

            if "-" in formatted or "" in formatted:
                continue

            times = []

            if t != 0:
                a = datetime.strptime(lal[11], '%H:%M:%S')
                _5k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[12], '%H:%M:%S')
                _10k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[13], '%H:%M:%S')
                _15k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[14], '%H:%M:%S')
                _20k = a.second + a.minute * 60 + a.hour * 3600

                # lal[15] is half

                a = datetime.strptime(lal[16], '%H:%M:%S')
                _25k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[17], '%H:%M:%S')
                _30k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[18], '%H:%M:%S')
                _35k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[19], '%H:%M:%S')
                _40k = a.second + a.minute * 60 + a.hour * 3600

                a = datetime.strptime(lal[22], '%H:%M:%S')
                actual_time = a.second + a.minute * 60 + a.hour * 3600

                row = [_5k, _10k, _15k, _20k, _25k, _30k, _35k, _40k]

                row = row[0:num_user_times]
                str_row = str(row)
                actual_times[str_row] = actual_time

                rows.append(row)

            # don't do the whole thing (for test)
            # if t > 11:
            #     break
            t += 1

    # for row in rows:
    #     print(row)

    tree = spatial.KDTree(rows)

    # print(repr(actual_times))
    # test = [1, 2, 3, 4, 5, 6, 7, 8]
    # print(tree.query(test))
    # print("predicted time:", actual_times[str(rows[tree.query(test)[1]])])
    # print()

    # return "user input:" + str(user_times)+ str(rows) + "\nactual times:\n" + repr(actual_times) + "\nresult:\n" + str(actual_times[str(rows[tree.query(user_times)[1]])])
    return str(actual_times[str(rows[tree.query(user_times)[1]])])
    # ultimately returns number of seconds the runner is projected to run
    # return return_str