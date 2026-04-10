import time
from helpers.Helpers import clear_console
from dfs.DFS import HospitalGraph
from helpers import Constant


class Application():
    def __init__(self):
        super().__init__

    def start_screen(self):
        START_SCREEN = """
            ╔════════════════════════════════════════════════════════════╗
            ║                                                            ║
            ║          ANDA COMMUNITY HOSPITAL DEPENDENCY SYSTEM         ║
            ║                                                            ║
            ║                  🏥 Bayan ng Anda                          ║
            ║                  📋 Lalawigan ng Pangasinan                ║
            ║                  👥 2026                                   ║
            ║                                                            ║
            ╚════════════════════════════════════════════════════════════╝
            """
        print(f'{START_SCREEN}\n')
        time.sleep(2)

    
    def view_graph_adjacency_list(self):
        nodes = {
            "assessment": ["er_triage", "opd_triage"],
            "er_triage": ["basic_test"],
            "opd_triage": ["family_medicine"],
            "basic_test": ["hospitalized"],
            "family_medicine": ["tests", "hospitalized", "discharged"],
            "tests": ["surgeon", "internal", "geriatrics", "pediatrics","discharged"],
            "surgeon": ["hospitalized"],
            "hospitalized": ["family_medicine", "surgeon", "discharged"],
            "pediatrics": ["discharged"],
            "internal": ["discharged"],
            "geriatrics": ["discharged"],
            "discharged": []
        }
        print("--- ADJACENCY LIST REPRESENTATION ---")
        for node, neighbors in nodes.items():
            print(f"{node.upper():<15} -> {neighbors}")
        return nodes

    def view_graph_adjacency_matrix(self):
        labels = ["assess", "er_tri", "opd_tri", "basic", "fam_med", "tests", "surg", "hosp", "pedia", "intern", "geria", "disch"]
        matrix = [
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # assessment
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # er_triage
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # opd_triage
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # basic_test
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], # family_medicine
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1], # tests
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # surgeon
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], # hospitalized
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # pediatrics
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # internal
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # geriatrics
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # discharged
        ]
        
        print("--- ADJACENCY MATRIX ---")
        header = " " * 8 + " ".join([f"{l:>6}" for l in labels])
        print(header)
        
        for i, row in enumerate(matrix):
            row_str = " ".join([f"{val:>6}" for val in row])
            print(f"{labels[i]:<8} [{row_str} ]")
            
        return matrix

    def view_visual_graph(self):
        visual_hospital = HospitalGraph()
        visual_hospital.print_graph()

    def menu_answer_1(self):
        print('Welcome to the Anda Community Hospital Dependency System!') 
        print('The system is design to show the patient flow network from assessment to discharge.') 
        print("""\n\n\n\nGRAPH DEFINITION
            G = (V, E) where:
            V = {assessment, er_triage, opd_triage, basic_test, family_medicine, additional_tests, 
                surgery_doc, hospitalized, pediatrics, internal, geriatrics, release_the_patient_from_medical_care}

            |V| = 12 vertices""")  
        print("""\n Edge connections
            1. assessment → er_triage
            2. assessment → opd_triage
                
            3. er_triage → basic_test

            4. basic_test → hospitalized

            5. hospitalized → family_medicine
            6. hospitalized → Surgery_doc
            7. hospitalized → release_the_patient_from_medical_care
                
            8. opd_triage → family_medicine
                
            9. family_medicine → hospitalized
            10. family_medicine → release_the_patient_from_medical_care
            11. family_medicine → Additional Tests

            12. additional_tests → surgery_doc
            13. additional_tests → internal
            14. additional_tests → geriatrics
            15. additional_tests → pediatrics
                
            16. surgery_doc → hospitalized

            17. internal → release_the_patient_from_medical_care
            18. pediatrics → release_the_patient_from_medical_care
            19. geriatrics → release_the_patient_from_medical_care""")  

        while True:
            print("""\nViewing the current graph.
                  Press 1 to view the graph in an adjacency matrix.
                  Press 2 to view the graph in list representation.
                  Press 3 to view the graph in visual graph.
                  """) 
            answer = input(': ')         
            clear_console()   
            if answer == '1':
                self.view_graph_adjacency_matrix()
            elif answer == '2':
                self.view_graph_adjacency_list()
            else:
                self.view_visual_graph()     
            print("""\n
                  Press 0 to go back in the view section
                  Press 1 to run the DFS
                  """) 
            answer = input(': ')         
            clear_console()   
            if answer == '1':
                break 
        
        hospital = HospitalGraph()
        hospital.dfs(1)

        while True:
            print("""\n
                    Press 1 to detect a cycle
                    """) 
            answer = input(': ')         
            clear_console()   
            if answer == '1':
                break 
        hospital.detect_cycles()
        # detect cycle
        while True:
            print("""\n
                    Press 1 to find all paths
                    """) 
            answer = input(': ')         
            clear_console()   
            if answer == '1':
                break 
        # find all paths

        while True:
            print("""\n
                    Press 1 to try and input a patient
                    """) 
            answer = input(': ')         
            clear_console()   
            if answer == '1':
                age_input = int(input(f"Enter patient age: "))
                gender_input = str(input(f"Enter patient gender: "))
                urgent_input = str(input(f"Is the illness considered life-threatening Y/N?: ")).lower()
                break
        visual_hospital = HospitalGraph()

        if urgent_input =='y':
            if int(age_input) <= 21 and age_input != 0:
                visual_hospital.update_adj_list(Constant.ER_AND_PEDIATRIC)
            if int(age_input) >= 21 and age_input <= 74:
                visual_hospital.update_adj_list(Constant.ER_AND_INTERNAL)
            if int(age_input) >= 75:
                visual_hospital.update_adj_list(Constant.ER_AND_GERIATRIC)
        if urgent_input == 'n':
            if int(age_input) <= 21 and age_input != 0:
                visual_hospital.update_adj_list(Constant.NON_ER_AND_PEDIATRIC)
            if int(age_input) >= 21 and age_input <= 74:
                visual_hospital.update_adj_list(Constant.NON_ER_AND_INTERNAL)
            if int(age_input) >= 75:
                visual_hospital.update_adj_list(Constant.NON_ER_AND_GERIATRIC)
        while True:
            print("""\n
                    Press 0 to run DFS
                    Press 1 to show updated graph w/ patient details
                    Press 2 to detect cycles
                    Press 3 to exit
                    """) 
            answer = input(': ')         
            clear_console()
            if answer == '0':
                clear_console()
                visual_hospital.dfs(1)
            elif answer == '1':
                clear_console()
                visual_hospital.print_graph(age=age_input, gender=gender_input, urgent=urgent_input)
            elif answer == '2':
                clear_console()
                visual_hospital.detect_cycles()
            elif answer == '3':
                break
            else:
                print("Invalid input. Please try again.")



if __name__ == "__main__":
    start = Application()
    start.start_screen()
    start.menu_answer_1()