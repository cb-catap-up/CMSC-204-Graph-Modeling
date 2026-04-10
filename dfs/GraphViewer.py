class GraphViewer:
    def __init__(self,graph_nodes):
        self.graph_nodes = graph_nodes
        self.graph_names = {
            1: "Assessment",   
            2: "ER Triage",     
            3: "OPD Triage",
            4: "Basic Test",   
            5: "Family Medicine", 
            6: "Additional Tests",
            7: "Surgery Doc",      
            8: "Hospitalized",   
            9: "Pediatrics",
            10: "Internal",   
            11: "Geriatrics",    
            12: "Release the patient from medical care"
        }
        self.age = 16

    def make_inner_separator(self, left_pad, inner_spaces):
        return f"{' ' * left_pad}/{' ' * inner_spaces}\\"

    def make_outer_separator(self, left_pad, inner_spaces):
        return f"{' ' * left_pad}|/{' ' * inner_spaces}\\|"


    # for empty left
    def make_inner_separator_empty_left(self, left_pad, inner_spaces):
        return f"{' ' * left_pad}  {' ' * inner_spaces}\\"
    def make_outer_separator_empty_left(self, left_pad, inner_spaces):
        return f"{' ' * left_pad}   {' ' * inner_spaces}\\|"

    # for empty right
    def make_inner_separator_empty_right(self, left_pad, inner_spaces):
        return f"{' ' * left_pad}/{' ' * inner_spaces} "
    def make_outer_separator_empty_right(self, left_pad, inner_spaces):
        return f"{' ' * left_pad}|/{' ' * inner_spaces}  "


    def make_vertical_inner_separator(self, left_pad, inner_spaces, is_solo_left = False, is_solo_right = False):
        
        if is_solo_right:
            return f"{' ' * left_pad}|"
        
        if is_solo_left:
            return f"{' ' * left_pad} {' ' * inner_spaces}|"

        return f"{' ' * left_pad}|{' ' * inner_spaces}|"
    
    def make_vertical_inner_separator_with_left_connection(self, left_pad, inner_spaces, spacer,is_solo_left = False, is_solo_right = False, header = False, footer=False):

        if is_solo_left and header:
            return f"{' ' * left_pad} {' ' * (inner_spaces-spacer)}/|{' ' * (spacer-2)}|{' '*43}|"
        elif is_solo_left and footer:
            return f"{' ' * left_pad} {' ' * (inner_spaces-spacer-2)}|/{' ' * (spacer-1)}\|/{' '*42}|"
        elif is_solo_right:
            return f"{' ' * left_pad}|"
        elif is_solo_left:
            return f"{' ' * left_pad} {' ' * (inner_spaces-spacer)}/{' ' * (spacer-1)}|{' '*43}|"
        elif header:
            return f"{' ' * left_pad}|{' ' * (inner_spaces-spacer)}/|{' ' * (spacer-2)}|{' '*43}|"
        elif footer:
            return f"{' ' * (left_pad-1)}\|/{' ' * (inner_spaces-spacer-3)}|/{' ' * (spacer-1)}\|/{' '*42}|"

        return f"{' ' * left_pad}|{' ' * (inner_spaces-spacer)}/{' ' * (spacer-1)}|{' '*43}|"


    def make_vertical_outer_separator(self, left_pad, inner_spaces, is_solo_left = False, is_solo_right = False):
        if is_solo_right:
            return f"{' ' * left_pad}\|/"
        if is_solo_left:
            return f"{' ' * left_pad}   {' ' * inner_spaces}\|/"

        return f"{' ' * left_pad}\|/{' ' * inner_spaces}\|/"

    def vertex_name_formatter(self,input_string, spacing):
        print(f"{' '*spacing} {'—'*(len(input_string)+2)}")
        print(f"{' '*spacing}| {input_string} |")
        print(f"{' '*spacing} {'—'*(len(input_string)+2)}")

    def end_vertex_name_formatter(self, input_string, spacing):
        print(f"{' '*28}|{' '*(spacing-38)} {'—'*(len(input_string)+2)}{' '*17}|")
        print(f"{' '*28}|{'—'*(spacing-39)}>| {input_string} |<{'—'*15}|")
        print(f"{' '*28}{' '*(spacing-37)} {'—'*(len(input_string)+2)}")

    def two_node_vertex_name_formatter(self, first_string, start_spacing, middle_spacing, second_string, is_connected = False, empty_first= False, empty_second = False, is_end_connected = False, spacer = 0):
        separator =  ' '*middle_spacing
        first_spacer = '—'*(len(first_string)+2)

        second_spacer = '—'*(len(second_string)+2)
        if is_connected:
            separator = f" <{'—'*(middle_spacing-4)}> "

        mid_spacer =f"{' '*start_spacing}| {first_string} |{separator}| {second_string} |"

        if is_end_connected and spacer != 0:
            mid_spacer =  f"{mid_spacer}{' ' * spacer}|"
        elif is_end_connected:
            mid_spacer =  f"{mid_spacer}{'—' * 34}"

        if empty_first:
            first_string = " "*len(first_string)
            first_spacer = " "*(len(first_string)+2)
            mid_spacer = f"{' '*start_spacing}  {first_string}  {separator}| {second_string} |"
            if is_end_connected:
                mid_spacer = f"{' '*start_spacing}  {first_string}  {separator}| {second_string} |{'—' * 34}"
        if empty_second:
            second_string = " "*len(second_string)
            second_spacer = " "*(len(second_string)+2)
            mid_spacer = f"{' '*start_spacing}| {first_string} |{separator}  {second_string}  "
        ender = f"{' '*start_spacing} {first_spacer}{' '*middle_spacing}  {second_spacer}"
        starter = f"{' '*start_spacing} {first_spacer}{' '*middle_spacing}  {second_spacer}"
        if is_end_connected and spacer != 0:
            starter = f"{' '*start_spacing} {first_spacer}{' '*middle_spacing}  {second_spacer}{' ' *29}|"
            ender = f"{' '*start_spacing} {first_spacer}{' '*middle_spacing}  {second_spacer}{' ' *29}|"
        elif is_end_connected:
            ender = f"{' '*start_spacing} {first_spacer}{' '*middle_spacing}  {second_spacer}{' ' *34}|"
        print(starter)
        print(f"{mid_spacer}")
        print(ender)

    def four_node_vertex_name_formatter(self,
                                        first_string,
                                        second_string,
                                        third_string,
                                        fourth_string,
                                        start_spacing,
                                        middle_spacing,
                                        initial_spacing,
                                        age = 0):
        if age == 0:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}| {second_string} |{' '*middle_spacing}| {third_string} |{' '*middle_spacing}| {fourth_string} |{' '*6}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")

        if int(age) <= 21 and age != 0:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}| {second_string} |{' '*middle_spacing}  {' '*len(third_string)}  {' '*middle_spacing}  {' '*len(fourth_string)}  {' '*6}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")
        if int(age) >= 21 and age <= 74:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}  {' '*len(second_string)}  {' '*middle_spacing}| {third_string} |{' '*middle_spacing}  {' '*len(fourth_string)}  {' '*6}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")
        if int(age) >= 75:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}  {' '*len(second_string)}  {' '*middle_spacing}  {' '*len(third_string)}  {' '*middle_spacing}| {fourth_string} |{' '*6}|")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}{' '*5}|")
        # this prints the separator with 4 nodes
    def fourth_level_separators_and_pointers(self, age = 0):
        if age == 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5}|{' '*10}|{' '*5}\\{' '* 25}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6}|{' '*10}|{' '*6}\\{' '* 24}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7}|{' '*10}|{' '*7}\\{' '* 23}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8}|{' '*10}|{' '*8}\\{' '* 22}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9}|{' '*10}|{' '*9}\\{' '* 21}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}\|/{' '*8}\|/{' '*9}\\|{' '* 19}|")
        if int(age) <= 21 and age != 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5}|{' '*10} {' '*5} {' '* 25}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6}|{' '*10} {' '*6} {' '* 24}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7}|{' '*10} {' '*7} {' '* 23}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8}|{' '*10} {' '*8} {' '* 22}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9}|{' '*10} {' '*9} {' '* 21}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}\|/{' '*8}   {' '*9}  {' '* 19}|")
        if int(age) >= 21 and age <= 74:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5} {' '*10}|{' '*5} {' '* 25}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6} {' '*10}|{' '*6} {' '* 24}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7} {' '*10}|{' '*7} {' '* 23}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8} {' '*10}|{' '*8} {' '* 22}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9} {' '*10}|{' '*9} {' '* 21}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}   {' '*8}\|/{' '*9}  {' '* 19}|")
        if int(age) >= 75:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5} {' '*10} {' '*5}\\{' '* 25}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6} {' '*10} {' '*6}\\{' '* 24}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7} {' '*10} {' '*7}\\{' '* 23}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8} {' '*10} {' '*8}\\{' '* 22}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9} {' '*10} {' '*9}\\{' '* 21}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}   {' '*8}   {' '*9}\\|{' '* 19}|")
# here

    def fifth_level_separators_and_pointers(self, age = 0):
        if age == 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9}|{' '*14}|{' '*16}/{' '*10}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9}|{' '*14}|{' '*15}/{' '*11}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9}|{' '*14}|{' '*14}/{' '*12}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9}|{' '*14}|{' '*13}/{' '*13}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9}|{' '*14}|{' '*12}/{' '*14}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9}|{' '*14}|{' '*11}/{' '*15}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9}|{' '*14}|{' '*10}/{' '*16}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9}|{' '*14}|{' '*9}/{' '*17}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9}|{' '*14}|{' '*8}/{' '*18}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9}|{' '*14}|{' '*7}/{' '*19}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9}|{' '*14}|{' '*6}/{' '*20}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}\|/{' '*12}\|/{' '*3}|/{' '*21}|")
        if int(age) <= 21 and age != 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9}|{' '*14} {' '*16}{' '* 11}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9}|{' '*14} {' '*15}{' '* 12}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9}|{' '*14} {' '*14}{' '* 13}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9}|{' '*14} {' '*13}{' '* 14}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9}|{' '*14} {' '*12}{' '* 15}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9}|{' '*14} {' '*11}{' '* 16}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9}|{' '*14} {' '*10}{' '* 17}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9}|{' '*14} {' '*9}{' '* 18}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9}|{' '*14} {' '*8}{' '* 19}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9}|{' '*14} {' '*7}{' '* 20}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9}|{' '*14} {' '*6}{' '* 21}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}\|/{' '*12}   {' '*3}  {' '* 21}|")
        if int(age) >= 21 and age <= 74:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9} {' '*14}|{' '*16}{' '* 11}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9} {' '*14}|{' '*15}{' '* 12}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9} {' '*14}|{' '*14}{' '* 13}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9} {' '*14}|{' '*13}{' '* 14}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9} {' '*14}|{' '*12}{' '* 15}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9} {' '*14}|{' '*11}{' '* 16}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9} {' '*14}|{' '*10}{' '* 17}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9} {' '*14}|{' '*9}{' '* 18}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9} {' '*14}|{' '*8}{' '* 19}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9} {' '*14}|{' '*7}{' '* 20}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9} {' '*14}|{' '*6}{' '* 21}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}   {' '*12}\|/{' '*3}  {' '* 21}|")
        if int(age) >= 75:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9} {' '*14} {' '*16}/{' '* 10}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9} {' '*14} {' '*15}/{' '* 11}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9} {' '*14} {' '*14}/{' '* 12}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9} {' '*14} {' '*13}/{' '* 13}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9} {' '*14} {' '*12}/{' '* 14}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9} {' '*14} {' '*11}/{' '* 15}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9} {' '*14} {' '*10}/{' '* 16}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9} {' '*14} {' '*9}/{' '* 17}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9} {' '*14} {' '*8}/{' '* 18}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9} {' '*14} {' '*7}/{' '* 19}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9} {' '*14} {' '*6}/{' '* 20}|")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}   {' '*12}   {' '*3}|/{' '* 21}|")

    def view_all_graph(self):

        # first level separators
        separator_for_1_first_level  = self.make_inner_separator(41, 3)
        separator_for_1_second_level = self.make_inner_separator(40, 5)
        separator_for_1_third_level  = self.make_inner_separator(39, 7)
        separator_for_1_fourth_level = self.make_inner_separator(38, 9)
        separator_for_1_fifth_level  = self.make_inner_separator(37, 11)
        separator_for_1_sixth_level  = self.make_outer_separator(35, 13)
        # second level separators
        separator_for_2_first_level  = self.make_inner_separator(32, 20)
        separator_for_2_second_level = self.make_inner_separator(31, 22)
        separator_for_2_third_level  = self.make_inner_separator(30, 24)
        separator_for_2_fourth_level = self.make_outer_separator(28, 26)

        separator_for_3_first_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=11, header = True)
        separator_for_3_second_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=12)
        separator_for_3_third_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=13)
        separator_for_3_fourth_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=14)
        separator_for_3_fifth_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=15)
        separator_for_3_sixth_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=16)
        separator_for_3_seventh_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=17)
        separator_for_3_eight_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=17, footer=True)


        self.vertex_name_formatter(self.graph_names[1], 37)
        print(separator_for_1_first_level)
        print(separator_for_1_second_level)
        print(separator_for_1_third_level)
        print(separator_for_1_fourth_level)
        print(separator_for_1_fifth_level)
        print(separator_for_1_sixth_level)
        self.two_node_vertex_name_formatter(start_spacing=28, first_string=self.graph_names[2], middle_spacing=4, second_string=self.graph_names[3])
        print(separator_for_2_first_level)
        print(separator_for_2_second_level)
        print(separator_for_2_third_level)
        print(separator_for_2_fourth_level)
        self.two_node_vertex_name_formatter(start_spacing=22, first_string=self.graph_names[4], middle_spacing=13, second_string=self.graph_names[5], is_end_connected=True)
        print(separator_for_3_first_level)
        print(separator_for_3_second_level)
        print(separator_for_3_third_level)
        print(separator_for_3_fourth_level)
        print(separator_for_3_fifth_level)
        print(separator_for_3_sixth_level)
        print(separator_for_3_seventh_level)
        print(separator_for_3_eight_level)
        self.two_node_vertex_name_formatter(start_spacing=21, first_string=self.graph_names[8], middle_spacing=16, second_string=self.graph_names[6],is_end_connected=True, spacer=28)
        self.fourth_level_separators_and_pointers()
        self.four_node_vertex_name_formatter(start_spacing=28,
                                        first_string=self.graph_names[7],
                                        second_string=self.graph_names[9],
                                        third_string=self.graph_names[10],
                                        fourth_string=self.graph_names[11],
                                        middle_spacing=2,
                                        initial_spacing=5)
        self.fifth_level_separators_and_pointers()
        self.end_vertex_name_formatter(self.graph_names[12], 53)
    
    def view_non_er_graph(self, age):
        # empty left for first level
        separator_for_1_first_level  = self.make_inner_separator_empty_left(41, 3)
        separator_for_1_second_level = self.make_inner_separator_empty_left(40, 5)
        separator_for_1_third_level  = self.make_inner_separator_empty_left(39, 7)
        separator_for_1_fourth_level = self.make_inner_separator_empty_left(38, 9)
        separator_for_1_fifth_level  = self.make_inner_separator_empty_left(37, 11)
        separator_for_1_sixth_level  = self.make_outer_separator_empty_left(35, 13)
        # second level separators
        separator_for_2_first_level  = self.make_inner_separator(32, 20)
        separator_for_2_second_level = self.make_inner_separator(31, 22)
        separator_for_2_third_level  = self.make_inner_separator(30, 24)
        separator_for_2_fourth_level = self.make_outer_separator(28, 26)

        # empty left for second level
        separator_for_2_first_level  = self.make_inner_separator_empty_left(32, 20)
        separator_for_2_second_level = self.make_inner_separator_empty_left(31, 22)
        separator_for_2_third_level  = self.make_inner_separator_empty_left(30, 24)
        separator_for_2_fourth_level = self.make_outer_separator_empty_left(28, 26)

        # empty left

        separator_for_3_first_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=11, header = True,is_solo_left=True)
        separator_for_3_second_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=12,is_solo_left=True)
        separator_for_3_third_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=13, is_solo_left=True)
        separator_for_3_fourth_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=14, is_solo_left=True)
        separator_for_3_fifth_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=15, is_solo_left=True)
        separator_for_3_sixth_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=16, is_solo_left=True)
        separator_for_3_seventh_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=17, is_solo_left=True)
        separator_for_3_eight_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=17, footer=True, is_solo_left=True)


        self.vertex_name_formatter(self.graph_names[1], 37)
        print(separator_for_1_first_level)
        print(separator_for_1_second_level)
        print(separator_for_1_third_level)
        print(separator_for_1_fourth_level)
        print(separator_for_1_fifth_level)
        print(separator_for_1_sixth_level)
        self.two_node_vertex_name_formatter(start_spacing=28, first_string=self.graph_names[2], middle_spacing=4, second_string=self.graph_names[3], empty_first=True)
        print(separator_for_2_first_level)
        print(separator_for_2_second_level)
        print(separator_for_2_third_level)
        print(separator_for_2_fourth_level)
        self.two_node_vertex_name_formatter(start_spacing=22, first_string=self.graph_names[4], middle_spacing=13, second_string=self.graph_names[5], empty_first= True, is_end_connected=True)
        print(separator_for_3_first_level)
        print(separator_for_3_second_level)
        print(separator_for_3_third_level)
        print(separator_for_3_fourth_level)
        print(separator_for_3_fifth_level)
        print(separator_for_3_sixth_level)
        print(separator_for_3_seventh_level)
        print(separator_for_3_eight_level)
        self.two_node_vertex_name_formatter(start_spacing=21, first_string=self.graph_names[8], middle_spacing=16, second_string=self.graph_names[6],is_end_connected=True, spacer=28)
        self.fourth_level_separators_and_pointers(age=age)
        self.four_node_vertex_name_formatter(start_spacing=28,
                                        first_string=self.graph_names[7],
                                        second_string=self.graph_names[9],
                                        third_string=self.graph_names[10],
                                        fourth_string=self.graph_names[11],
                                        middle_spacing=2,
                                        initial_spacing=5,
                                        age=age)
        self.fifth_level_separators_and_pointers(age=age)
        self.end_vertex_name_formatter(self.graph_names[12], 53)
    
    def view_er_graph(self, age):
        # empty left for first level
        separator_for_1_first_level  = self.make_inner_separator_empty_right(41, 3)
        separator_for_1_second_level = self.make_inner_separator_empty_right(40, 5)
        separator_for_1_third_level  = self.make_inner_separator_empty_right(39, 7)
        separator_for_1_fourth_level = self.make_inner_separator_empty_right(38, 9)
        separator_for_1_fifth_level  = self.make_inner_separator_empty_right(37, 11)
        separator_for_1_sixth_level  = self.make_outer_separator_empty_right(35, 13)


        # empty left for second level
        separator_for_2_first_level  = self.make_inner_separator_empty_right(32, 20)
        separator_for_2_second_level = self.make_inner_separator_empty_right(31, 22)
        separator_for_2_third_level  = self.make_inner_separator_empty_right(30, 24)
        separator_for_2_fourth_level = self.make_outer_separator_empty_right(28, 26)

        # empty left
        separator_for_3_first_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=11, header = True)
        separator_for_3_second_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=12)
        separator_for_3_third_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=13)
        separator_for_3_fourth_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=14)
        separator_for_3_fifth_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=15)
        separator_for_3_sixth_level  = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=16)
        separator_for_3_seventh_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=17)
        separator_for_3_eight_level = self.make_vertical_inner_separator_with_left_connection(left_pad=28, inner_spaces=28,spacer=17, footer=True)


        self.vertex_name_formatter(self.graph_names[1], 37)
        print(separator_for_1_first_level)
        print(separator_for_1_second_level)
        print(separator_for_1_third_level)
        print(separator_for_1_fourth_level)
        print(separator_for_1_fifth_level)
        print(separator_for_1_sixth_level)
        self.two_node_vertex_name_formatter(start_spacing=28, first_string=self.graph_names[2], middle_spacing=4, second_string=self.graph_names[3], empty_second=True)
        print(separator_for_2_first_level)
        print(separator_for_2_second_level)
        print(separator_for_2_third_level)
        print(separator_for_2_fourth_level)
        self.two_node_vertex_name_formatter(start_spacing=22, first_string=self.graph_names[4], middle_spacing=13, second_string=self.graph_names[5], is_end_connected=True)
        print(separator_for_3_first_level)
        print(separator_for_3_second_level)
        print(separator_for_3_third_level)
        print(separator_for_3_fourth_level)
        print(separator_for_3_fifth_level)
        print(separator_for_3_sixth_level)
        print(separator_for_3_seventh_level)
        print(separator_for_3_eight_level)
        self.two_node_vertex_name_formatter(start_spacing=21, first_string=self.graph_names[8], middle_spacing=16, second_string=self.graph_names[6],is_end_connected=True, spacer=28)
        self.fourth_level_separators_and_pointers(age=age)
        self.four_node_vertex_name_formatter(start_spacing=28,
                                        first_string=self.graph_names[7],
                                        second_string=self.graph_names[9],
                                        third_string=self.graph_names[10],
                                        fourth_string=self.graph_names[11],
                                        middle_spacing=2,
                                        initial_spacing=5,
                                        age=age)
        self.fifth_level_separators_and_pointers(age=age)
        self.end_vertex_name_formatter(self.graph_names[12], 53)