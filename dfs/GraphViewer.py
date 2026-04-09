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
        print(f"{' '*28}|{' '*(spacing-38)} {'—'*(len(input_string)+2)}")
        print(f"{' '*28}|{'—'*(spacing-39)}>| {input_string} |")
        print(f"{' '*28}{' '*(spacing-37)} {'—'*(len(input_string)+2)}")

    def two_node_vertex_name_formatter(self, first_string, start_spacing, middle_spacing, second_string, is_connected = False, empty_first= False, empty_second = False):
        separator =  ' '*middle_spacing
        first_spacer = '—'*(len(first_string)+2)

        second_spacer = '—'*(len(second_string)+2)
        if is_connected:
            separator = f" <{'—'*(middle_spacing-4)}> "

        mid_spacer =f"{' '*start_spacing}| {first_string} |{separator}| {second_string} |"

        if empty_first:
            first_string = " "*len(first_string)
            first_spacer = " "*(len(first_string)+2)
            mid_spacer = f"{' '*start_spacing}  {first_string}  {separator}| {second_string} |"
        if empty_second:
            second_string = " "*len(second_string)
            second_spacer = " "*(len(second_string)+2)
            mid_spacer = f"{' '*start_spacing}| {first_string} |{separator}  {second_string}  "
        
        print(f"{' '*start_spacing} {first_spacer}{' '*middle_spacing}  {second_spacer}")
        print(mid_spacer)
        print(f"{' '*start_spacing} {first_spacer}{' '*middle_spacing}  {second_spacer}")

    def four_node_vertex_name_formatter(self, first_string,
                                        second_string,
                                        third_string,
                                        fourth_string,
                                        start_spacing,
                                        middle_spacing,
                                        initial_spacing,
                                        age = 0):
        if age == 0:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}| {second_string} |{' '*middle_spacing}| {third_string} |{' '*middle_spacing}| {fourth_string} |")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}")
        
        if int(age) <= 21 and age != 0:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}| {second_string} |{' '*middle_spacing}  {' '*len(third_string)}  {' '*middle_spacing}  {' '*len(fourth_string)}  ")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {'—'*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}")
        if int(age) >= 21 and age <= 74:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}  {' '*len(second_string)}  {' '*middle_spacing}| {third_string} |{' '*middle_spacing}  {' '*len(fourth_string)}  ")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {'—'*(len(third_string)+2)}{' '*middle_spacing}  {' '*(len(fourth_string)+2)}{' '*middle_spacing}")
        if int(age) >= 75:
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}")
            print(f"{' '*start_spacing}|{' '*initial_spacing}| {first_string} |{' '*middle_spacing}  {' '*len(second_string)}  {' '*middle_spacing}  {' '*len(third_string)}  {' '*middle_spacing}| {fourth_string} |")
            print(f"{' '*start_spacing}|{' '*initial_spacing} {'—'*(len(first_string)+2)}{' '*middle_spacing}  {' '*(len(second_string)+2)}{' '*middle_spacing}  {' '*(len(third_string)+2)}{' '*middle_spacing}  {'—'*(len(fourth_string)+2)}{' '*middle_spacing}")
    # this prints the separator with 4 nodes
    def fourth_level_separators_and_pointers(self, age = 0):
        if age == 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5}|{' '*10}|{' '*5}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6}|{' '*10}|{' '*6}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7}|{' '*10}|{' '*7}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8}|{' '*10}|{' '*8}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9}|{' '*10}|{' '*9}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}\|/{' '*8}\|/{' '*9}\\|")
        if int(age) <= 21 and age != 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5}|{' '*10} {' '*5}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6}|{' '*10} {' '*6}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7}|{' '*10} {' '*7}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8}|{' '*10} {' '*8}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9}|{' '*10} {' '*9}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}\|/{' '*8}   {' '*9}")
        if int(age) >= 21 and age <= 74:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5} {' '*10}|{' '*5} ")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6} {' '*10}|{' '*6} ")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7} {' '*10}|{' '*7} ")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8} {' '*10}|{' '*8} ")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9} {' '*10}|{' '*9} ")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}   {' '*8}\|/{' '*9}  ")
        if int(age) >= 75:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1} /\\{' '*19}/{' '*5} {' '*10} {' '*5}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*1}{' '*3}\\{' '*(17)}/{' '*6} {' '*10} {' '*6}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*2}{' '*3}\\{' '*(15)}/{' '*7} {' '*10} {' '*7}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*3}{' '*3}\\{' '*(13)}/{' '*8} {' '*10} {' '*8}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*4}{' '*3}\\{' '*(11)}/{' '*9} {' '*10} {' '*9}\\")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*5}   \\/{' '*7}|/{' '*9}   {' '*8}   {' '*9}\\|")

    def fifth_level_separators_and_pointers(self, age = 0):
        if age == 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9}|{' '*14}|{' '*16}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9}|{' '*14}|{' '*15}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9}|{' '*14}|{' '*14}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9}|{' '*14}|{' '*13}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9}|{' '*14}|{' '*12}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9}|{' '*14}|{' '*11}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9}|{' '*14}|{' '*10}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9}|{' '*14}|{' '*9}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9}|{' '*14}|{' '*8}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9}|{' '*14}|{' '*7}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9}|{' '*14}|{' '*6}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}\|/{' '*12}\|/{' '*3}|/")
        if int(age) <= 21 and age != 0:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9}|{' '*14} {' '*16}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9}|{' '*14} {' '*15}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9}|{' '*14} {' '*14}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9}|{' '*14} {' '*13}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9}|{' '*14} {' '*12}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9}|{' '*14} {' '*11}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9}|{' '*14} {' '*10}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9}|{' '*14} {' '*9}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9}|{' '*14} {' '*8}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9}|{' '*14} {' '*7}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9}|{' '*14} {' '*6}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}\|/{' '*12}   {' '*3}  ")
        if int(age) >= 21 and age <= 74:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9} {' '*14}|{' '*16}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9} {' '*14}|{' '*15}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9} {' '*14}|{' '*14}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9} {' '*14}|{' '*13}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9} {' '*14}|{' '*12}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9} {' '*14}|{' '*11}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9} {' '*14}|{' '*10}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9} {' '*14}|{' '*9}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9} {' '*14}|{' '*8}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9} {' '*14}|{' '*7}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9} {' '*14}|{' '*6}")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}   {' '*12}\|/{' '*3}  ")
        if int(age) >= 75:
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*9}\\{' '*10}{' '*9} {' '*14} {' '*16}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*10}\\{' '*9}{' '*9} {' '*14} {' '*15}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*11}\\{' '*8}{' '*9} {' '*14} {' '*14}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*12}\\{' '*7}{' '*9} {' '*14} {' '*13}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*13}\\{' '*6}{' '*9} {' '*14} {' '*12}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*14}\\{' '*5}{' '*9} {' '*14} {' '*11}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*15}\\{' '*4}{' '*9} {' '*14} {' '*10}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*16}\\{' '*3}{' '*9} {' '*14} {' '*9}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*17}\\{' '*2}{' '*9} {' '*14} {' '*8}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*18}\\{' '*1}{' '*9} {' '*14} {' '*7}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*19}\\{' '*0}{' '*9} {' '*14} {' '*6}/")
            print(f"{self.make_vertical_inner_separator(28, 28, is_solo_right=True)}{' '*20}\\|{' '*6}   {' '*12}   {' '*3}|/")


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

        # third level separators
        separator_for_3_first_level  = self.make_vertical_inner_separator(28, 28)
        separator_for_3_second_level = self.make_vertical_inner_separator(28, 28)
        separator_for_3_third_level  = self.make_vertical_inner_separator(28, 28)
        separator_for_3_fourth_level = self.make_vertical_outer_separator(27, 26)


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
        self.two_node_vertex_name_formatter(start_spacing=22, first_string=self.graph_names[4], middle_spacing=13, second_string=self.graph_names[5])
        print(separator_for_3_first_level)
        print(separator_for_3_second_level)
        print(separator_for_3_third_level)
        print(separator_for_3_fourth_level)
        self.two_node_vertex_name_formatter(start_spacing=21, first_string=self.graph_names[8], middle_spacing=16, second_string=self.graph_names[6], is_connected=True)
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
        separator_for_3_first_level  = self.make_vertical_inner_separator(28, 28, is_solo_left=True)
        separator_for_3_second_level = self.make_vertical_inner_separator(28, 28, is_solo_left=True)
        separator_for_3_third_level  = self.make_vertical_inner_separator(28, 28, is_solo_left=True)
        separator_for_3_fourth_level = self.make_vertical_outer_separator(27, 26, is_solo_left=True)


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
        self.two_node_vertex_name_formatter(start_spacing=22, first_string=self.graph_names[4], middle_spacing=13, second_string=self.graph_names[5],empty_first=True)
        print(separator_for_3_first_level)
        print(separator_for_3_second_level)
        print(separator_for_3_third_level)
        print(separator_for_3_fourth_level)
        self.two_node_vertex_name_formatter(start_spacing=21, first_string=self.graph_names[8], middle_spacing=16, second_string=self.graph_names[6], is_connected=True)
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
        separator_for_3_first_level  = self.make_vertical_inner_separator(28, 28, is_solo_right=True)
        separator_for_3_second_level = self.make_vertical_inner_separator(28, 28, is_solo_right=True)
        separator_for_3_third_level  = self.make_vertical_inner_separator(28, 28, is_solo_right=True)
        separator_for_3_fourth_level = self.make_vertical_outer_separator(27, 26, is_solo_right=True)


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
        self.two_node_vertex_name_formatter(start_spacing=22, first_string=self.graph_names[4], middle_spacing=13, second_string=self.graph_names[5],empty_second=True)
        print(separator_for_3_first_level)
        print(separator_for_3_second_level)
        print(separator_for_3_third_level)
        print(separator_for_3_fourth_level)
        self.two_node_vertex_name_formatter(start_spacing=21, first_string=self.graph_names[8], middle_spacing=16, second_string=self.graph_names[6], is_connected=True)
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