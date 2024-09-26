from shiny import App, render, ui, reactive
from shinywidgets import output_widget, render_widget  
import plotly.express as px
import pandas as pd


app_ui = ui.page_sidebar(  
    ui.sidebar(
        "Game Settings", 
        ui.input_slider("n", "Number of players", 0, 4, 1),
        ui.output_text_verbatim("number_of_players"),
        ui.output_ui("player_selector"),
        ui.output_ui("player_name_in"),
        ui.output_text_verbatim("player_name_out"),
        "Game Inputs",
        ui.input_slider("x_axis", "Horizontal Axis", 1, 10, 1),
        ui.input_slider("y_axis", "Vertical Axis", 1, 10, 1),
        ui.input_action_button("submit_button", "Submit"),  
        ui.input_switch("switch", "Ready", False),  

        bg="#f8f8f8"
        ),  
    "Axis", 
    output_widget("grid"),
    ui.output_data_frame("table")
) 

def server(input, output, session):

    def game_data(game: dict = None):
        shell = {
            "player": "1",
            "question": "seed",
            "horizontal": 0,
            "vertical": 0,
            "horizontal_trait": "",
            "vertical_trait": "",
        }
        return shell

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
                return ui.input_text("name", "Name", "Screen Name")
            
    @render.data_frame
    def table():
        data = game_data()
        return pd.DataFrame(data, index=[0])
        

    @render_widget
    def grid():
        data = game_data()
        df = pd.DataFrame(data, index=[1])
        scatterplot = px.scatter(
            data_frame=df,
            x="horizontal",
            y="vertical",
            color="player",
            hover_data=['player'],
        )
        return scatterplot



    #### TODO: Fix this the palying as name placard is not displaying.
    # @render.ui
    # @reactive.event(input.name) 
    # def player_name_out():
    #     if input.name():
    #         return f"Playing as: {input.player_name_in()}"


app = App(app_ui, server)