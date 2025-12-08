import csv
from contextlib import nullcontext
import pandas as pd
import upload


class import_data():
    def __init__(self):
        self.data = "data/SpdCoach 2499775 20250920 0403PM.csv"         #need to make interactive
        #self.data = f"data/{input('Enter file name: ')}"
        self.df = pd.read_csv(self.data)
        self.name = "Martijn"
        for i, row in self.df.iterrows():
            row_text = " ".join(str(v) for v in row.values)  # convert full row to a string

            if "Per-Stroke Data:" in row_text:
                #print("Switch triggered at row:", i)
                x = i

        with open("temp_generaldata.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for i, row in self.df.iterrows():
                if i >= x - 2:
                    break
                writer.writerow(row)


        with open("temp_strokedata.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for i, row in self.df.iterrows():
                #if i == x + 2:
                #    writer.writerow(row)
                if i <= x+3:
                    continue

                writer.writerow(row)

    def general_data(self, id, time_zone = -5, comments = "NaN"):

        self.general = "temp_generaldata.csv"
        self.gendf = pd.read_csv(self.general, header=None, sep=",", engine="python")
        #print(self.gendf)
        name = f"{self.gendf.iloc[2, 1]}:{self.gendf.iloc[3, 5]}"  # row 3, column 2
        timezone = time_zone
        date = self.gendf.iloc[2, 1] #4,2
        self.id = id
        comments = comments
        type = self.gendf.iloc[3, 1]
        distance = self.gendf.iloc[14, 1]
        stroke_rate = self.gendf.iloc[14, 8]
        workout_type = "rowing"
        time = self.gendf.iloc[14,3]
        source = self.gendf.iloc[1, 5]
        average_hr = self.gendf.iloc[14,12]


        d = {
            "Filename": name,
            "timezone": timezone,
            "date": date,
            "id": id,
            "comments": comments,
            # "calories_total": calories_total,
            "type": type,
            "distance": distance,
            "stroke_rate": stroke_rate,
            "workout_type": workout_type,
            "time": time,
            "source": source,
            "average": average_hr,
            # "max": max_hr,
            # "min": min_hr,
            # "recovery": recovery_hr
        }
        u_gen = upload.baseObject()
        u_gen.set(d)
        u_gen.insert(table="workouts")


        distance = self.gendf.iloc[21, 1]
        stroke_rate = float(self.gendf.iloc[21, 8])
        time = self.gendf.iloc[21,3]
        average_hr = self.gendf.iloc[21,12]
        spnr = self.gendf.iloc[21, 0]

        d_split = {
            "stroke_rate": stroke_rate,
            "time": time,
            "distance": distance,
            "Splitnr": spnr,
            "average_hr": average_hr,
            "id": self.id,
        }

        u_set = upload.baseObject()
        u_set.set(d_split)
        u_set.insert(table="splits")
        #return d, d_split


    def stroke_data(self):
        self.general = "temp_strokedata.csv"
        self.stdf = pd.read_csv(self.general, header=None, sep=",", engine="python")
        #print(self.stdf)
        stroke = {}
        for i, row in self.stdf.iterrows():
            d_stroke = {
                "strokenr": int(self.stdf.iloc[i, 9]),
                "p": self.stdf.iloc[i, 4],
                "t": self.stdf.iloc[i, 3],
                "d": self.stdf.iloc[i, 1],
                "spm": self.stdf.iloc[i, 8],
                "hr": self.stdf.iloc[i, 12],
                "len": self.stdf.iloc[i, 10],
                "id": self.id,
            }
            u_stroke = upload.baseObject()
            u_stroke.set(d_stroke)
            u_stroke.insert(table = "strokes")

            #stroke[f"stroke_{self.stdf.iloc[i, 9]}"] = d_stroke

    def make_workout(self):
        u_workout = upload.baseObject()
        x = u_workout.getByField(self.name, "name", "users", "user_id")
        d = {
            "user_id" : x,
            "id": self.id,
        }
        u_workout.set(d)
        u_workout.insert(table="workout")

        #self.set(self.data[0])















