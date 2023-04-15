class Students:
    def __init__(self, name, program, batch, roll_no,sap_id,semester):
        self.name = name
        self.program = program
        self.batch = batch
        self.roll_no = roll_no
        self.sap_id= sap_id
        self.semester= semester

    def write_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"Name: {self.name}")
            file.write(f"Program: {self.program}")
            file.write(f"Batch: {self.batch}")
            file.write(f"Roll No: {self.roll_no}")
            file.write(f"Sap ID: {self.sap_id}")
            file.write(f"Semester: {self.semester}")
            
student = Students("Kavya Dangi", "B.Tech(cse)","35", "1184", "500108583","2nd")
student.write_to_file("classactibity.txt")

