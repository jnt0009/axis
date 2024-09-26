from shiny import App, render, ui, reactive

app_ui = ui.page_sidebar(  
    ui.sidebar(
        "Game Settings", 
        ui.input_slider("n", "Number of players", 0, 4, 1),
        ui.output_text_verbatim("number_of_players"),
        ui.output_ui("player_selector"),
        ui.output_ui("player_name_in"),
        ui.output_text_verbatim("player_name_out"),


        bg="#f8f8f8"
        ),  
    "Main content", 
) 

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"
    
    # @render.ui
    @reactive.event(input.n) 
    def number_of_players():
        player_array = []
        for i in range(input.n()):
            player_array.append(f"Player {i+1}")
        print(player_array)
        return player_array
        return f"Number of players: {input.n()}"
    
    @render.ui
    @reactive.event(input.n) 
    def player_selector():
        if input.n():
            value = input.n()
            if value > 0:
                return ui.input_selectize("player1", 'Select player', number_of_players())
    
    @render.ui
    @reactive.event(input.player1) 
    def player_name_in():
        print(input.n())
        if input.n():
            value = input.n()
            if value > 0:
                return ui.input_text("name", "Name", "John Doe")


    #### TODO: Fix this the palying as name placard is not displaying.
    # @render.ui
    # @reactive.event(input.name) 
    # def player_name_out():
    #     if input.name():
    #         return f"Playing as: {input.player_name_in()}"


app = App(app_ui, server)