'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''
    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    
    fig=px.scatter()
    fig.update_layout(
        dragmode=False,
        xaxis= dict(
            visible= False
        ),
        yaxis=dict(
            visible= False
        ),  
        annotations= [
            dict(
                text= "No data to display. Select a cell in the heatmap for more information.",
                showarrow= False,
                font= dict(
                    size= 14
                )
            )
        ],
        plot_bgcolor="#ffffff" #THEME['background_color']
    )
    return fig



def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    fig.update_xaxes(range=[0,4])
    fig.update_yaxes(range=[0,4])
    fig.add_shape(
        type='rect',
        x0=0, x1=4,
        y0=1, y1=3,
        fillcolor='#DFD9E2', #THEME['pale_color']
        line_color='#ffffff' #THEME['background_color']
    )
    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    return None
